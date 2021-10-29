import datetime
import re
import pprint as pp
import os
#CUT BY PERIOD
import pandas as pd

def customDataFrame(filename):
    df = pd.read_csv(filename,sep=',')
    df = df.drop(columns=["PERI","NRODOC"])
    return df

def cutByPeriod(df,period):
    df = df.loc[df["FECASI"].str.contains("\d\d\/"+period +"/\d\d",regex=True)]
    return df

def sliceByDebeHaber(df):
    dfHaber = df.loc[df["MONMN"] < 0]
    dfDebe =  df.loc[df["MONMN"] > 0]

    #SORT DF BY NROASI
    dfHaber = dfHaber.sort_values(["NROASI"],ascending=True)
    dfDebe = dfDebe.sort_values(["NROASI"], ascending=True)

    return (dfDebe,dfHaber)
def mergeDataFrames(df1,df2):
    #PERI,FECASI,LIB,NROASI,NRODOC,CODCTA,MONMN
    cols = ["FECASI","LIB","NROASI","CODCTA","MONMN"]
    # dicHaber = {}
    # dicDebe = {}

    # for item in cols:
    #     for newItem in cols:
    #         dicHaber.setdefault(item,item+"_haber")
    #         dicDebe.setdefault(item,item+"_debe")

    # pp.pprint(dicDebe)
    # pp.pprint(dicHaber)    

    df1 = df1.rename(columns={'CODCTA': 'CODCTA_debe',
    'FECASI': 'FECASI_debe',
    'LIB': 'LIB_debe',
    'MONMN': 'MONMN_debe',
    'NROASI': 'NROASI_debe'})
    df2 = df2.rename(columns={'CODCTA': 'CODCTA_haber',
    'FECASI': 'FECASI_haber',
    'LIB': 'LIB_haber',
    'MONMN': 'MONMN_haber',
    'NROASI': 'NROASI_haber'})
    
    print(df1.head())
    print(df2.head())
    mergeDF = pd.concat([df1["MONMN_debe"],df2["MONMN_haber"]],axis=1)
    # print(merge.head(12))
    # mergeDF = merge

    #mergeDF = df1["NROASI_debe"]+df1["MONMN_debe"] + df2["NROASI_haber"] + df2["MONMN_haber"]
    # except:
    #     print("Some goes wrong")
    #return None
    return mergeDF

def saveDataFrame(df,filename):
    if df.empty:
        print("DF is None")
        return
    path = "sliceByDebeHaber/"+filename
    typ = os.path.splitext(path)[1]

    df.to_csv(path,index=False,sep=',')

    if typ == ".csv":
        df.to_csv(path,index=False,sep=',')
    elif typ == ".xlsx":
        df.to_excel(path,index=False)
    else:
        return None

def cutByNroAsiento(df,field,init,fin):
    #de la 10:59 por ejemplo
    # campo = field
    # init = 10
    # final = 59
    try:

        cutDf = df.loc[(df[field] >= init) & (df[field] <= fin)] 
        return cutDf
    except:
        print("Something goes rown in cutByNroAsiento()")
        return
    # print(cutDf.head(20))
def main():
    filename="DIARIOD.csv"

    #init dataframe
    df = customDataFrame(filename)
    period="01"
    #delete unnecesary columns
    df = df.drop(columns=["LIB","CODCTA"])
    #cut by period
    df = cutByPeriod(df,period)
    # slice by haber and debe
    dfDebe,dfHaber = sliceByDebeHaber(df)
    #delete unnecesary columns
    dfDebe.drop(columns=["FECASI"])
    dfHaber.drop(columns=["FECASI"])
    #group by PERIOD
    dfDebe = dfDebe.groupby(["NROASI"]).sum()
    dfHaber = dfHaber.groupby(["NROASI"]).sum()
    saveDataFrame(dfDebe,"debe_02_sumByNroAsi.xlsx") 
    saveDataFrame(dfHaber,"haber_02_sumByNroAsi.xlsx") 
    
    # dfDebe1059 = cutByNroAsiento(dfDebe,"NROASI",10,59)
    
    # saveDataFrame(dfDebe1059,"debe_01_10_59.xlsx")
    # cutByNroAsiento(dfHaber,"NROASI")
    
    # mergeDF = mergeDataFrames(dfDebe,dfHaber)
        # SAVE files
    #saveDataFrame(mergeDF,"debe-haberOnly.xlsx")
        # saveDataFrame(dfDebe,"per01-debe1.xlsx")
        # saveDataFrame(dfHaber,"per01-haber1.xlsx")
    print("Success")


if __name__ == "__main__":
    main()


def matchParser(period,data):
    pattern = "\d\d\/"+period +"/\d\d"
    obj = re.search(pattern,"01/01/04")
    return bool(obj)

#matchParser("02","01/01/04")




def parser(date):
    #"05/05/2004"
    date = date[:-4]+date[-2:]
    obj = datetime.datetime.strptime(date,"%d/%m/%y")

#parser("05/05/2004")




