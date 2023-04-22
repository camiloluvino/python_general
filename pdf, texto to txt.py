# %% SEPARAR PÁGINAS Y COLAPSAR INTERNAMENTE GROUP EVERY 10 PAGES AND GENERATE A .MD FOR EACH GROUP OF 10

import os
import PyPDF2

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

pdf_path = r"C:\Users\redk8\OneDrive\Documentos\Araujo - 2022 - The Circuit of Detachment in Chile Understanding _61.pdf"
output_directory = r"C:\Users\redk8\OneDrive\Documentos\Proyectos Python\python_general\resultados"
create_directory(output_directory)

pdf_file = open(pdf_path, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

total_pages = len(pdf_reader.pages)
pages_per_file = 10

for start_page in range(0, total_pages, pages_per_file):
    end_page = min(start_page + pages_per_file, total_pages)
    file_name = f"araujoCircuitDetachmentChile2022VII_{start_page+1}-{end_page}.md"
    output_path = os.path.join(output_directory, file_name)

    text = ""
    for page_num in range(start_page, end_page):
        page_text = pdf_reader.pages[page_num].extract_text()
        page_text = ' '.join(page_text.split('\n'))
        page_text = page_text.replace("\xad", "").replace("\x00", "")
        text += page_text
        if page_num < end_page - 1:
            text += '\n\n\n'

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

# Guardar el texto original en un archivo de texto
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

with open(os.path.join(output_directory, "texto_original.txt"), "w", encoding="utf-8") as text_file:
    text_file.write(text)


    # %%
