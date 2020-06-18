# Importar librerias necesarias para correr la app
from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config

# Las funciones view_config le dicen a Pyramid qué vista de ruta se va a definir en la función que sigue

@view_config(route_name='intro')
def home_page(request):
    boot='<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
    header = '<h1 class="text-light bg-dark">MI PRIMER FORMULARIO</h1>'

    body = '<form><div class="form-group"><label for="exampleFormControlInput1">MATRICULA</label><input type="number" class="form-control" id="ControlInput1" placeholder="17180000"></div><div class="form-group"><label for="exampleFormControlInput1">NOMBRE</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com"></div><div class="form-group"><label for="exampleFormControlInput1">PRIMER APELLIDO</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com"></div><div class="form-group"><label for="exampleFormControlInput1">SEGUNDO APELLIDO</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com"></div><div class="form-group"><label for="exampleFormControlInput1">EDAD</label><input type="number" class="form-control" id="exampleFormControlInput1" placeholder="18"></div><div class="form-group"><label for="exampleFormControlInput1">FECHA DE NACIMIENTO</label><input type="date" class="form-control" id="exampleFormControlInput1" placeholder=""></div><div><select class="form-control form-control"><option>Hombre</option><option>Mujer</option><option>Otro</option></select></div> <div><label for="validationDefault04">Estado</label><select class="custom-select" id="validationDefault04" required><option selected disabled value="">Choose...</option><option>...</option></select></div><br><br>'
    
    body += '<body background="https://image.freepik.com/vector-gratis/fondo-formas-abstractas-triangulo-azul_1035-17551.jpg">'

    button='<a class="btn btn-danger" href="/fer" role="button">GUARDAR</a>'

    # En la etiqueta 'a', observe que href contiene '/ fer', esta ruta se definirá en el archivo intro.py
    # Simplemente le dice a la vista que navegue a esa ruta y ejecute cualquier código que esté en esa vista

    return Response(boot + header +  body + button )





@view_config(route_name='fer')
def fer_history(request):
    header = '<h2 style="text-align: center; color:white;">Fernando Hernadez Vazquez</h2>'
    data = '<p style="text-align: center; color:white; font-family: verdana;">Universidad tecnologica de Tulancingo</p><p style="text-align: center; color:white;">HOLAA</p><p style="text-align: center; color:white; font-family: verdana;"><p style="text-align: center; color:white; font-family: verdana;">Para <a href="/">volver a inicio</a>.</p><body background="https://image.freepik.com/vector-gratis/concepto-fondo-luces-neon_52683-35551.jpg">'

    return Response(header + data)