#%%
import ebooklib
from ebooklib import epub
book = epub.read_epub(r"C:\Users\redk8\Documents\Proyectos en Python\python_general\fuentes de datos\epubPdf_toMarkdownTxt\Una invitacion a la sociologia - Loic Wacquant.epub")
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

#%%
