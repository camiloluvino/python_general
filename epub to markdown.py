#%%
import ebooklib
from ebooklib import epub
import os

# open the epub file
book = epub.read_epub('C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/epub to markdown/Una invitacion a la sociologia - Loic Wacquant.epub')

# create the output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# loop through each item in the epub file
for item in book.get_items():

    # check if the item is an xhtml file
    if item.is_document():

        # read in the content of the xhtml file
        content = item.get_content()

        # create a markdown file with the same name as the xhtml file
        filename = os.path.splitext(os.path.basename(item.file_name))[0]
        with open(f'output/{filename}.md', 'w', encoding="utf-8") as f:

            # write the markdown content to the file
            f.write(content)








# %%
