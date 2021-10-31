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
    filename = "home/DIARIOD.csv"
    df = pd.read_csv(filename)
    for row in df.itertuples():
        date = parser(row.FECASI)
        lib = str(row.LIB)
        asiento = int(row.NROASI)
        nrodoc = str(row.NRODOC)
        codcta = str(row.CODCTA)
        monmn = float(row.MONMN)
        if(math.isnan(row.NRODOC)==True):
            obj = Diario(fecasi=date,lib=lib,nroasi=asiento,codcta=codcta,monmn=monmn)
            obj.save()
        else:
            obj = Diario(fecasi=date,lib=lib,nroasi=asiento,nrodoc=nrodoc,codcta=codcta,monmn=monmn)
            obj.save()
            
def main():
    dumData()
    
if __name__ == "__main__":
    main()



