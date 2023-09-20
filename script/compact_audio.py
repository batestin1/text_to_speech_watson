from pydub import AudioSegment
import os
import json

combined_audio = AudioSegment.empty()

path_in = r"audio"
path_out = r"audiofinal"
path_in = r'books'
path_out = r"audio"

if not os.path.exists(path_in):
    os.makedirs(path_in)
if not os.path.exists(path_out):
    os.makedirs(path_out)

for file_name in os.listdir(path_in):
    if file_name.endswith(".wav"):
        path_file_out = os.path.join(path_in, file_name)
        audio_part = AudioSegment.from_wav(path_file_out)
        combined_audio += audio_part


# Salve o áudio combinado como "audiobook_Ciga.wav"
audiobook_filename = "audiobook_Ciga.wav"
combined_audio.export(os.path.join(path_out, audiobook_filename), format="wav")
