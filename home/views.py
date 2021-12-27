from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views import View
from .models import Diario
# import mysql.connector
# Create your views here.
# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="edsel",
# 	database="sisinf"
# )




def Obtener_hoja_trabajo(ANIO,MES,LIMITARCUENTAS,typo=None):
    rows = []
    with connection.cursor() as cursor:
        cursor.execute(f"call GetHojadeTrabajoFull({ANIO},{MES},{LIMITARCUENTAS})")
        if(typo == "all"):
            rows = cursor.fetchall()
        else:
            for _ in range(100):
                data = cursor.fetchone()
                rows.append(data)
    return rows

def principal(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "base.html", {})

def result(request, *args, **kwargs):
    return render(request, "imprimir.html", {})

class MensajeJsonEnviados(View):
    def get(self, request, *args, **kwargs):
        start = request.GET['var1']
        start2 = request.GET['var2']
        k = Obtener_hoja_trabajo(2004,int(start),int(start2))
        return JsonResponse(list(k), safe=False)

from openpyxl import Workbook
def makeFile(anio,mes,digit):
    # import os
    # from sisinfo.settings import BASE_DIR
    # path = os.path.join(BASE_DIR,"home","static","xlsxs","hw.xlsx")
    wb = Workbook()
    sheet = wb.active

    header = ["AÑO","COD CTA","DEBE acumulado","HABER acumulado","DEBE01","HABER01","DEBE TOTAL","HABER TOTAL","DEUDOR","ACREEDOR"]
    hcol = 'A'
    for head in header:
        sheet[f"{hcol}2"] = head
        curr = ord(hcol)
        curr +=1
        hcol = chr(curr)

    results = Obtener_hoja_trabajo(anio,mes,digit,typo="all")

    fil = 3
    for row in results:
        col = 'A'
        fil += 1
        for item in row[1:]:
            sheet[f"{col}{fil}"] = item
            current = ord(col)
            current+=1
            col = chr(current) 
    wb.save(filename="hw.xlsx")

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







