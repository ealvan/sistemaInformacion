from home.models import Diario
import pandas as pd
import datetime
import math
#cargamos los datos del csv al mysql
#unsa 50000 lineas
def parser(date):
    #"05/05/2004"
    date = date[:-4]+date[-2:]
    obj = datetime.datetime.strptime(date,"%d/%m/%y")
    return obj.date()

def dumData():
    filename = "home/DIARIOD_v2.csv"
    df = pd.read_csv(filename)

    for row in df.itertuples():
        u,d,t,c,ci,s = True,True,True,True,True,True
        try:
            date = parser(row.FECASI)
            u=True
        except:
            u=False
        try:
            lib = str(row.LIB)
            d=True
        except:
            d=False
        try:
            asiento = int(row.NROASI)
            t=True
        except:
            t=False
        try:
            nrodoc = str(row.NRODOC)
            c=True
        except:
            c=False
        try:
            codcta = str(row.CODCTA)
            ci=True
        except:
            ci=False
        try:
            monmn = float(row.MONMN)
            s=True
        except:
            s=False
        if all([u,d,t,c,ci,s]) == True:
            isNaN = False
            if(nrodoc == "nan"):
                isNaN = True
            else:
                isNaN = False

            if(isNaN):
                obj = Diario(fecasi=date,lib=lib,nroasi=asiento,codcta=codcta,monmn=monmn)
                obj.save()
            else:
                obj = Diario(fecasi=date,lib=lib,nroasi=asiento,nrodoc=nrodoc,codcta=codcta,monmn=monmn)
                obj.save()    
        else:
            print(u,d,t,c,ci,s)   
            
def main():
    dumData()
    
if __name__ == "__main__":
    main()


