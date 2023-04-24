#%% ALTERNATIVA DE CHATGPT
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

# alternativa 2 

for file_path in file_paths:
    translated_file_path = translate_file(file_path, source_language, target_language)
    print(f"Translated file saved at: {translated_file_path}")



# %% ALTERNATIVA DE BARD (ME DA EL PROBLEMA DEL ERROR DE 500 CA)
import io

with io.open(r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x01 - The Sopranos.HDTV.fr - corta.txt", "r", encoding="latin-1") as f:
    contents = f.read()

from translate import Translator

translator = Translator(to_lang="es")
translation = translator.translate(contents)

with open(r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x01 - The Sopranos.HDTV.es.txt", "w") as f:
    f.write(translation)
