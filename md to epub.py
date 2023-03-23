#%%
import pypub
from pathlib import Path

# Define paths to the markdown files
md_files = [
    "C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/mdToEpub/@horkheimerTeoriaTradicionalTeoria1998_1.md",
    "C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/mdToEpub/@horkheimerTeoriaTradicionalTeoria1998_2.md",
    "C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/mdToEpub/@horkheimerTeoriaTradicionalTeoria1998_3.md",
    "C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/mdToEpub/@horkheimerTeoriaTradicionalTeoria1998_4.md",
    "C:/Users/redk8/Documents/Proyectos en Python/python_general/fuentes de datos/mdToEpub/@horkheimerTeoriaTradicionalTeoria1998_5.md"
]

# Initialize a new EPUB file
book = pypub.Epub(title="My EPUB book", creator="Me")

# Add each markdown file to the book
for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
        # Remove the file extension from the filename to use as the chapter title
        title = Path(md_file).stem
        chapter = pypub.create_chapter_from_string(title, content)
        book.add_chapter(chapter)

# Generate the EPUB file
book.create_epub("my_book.epub", cover=None)
