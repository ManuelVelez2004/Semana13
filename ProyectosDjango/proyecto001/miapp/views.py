from django.shortcuts import render, HttpResponse


# Create your views here.


layout = """
    <h1> Proyecto Web (LP3 - 2024) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/0/100"> Mostrar Números [0,100]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = [ 'Isabella Caballero', 
                    'Alejandro Hermitaño',
                    'Joan Palomino',
                    'Pierre Bernaola']


    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })


def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Mg. Flor Elizabeth Cerdán León'
    }
)

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)


def rango2(request,a,b):
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)