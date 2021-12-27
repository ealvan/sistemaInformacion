from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Diario
import mysql.connector
# Create your views here.
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Jeampier123A",
	database="sisinf"
)
def Obtener_hoja_trabajo(ANIO,MES,LIMITARCUENTAS):
    mycursor = mydb.cursor(buffered=True,dictionary=True)
    args = [ANIO,MES,LIMITARCUENTAS]
    mycursor.callproc('GetHojadeTrabajoFull',args)
    strquery="SELECT * from hoja_de_trabajo_full"
    mycursor.execute(strquery)
    myresult = mycursor.fetchall()
    return myresult
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
