from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Diario
from django.db import connection

# Create your views here.


def principal(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "base.html", {})

def tablaDeSaldos(request):
    # cursor = connections.cursor()
    #getTablaSaldos()
    # cursor.callproc("getTablaSaldos()")
    rows = []
    with connection.cursor() as cursor:
        cursor.execute("CALL getTablaSaldos()")
        for _ in range(100):
            data = cursor.fetchone()
            rows.append(data)
    # print("**_**=",rows[0][1])
    context = {
        "tabla":rows
    }

    return render(request, "tabla_de_saldos.html",context)



class MensajeJsonEnviados(View):
    def get(self, request, *args, **kwargs):
        start = request.GET['start']
        print(start)
        queryset = Diario.objects.filter(id=5)
        return JsonResponse(list(queryset.values()), safe=False)







