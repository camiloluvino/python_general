
#%%
# importamos librerias

from tabula import read_pdf 
import pandas as pd


#%%
# leer pdf 
doc = read_pdf("FMCA_17412886-3_202207_U_.pdf", pages = "all")

# devuelve una lista, que la llamamos "doc" que contiene el número de dataframes de acuerdo a las tablas que encontró.abs(x)
print("tipo de objeto:",type(doc))
print("número de elementos:",len(doc))

#%%
# crea un archivo llamado "pdf.xlsx"

writer = pd.ExcelWriter("pdf.xlsx")
# la idea es guardar cada tabla en una hoja aparte dentro del mismo excel

doc[0].to_excel(writer, sheet_name = "tabla 1")
doc[1].to_excel(writer, sheet_name = "tabla 2")
doc[2].to_excel(writer, sheet_name = "tabla 3")

writer.save()

# %%
# hacemos lo mismo que el anterior de modo iterativo en vez de definir cada dataframe.

writer = pd.ExcelWriter("pdf1.xlsx")
i=1
for tabla in doc:
   tabla.to_excel(writer, sheet_name = "tabla"+str(i))
   i = i+1
    
writer.save()    

#%%
# un paréntesis, para concatenar dos o más strings, sólo basta sumarlos 
string1 = "tabla"
string2 = "2"
string = string1 +"-" +string2 
print(string)

#%%
#importamos la libreria glob
import glob

#la libreria tiene una funcion que permite encontrar archivos con algún patrón, en este caso los archivos pdf que están en la carpeta "ejemplos_pdf"
archivos = glob.glob("ejemplos_pdf/*.pdf")

#la funcion devuelve una lista que la llamamos "archivos"

doc = read_pdf(archivos[0], pages = "all")

#%%
# todos las tablas de la lista la guardamos de forma iterativa en un solo dataframe

df = pd.DataFrame()
for page in doc:
    df= pd.concat([df,page])

    
#%%

