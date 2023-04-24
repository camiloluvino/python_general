# %%
import os
import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

def read_file_to_sentences(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    return sent_tokenize(text)

# Define file paths
original_file_path = r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x02 - 46 Long.HDTV.fr.srt"
translated_file_path = r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\los sopranos\The Sopranos - 1x02 - 46 Long.HDTV.fr.en.srt"

# Get file encodings
original_file_encoding = get_file_encoding(original_file_path)
translated_file_encoding = get_file_encoding(translated_file_path)

# Read files and split into sentences
original_sentences = read_file_to_sentences(original_file_path, original_file_encoding)
translated_sentences = read_file_to_sentences(translated_file_path, translated_file_encoding)

# Define column width
column_width = 100

# Create the output file path
output_file_name = os.path.splitext(os.path.basename(original_file_path))[0] + " - combinado" + ".srt"
output_file_path = os.path.join(os.path.dirname(original_file_path), output_file_name)

# Combine sentences line by line
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for original_sentence, translated_sentence in zip(original_sentences, translated_sentences):
        # Pad the original text with spaces to align the translated text
        padded_original_sentence = original_sentence.strip().ljust(column_width)
        combined_line = f'{padded_original_sentence}{translated_sentence.strip()}\n'
        output_file.write(combined_line)

# %%
