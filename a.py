from home.models import Diario, onlyBc, Res2004
import pandas as pd
import datetime
import math
# cargamos los datos del csv al mysql
# unsa 50000 lineas

f = Diario.objects.values('codcta').order_by('codcta').distinct()

def parser(date):
    # "05/05/2004"
    date = date[:-4]+date[-2:]
    obj = datetime.datetime.strptime(date, "%d/%m/%y")
    return obj.date()

def ingData():
    #filename = "home/DIARIOD_v2.csv"
    #df = pd.read_csv(filename)
    #Datos unicos codcta
    f = Diario.objects.values('codcta').order_by('codcta').distinct()

    #for p in Diario.objects.raw("select id, peri, codcta, sum(monmn) from home_diario where monmn > 0 and codcta = '10900000' group by codcta,peri order by peri"):
    #    print(p)

    for y in f:
        s = str(y['codcta'])
        u, d, t, c, ci, d, nn = True, True, True, True, True, True, True

        hb1, db1, hb2, db2, hb3, db3, hb4, db4 = True, True, True, True, True, True, True, True
        try:
            aaaa = str(2004)
        except:
            u = False

        try:
            codcta = str(s)
            d = True
        except:
            d = False
        
        try:
            f = onlyBc.objects.filter(codcta=s)
            if f:
                de0 = float(abs(f[0].debe00))
            else:
                de0 = float(0)
        except : 
            t = False

        try:
            f = onlyBc.objects.filter(codcta=s)
            if f:
                ha0 = float(f[0].haber00)
            else:
                ha0 = float(0)
        except : 
            c = False
        
        #Haber y debe 1

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn > 0 and codcta = '" + s + "' and peri = '200401' group by codcta,peri order by peri")
            if f:
                ha1 = float(f[0].monto)
            else:
                ha1 = float(0)
            
        except : 
            hb1 = False

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn < 0 and codcta = '" + s + "' and peri = '200401' group by codcta,peri order by peri")
            if f:
                de1 = float(abs(f[0].monto))
            else:
                de1 = float(0)
            
        except : 
            db1 = False
        
        #Haber y debe 2

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn > 0 and codcta = '" + s + "' and peri = '200402' group by codcta,peri order by peri")
            if f:
                ha2 = float(f[0].monto)
            else:
                ha2 = float(0)
            
        except : 
            hb2 = False

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn < 0 and codcta = '" + s + "' and peri = '200402' group by codcta,peri order by peri")
            if f:
                de2 = float(abs(f[0].monto))
            else:
                de2 = float(0)
            
        except : 
            db2 = False

        #Haber y debe 3

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn > 0 and codcta = '" + s + "' and peri = '200403' group by codcta,peri order by peri")
            if f:
                ha3 = float(f[0].monto)
            else:
                ha3 = float(0)
            
        except : 
            hb3 = False

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn < 0 and codcta = '" + s + "' and peri = '200403' group by codcta,peri order by peri")
            if f:
                de3 = float(abs(f[0].monto))
            else:
                de3 = float(0)
            
        except : 
            db3 = False

        #Haber y debe 4

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn > 0 and codcta = '" + s + "' and peri = '200403' group by codcta,peri order by peri")
            if f:
                ha4 = float(f[0].monto)
            else:
                ha4 = float(0)
            
        except : 
            hb3 = False

        try:
            f = Diario.objects.raw("select id, peri, codcta, sum(monmn) as monto from home_diario where monmn < 0 and codcta = '" + s + "' and peri = '200403' group by codcta,peri order by peri")
            if f:
                de4 = float(abs(f[0].monto))
            else:
                de4 = float(0)
            
        except : 
            db4 = False

        if all([hb1, db1, hb2, db2, hb3, db3, hb4, db4, u, d, t, c, ci, d, nn]) == True:
            obj = Res2004(
                aaaa=aaaa, 
                codcta=codcta, 
                debe00=round(de0,2),
                haber00=round(ha0,2), 
                debe01=round(de1,2),
                haber01=round(ha1,2), 
                debe02=round(de2,2),
                haber02=round(ha2,2), 
                debe03=round(de3,2),
                haber03=round(ha3,2), 
                debe04=round(de4,2),
                haber04=round(ha4,2)
                ) 

            obj.save()
        else:
            print("No copio: " + codcta)




def dumData():
    filename = "home/DIARIOD_v2.csv"
    df = pd.read_csv(filename)

    for row in df.itertuples():
        u, d, t, c, ci, s, nn = True, True, True, True, True, True, True
        try:
            date = parser(row.FECASI)
            u = True
        except:
            u = False

        try:
            dateA = str(row.FECASI)
            de = dateA[6:10] + dateA[3:5]
            nn = True
        except:
            nn = False
        try:
            lib = str(row.LIB)
            d = True
        except:
            d = False
        try:
            asiento = int(row.NROASI)
            t = True
        except:
            t = False
        try:
            nrodoc = str(row.NRODOC)
            c = True
        except:
            c = False
        try:
            codcta = str(row.CODCTA)
            ci = True
        except:
            ci = False
        try:
            monmn = float(row.MONMN)
            s = True
        except:
            s = False
        if all([u, d, t, c, ci, s, nn]) == True:
            isNaN = False
            if(nrodoc == "nan"):
                isNaN = True
            else:
                isNaN = False

            if(isNaN):
                obj = Diario(peri=de, fecasi=date, lib=lib,
                             nroasi=asiento, codcta=codcta, monmn=monmn)
                obj.save()
            else:
                obj = Diario(peri=de, fecasi=date, lib=lib, nroasi=asiento,
                             nrodoc=nrodoc, codcta=codcta, monmn=monmn)
                obj.save()
        else:
            print(u, d, t, c, ci, s, nn)

def dum():
    filename = "home/RES2004.csv"
    df = pd.read_csv(filename)

    for row in df.itertuples():
        u, d, t, c, ci, s, nn = True, True, True, True, True, True, True
        try:
            cod = str(row.CODCTA)
            u = True
        except:
            u = False

        try:
            debe = float(row.DEBE00)
            d = True
        except:
            d = False
        try:
            haber = float(row.HABER00)
            t = True
        except:
            t = False
        
        print(row.DEBE00)
        if all([u, d, t, c, ci, s, nn]) == True:
            obj = onlyBc(codcta=cod, debe00=debe, haber00 = haber)
            obj.save()
        else:
            print(u, d, t, c, ci, s, nn)

    

def fu():
    f = Diario.objects.values('codcta').order_by('codcta').distinct()
    print(f)


def main():
    dumData()


def asd():
    Diario.objects.all().delete()


if __name__ == "__main__":
    main()
