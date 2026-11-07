from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacionEstandar(PageNumberPagination):
    # Este atributo modificara el tamaño de elementos que retornaremos por pagina
    page_size = 5

    # Es el query param que se usara para poder indicar la cantidad de elementos que se mostraran pero tiene que ser menor que el max_page_size porque si es mayor, usara el max_page_size y si no es proveido se usara el page_size
    page_size_query_param = "cantidad"

    # Es el limite que podemos retornar de elementos por pagina
    max_page_size = 10

    # Es el query param que se usara para poder seleccionar que pagina queremos navegar
    page_query_param = "pagina"

    # Este mensaje se mostrara cuando ingresemos a una pagina que no es correcta
    invalid_page_message = "Pagina invalida"
    

    def get_paginated_response(self, data):
        # el parametro data contendra toda la informacion a paginar
        return Response({
            "content": data,
            "paginacion": {
                "total": self.page.paginator.count, # total de elementos que hay en la busqueda
                "pagina_actual": self.page.number, # La pagina en la que me encuentro
                "total_paginas": self.page.paginator.num_pages, # Total de paginas que puedo navegar
                "siguiente": self.get_next_link(), # la url de la pagina siguiente (si hay)
                "anterior": self.get_previous_link() # la url de la pagina anterior (si hay)
            }
        })

    