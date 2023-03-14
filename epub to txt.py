#%% importar librerías y libro
import ebooklib
from ebooklib import epub
book = epub.read_epub(r"C:\Users\redk8\Documents\Proyectos en Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\Una invitacion a la sociologia - Loic Wacquant.epub")

#%% identificar ítems
item_document = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

# %% VERSIÓN CHAT GPT
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

# Load the EPUB file
book = epub.read_epub(r"C:\Users\redk8\Documents\Proyectos en Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\Una invitacion a la sociologia - Loic Wacquant.epub")

# Get a list of all the document items in the book
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

# Create a directory to store the text files
if not os.path.exists('chapters'):
    os.makedirs('chapters')

# Loop over the document items and extract the chapter text
for item in items:
    # Check if the item is a chapter
    if 'chapter' in item.get_name().lower():
        # Use BeautifulSoup to extract the chapter text
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        text = [para.get_text() for para in soup.find_all('p')]
        chapter_text = ' '.join(text)
        # Save the chapter text to a file
        filename = os.path.join('chapters', item.get_name() + '.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chapter_text)


# %%
