# Import necessary functions to run our web app

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def main():
    with Configurator() as config:
        # En la función add_route, el primer parámetro define el nombre de la ruta
        # y el segundo parámetro define la 'ruta' o la ubicación de la página
        config.add_route('intro', '/')
        config.add_route('fer', '/fer')
        
        # La función de escaneo escanea nuestro directorio de proyectos en busca de un archivo llamado all_views.py
        # y conecta las rutas que proporcionamos anteriormente con sus vistas relevantes
        config.scan('all_views')

        application = config.make_wsgi_app()

    # Las siguientes líneas de código configuran e inician un servidor que aloja nuestro
    # sitio web localmente
    server = make_server('0.0.0.0', 8081, application)
    server.serve_forever()

main()