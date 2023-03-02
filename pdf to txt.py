# IMPORTAR LIBRERIAS
# %%
from tabula import read_pdf
import pandas as pd

# 
# %%
doc = read_pdf("fuentes de datos/epubPdf_toMarkdownTxt/FMCA_17412886-3_202207_U_.pdf", pages = "all")

# crea un archivo llamado "tablas fundos mutuos.xlsx"
writer = pd.ExcelWriter("resultados/tablas fondos mutuos.xlsx")

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
import glob
path = r"C:\Users\redk8\Documents\Proyectos en Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\FMCA*.pdf"
files = glob.glob(path)
print(files)

#la libreria tiene una funcion que permite encontrar archivos con algún patrón, en este caso los archivos pdf que están en la carpeta "ejemplos_pdf"
archivos = glob.glob("ejemplos_pdf/*.pdf")

#la funcion devuelve una lista que la llamamos "archivos"
doc = read_pdf(archivos[0], pages = "all")

#%%
# todos las tablas de la lista la guardamos de forma iterativa en un solo dataframe

df = pd.DataFrame()
for page in doc:
    df= pd.concat([df,page])

# %%
## Versión Chat GPT con varios excel
def process_pdfs(pdf_files, excel_file):
    # Create the ExcelWriter object
    writer = pd.ExcelWriter(excel_file)
    # Iterate through the list of PDF files
    for i, pdf_file in enumerate(pdf_files):
        # Read the PDF and extract the tables
        doc = read_pdf(pdf_file, pages = "all")
        # Iterate through the list of tables
        for j, df in enumerate(doc):
            # Write each table to a different sheet in the Excel file
            df.to_excel(writer, sheet_name = f"tabla {i+1}_{j+1}")
    # Save the Excel file
    writer.save()

pdf_files = [
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202207_U_.pdf',
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202208_U_.pdf',
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202209_U_.pdf',
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202210_U_.pdf',
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202211_U_.pdf',
    'C:\\Users\\redk8\\Documents\\Proyectos en Python\\python_general\\fuentes de datos\\epubPdf_toMarkdownTxt\\FMCA_17412886-3_202212_U_.pdf'
]
process_pdfs(pdf_files, "resultados/tablas fondos mutuos v.2.xlsx")

#%%
# read pdf postulaciones doctorado
basedoctorado = read_pdf(r"C:\Users\redk8\Dropbox\Graph_cosascotidianas\postulación beca anid 2022\documentación postulación año académico 2023\RES_1808_2023_ADJUDICACION_E2100_2023.pdf", pages="all")
# create a pandas dataframe with the first 55 elements of basedoctorado
df = pd.concat(basedoctorado[:57], axis=0)
# create an excel writer object and write the dataframe to the first sheet of the excel file
basedoctorado_paraexcel = pd.ExcelWriter("resultados/base doctorado.xlsx", engine='xlsxwriter')
df.to_excel(basedoctorado_paraexcel, sheet_name='Sheet1', index=False)
# save and close the excel file
basedoctorado_paraexcel.save()

# %%
# Extraer texto de pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

input_pdf = 'fuentes de datos/epubPdf_toMarkdownTxt/Brown - 2021 - En las ruinas del neoliberalismo el ascenso de la.pdf'

def pdf_to_text(input_file,output):
    i_f = open(input_file,'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr,retData, laparams= LAParams())
    interpreter = PDFPageInterpreter(resMgr,TxtConverter)
    for page in PDFPage.get_pages(i_f):
        interpreter.process_page(page)
 
    txt = retData.getvalue()
    print(txt)
    with open(output,'w') as of:
        of.write(txt)
 
output_txt = 'resultados/Brown - 2021 - En las ruinas del neoliberalismo el ascenso de la.txt'
pdf_to_text(input_pdf,output_txt)
