#%% cambiar extensiones de str a txt
import os

file_paths = [
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x01 - The Sopranos.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x02 - 46 Long.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x03 - Denial  Anger  Acceptance.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x04 - Meadowlands.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x05 - College.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x06 - Pax Soprana.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x07 - Down Neck.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x08 - The Legend of Tennessee Moltisanti.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x09 - Boca.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x10 - A Hit is a Hit.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x11 - Nobody Knows Anything.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x12 - Isabella.HDTV.fr.srt",
    r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x13 - I Dream of Jeannie Cusamano.HDTV.fr.srt"
]

for file_path in file_paths:
    # Split the file path into directory, filename, and extension
    file_dir, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)

    # Change the extension to .txt
    new_ext = ".txt"
    new_file_name = file_base + new_ext
    new_file_path = os.path.join(file_dir, new_file_name)

    # Rename the file
    os.rename(file_path, new_file_path)

#%% traducir archivos
from googletrans import Translator
import os

def translate_file(file_path, source_lang, target_lang):
    translator = Translator()

    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Translate the content
    translated_text = translator.translate(content, src=source_lang, dest=target_lang).text

    # Create a new file path for the translated file
    file_dir, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)
    translated_file_name = f"{file_base}_translated{file_ext}"
    translated_file_path = os.path.join(file_dir, translated_file_name)

    # Write the translated content to a new file
    with open(translated_file_path, 'w', encoding='utf-8') as translated_file:
        translated_file.write(translated_text)

    return translated_file_path

# Example usage
source_language = 'fr'  # French
target_language = 'en'  # English

file_path = r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x01 - The Sopranos.HDTV.fr.txt"
translated_file_path = translate_file(file_path, source_language, target_language)
print(f"Translated file saved at: {translated_file_path}")

#%% traducir archivos 2 
for file_path in file_paths:
    translated_file_path = translate_file(file_path, source_language, target_language)
    print(f"Translated file saved at: {translated_file_path}")


#%% colocar dos columnas

# Define file paths
original_file_path = r"C:\Users\redk8\OneDrive\Documentos\Proyectos Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\The-Last-of-Us_S01E01_French-ELSUBTITLE.COM-ST_69241578.txt"

"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x01 - The Sopranos.HDTV.fr.txt"

translated_file_path = r"C:\Users\redk8\OneDrive\Documentos\Proyectos Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\The-Last-of-Us_S01E01_French-ELSUBTITLE.COM-ST_69241578.fr.es.txt"

    
output_file_path = r"C:\Users\redk8\OneDrive\Documentos\Proyectos Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\combined_output.txt"

# Define column width
column_width = 100

# Read both files and combine them line by line
with open(original_file_path, 'r', encoding='utf-8') as original_file, open(translated_file_path, 'r', encoding='utf-8') as translated_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for original_line, translated_line in zip(original_file, translated_file):
        # Pad the original text with spaces to align the translated text
        padded_original_line = original_line.strip().ljust(column_width)
        combined_line = f'{padded_original_line}{translated_line.strip()}\n'
        output_file.write(combined_line)


# %%
