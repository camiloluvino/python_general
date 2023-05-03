#%%
import os
import re
import chardet

def get_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def read_file_to_subtitle_entries(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    subtitle_entries = re.split(r'\n\s*\n', text.strip())
    return subtitle_entries

# Define file paths
original_file_path = r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\westworld\Westworld.S01E05.720p.BluRay.x264-DEMAND.Fr.en.srt"
translated_file_path = r"C:\Users\redk8\Dropbox\Graph_idiomas\francés\subtítulos\westworld\Westworld.S01E05.720p.BluRay.x264-DEMAND.Fr.srt"

# Get file encodings
original_file_encoding = get_file_encoding(original_file_path)
translated_file_encoding = get_file_encoding(translated_file_path)

# Read files and split into subtitle entries
original_entries = read_file_to_subtitle_entries(original_file_path, original_file_encoding)
translated_entries = read_file_to_subtitle_entries(translated_file_path, translated_file_encoding)

# Create the output file path
output_file_name = os.path.splitext(os.path.basename(original_file_path))[0] + " - combinado" + ".srt"
output_file_path = os.path.join(os.path.dirname(original_file_path), output_file_name)

# Combine subtitle entries line by line
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for original_entry, translated_entry in zip(original_entries, translated_entries):
        # Extract subtitle texts
        original_text = re.sub(r'\d+\n\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n', '', original_entry).strip()
        translated_text = re.sub(r'\d+\n\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n', '', translated_entry).strip()
        
        # Extract index number
        index_number = re.search(r'\d+', original_entry).group()
        
        # Combine texts
        combined_entry = f'{index_number}\n{original_text}\n{translated_text}\n\n'
        output_file.write(combined_entry)

# %%
