#%%
import whisper
model = whisper.load_model("base")

#%%
# path to download the dataset
#https://www.kaggle.com/datasets/pavanelisetty/sample-audio-files-for-speech-recognition

result = model.transcribe("/content/harvard.wav")
result["text"]


#%% TEXTO DE JULIA
import whisper

model = whisper.load_model("base")

# New file path
file_path = "C:\\Users\\redk8\\Downloads\\msg609515370-7148.ogg"

result = model.transcribe(file_path)
text = result["text"]

# Save the transcribed text to a file named "audio Julia.txt"
with open("audio Julia.txt", "w") as output_file:
    output_file.write(text)

# %%
