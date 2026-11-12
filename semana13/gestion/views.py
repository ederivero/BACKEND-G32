from rest_framework.viewsets import ModelViewSet
from .serializers import JugadorSerializer, PuntuacionSerializer
from .models import Jugador, Puntuacion
from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

# si queremos usar el enrutador de DRF este solamente va a funcionar con los viewsets o con los APIViews, mas no funcionara con los generics views
# https://www.django-rest-framework.org/api-guide/viewsets/
class JugadorApiView(ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()

class PuntuacionApiView(ModelViewSet):
    serializer_class = PuntuacionSerializer
    queryset = Puntuacion.objects.all()

    # Este decorador permite agregar endpoints personalizados dentro de un Viewset
    # Para acceder a este endpoint tenemos que agregar la sub-url /ranking al final ya que estamos agregando un nuevo endpoint en vez de modificar el retrieve o list propios del viewset
    @action(detail=False, methods=['GET'])
    def ranking(self, request: Request):
        # Primero obtengo la data desde el redis en vez de ir a la bd
        data = cache.get('ranking_top10')

        if data is None:
            print("ESTA VACIO LA CACHE")
            # En el order_by se puede order ascendentemente solo colocando el nombre de la propiedad pero si quiere ordenar descendentenmente entonces al comienzo se le pone un guion (-)
            # En el ORM de django no hay limit ni offset, sino que se coloca como si fuese posicion de una lista y eso al hacer la consulta en la bd se hace la paginacion correspondiente (se agrega el limit y el offset si es necesario)
            # SELECT score, nombre 
            # FROM puntuaciones AS p INNER JOIN jugadores AS j ON p.jugador_id = j.id 
            # LIMIT 10 
            # ORDER BY score DESC;
            nuevaData = list(Puntuacion.objects.order_by('-score').values('jugador__nombre','score')[:10])
            data=nuevaData
            # Guardare la nueva informacion proveniente de la bd de postgres en mi bd de redis con un tiempo de espera maximo de 30 seg sino lanzara un error
            # timeout sirve para indicar cuanto tiempo va a durar en la bd de redis esta informacion, luego de ese tiempo automaticamente sera eliminada para evitar mostrar informacion pasada que ya no es relevante
            cache.set('ranking_top10', nuevaData, timeout=60)

        return Response(data)