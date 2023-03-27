import pandas as pd
# read_xml() esta en las ultimas versiones de pandas
df_cardata = pd.read_csv("C:/Users/slmanzano/Desktop/Sara/Talent Camp/Python/presentado/cardata.csv",sep=",",encoding="ISO-8859-1")

print(df_cardata)
print("\t")

#"PRECIO","COSTE MANTENIMIENTO","PUERTAS","CAPACIDAD","TAMAÑO","SEGURIDAD","DECISION"
cardata = df_cardata.rename(columns={'vhigh':'PRECIO',
                                   'PUERTAS':'vhigh.1'})

cardata.columns
print(df_cardata.columns)
