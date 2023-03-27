#%%
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.wav")
# %%
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
# %%
import whisper
print(whisper.__file__)