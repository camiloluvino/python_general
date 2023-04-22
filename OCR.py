import pytesseract

# Establece la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\redk8\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# El resto de tu código
import pytesseract
from PIL import Image
import pdf2image
import os

# If needed, set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

pdf_path = r"C:\Users\redk8\OneDrive\Documentos\Proyectos Python\python_general\fuentes de datos\OCR\garreton-la-sociedad-en-que-viviremos.pdf"
output_text_file = r"output_text.txt"

def pdf_to_images(pdf_path):
    return pdf2image.convert_from_path(pdf_path)

def images_to_text(images):
    text = ""
    for i, img in enumerate(images):
        img_text = pytesseract.image_to_string(img)
        text += f"--- Page {i + 1} ---\n{img_text}\n"
    return text

def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

if __name__ == "__main__":
    images = pdf_to_images(pdf_path)
    text = images_to_text(images)
    save_text_to_file(text, output_text_file)
    print("OCR completed. Text saved to", output_text_file)


