from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views import View
from .models import Diario
import mysql.connector
# Create your views here.
# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="edsel",
# 	database="sisinf"
# )
def Obtener_hoja_trabajo(ANIO,MES,LIMITARCUENTAS):
    rows = []
    with connection.cursor() as cursor:
        cursor.execute("call GetHojadeTrabajoFull(2004,3,4)")
        for _ in range(100):
            data = cursor.fetchone()
            rows.append(data)

    # mycursor = mydb.cursor(buffered=True,dictionary=True)
    
    # args = [ANIO,MES,LIMITARCUENTAS]
    
    # mycursor.callproc('GetHojadeTrabajoFull',args)
    # strquery="SELECT * from hoja_de_trabajo_full"
    # mycursor.execute(strquery)
    # myresult = mycursor.fetchall()
    # return myresult
    #mycursor.close()
def principal(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "base.html", {})

def result(request, *args, **kwargs):
    return render(request, "imprimir.html", {})

class MensajeJsonEnviados(View):
    def get(self, request, *args, **kwargs):
        queryset = Diario.objects.filter(id=5)
        k = Obtener_hoja_trabajo(2004,2,2)
        return JsonResponse(list(k), safe=False)


# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views import View
# from .models import Diario
# from django.db import connection

# # Create your views here.


# def principal(request, *args, **kwargs):
#     print(args, kwargs)
#     return render(request, "base.html", {})

# def tablaDeSaldos(request):
#     # cursor = connections.cursor()
#     #getTablaSaldos()
#     # cursor.callproc("getTablaSaldos()")
#     rows = []
#     with connection.cursor() as cursor:
#         cursor.execute("CALL getTablaSaldos()")
#         for _ in range(100):
#             data = cursor.fetchone()
#             rows.append(data)
#     # print("**_**=",rows[0][1])
#     context = {
#         "tabla":rows
#     }

#     return render(request, "tabla_de_saldos.html",context)



# class MensajeJsonEnviados(View):
#     def get(self, request, *args, **kwargs):
#         start = request.GET['start']
#         print(start)
#         queryset = Diario.objects.filter(id=5)
#         return JsonResponse(list(queryset.values()), safe=False)







