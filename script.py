import os
import openai
from tqdm import tqdm
import sys

source_directory = sys.argv[1]
export_directory = sys.argv[2]

if not os.path.exists(export_directory):
   os.makedirs(export_directory)

ALLOWED_EXTENSIONS = ('flac', 'mp3', 'mp4',
                      'mpeg', 'mpga', 'm4a', 'ogg', 'wav', 'webm')

records: list[str] = []

for filename in os.listdir(source_directory):
    f = os.path.join(source_directory, filename)
    if f.endswith(ALLOWED_EXTENSIONS) and os.path.isfile(f):
        records.append(f)

openai.api_key = os.getenv("OPENAI_API_KEY")

for record in tqdm(records):
    audio_file = open(record, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    with open(f"{export_directory}/{record.split('/')[-1]}.txt", 'w', encoding='UTF-8') as export_file:
        export_file.write(transcript.text)
