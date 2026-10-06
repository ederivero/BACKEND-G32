from math import ceil

def paginationInfo(total, pagina, porPagina):
    # Es la encargada de indicar cuantos elementos por pagina contendra el resultado
    itemsPorPagina = porPagina if total >= porPagina else total 
    # Esta propiedad me indicara cuantas paginas en total puede el usuario navegar y esto se calcula en base al total entre los elementos por pagina redondeado 
    # el metodo ceil sirve para redondear el numero flotante al siguiente numero entero sin importar si es 3.1 > 4, 3.99 > 4
    totalPaginas = ceil(total / itemsPorPagina) if itemsPorPagina > 0 else None 
    paginaPrevia = pagina - 1 if pagina > 1 and pagina <= totalPaginas else None
    paginaSiguiente = pagina + 1 if totalPaginas > 1 and pagina < totalPaginas else None

    return {
        'porPagina': itemsPorPagina,
        'total': total,
        'pagina': pagina,
        'paginaPrevia': paginaPrevia,
        'paginaSiguiente': paginaSiguiente,
        'totalPaginas': totalPaginas
    }