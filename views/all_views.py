# Importar librerias necesarias para correr la app
from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config

# Las funciones view_config le dicen a Pyramid qué vista de ruta se va a definir en la función que sigue

@view_config(route_name='intro')
def home_page(request):
    boot='<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
    header = '<p class="text-light bg-dark">MI PRIMER FORMULARIO</p>'

    body = '<form> <div class="row"> <div class="col"> <input type="number" class="form-control" placeholder="Matricula"> </div> <div class="col"> <input type="text" class="form-control" placeholder="Nombre"> </div> </div></form><div class="row"> <div class="col"> <input type="text" class="form-control" placeholder="Primer Apellido"> </div><div class="col"> <input type="text" class="form-control" placeholder="Segundo Apellido"></div><div class="col"> <input type="text" class="form-control" placeholder="Segundo Apellido"></div>'
    
    body += '<body background="https://image.freepik.com/vector-gratis/fondo-formas-abstractas-triangulo-azul_1035-17551.jpg">'

    button='<br><button type="button" class="btn btn-primary">Primary</button>'

    # En la etiqueta 'a', observe que href contiene '/ fer', esta ruta se definirá en el archivo intro.py
    # Simplemente le dice a la vista que navegue a esa ruta y ejecute cualquier código que esté en esa vista

    return Response(boot + header +  body + button)





@view_config(route_name='fer')
def fer_history(request):
    header = '<h2 style="text-align: center; color:white;">Fernando Hernadez Vazquez</h2>'
    data = '<p style="text-align: center; color:white; font-family: verdana;">Universidad tecnologica de Tulancingo</p><p style="text-align: center; color:white;">HOLAA</p><p style="text-align: center; color:white; font-family: verdana;"><p style="text-align: center; color:white; font-family: verdana;">Para <a href="/">volver a inicio</a>.</p><body background="https://image.freepik.com/vector-gratis/concepto-fondo-luces-neon_52683-35551.jpg">'

    return Response(header + data)