from django.http import HttpResponse

def index(request):
    html = """
        <h1> Inicio </h1>
        <p> Años hasta el 2050: </p>
    """

    year = 2023

    while year <=2050:
        if year%2==0:
            html += f"<li>{str(year)}</li>"
        year +=1

    html += "</ul>"
    
    return HttpResponse(html)
