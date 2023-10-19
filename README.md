# An Example of Using OpenAI Whisper Transcription API
Batch transcribes audio files in the specified folder. 

## Prerequisites
- Python 3
- OpenAI API key of an active account.

## Setup
For MacOS or Linux:
```bash
# setup python environment
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# set api key as environment variable
echo "export OPENAI_API_KEY=<your-openai-api-key>" \
 >> ~/.zshrc # use ~/.bashrc if bash
source ~/.zshrc
```

## Usage
The folder containing the audio files is the 'source folder', the folder that will store the transcription results as txt files is the 'export folder'.
```bash
python script.py <source-folder-path> <export-folder-path>
```
Example:
```bash
python script.py ~/Downloads/records/ transcripts/
```

## Support
Available audio file types:
- flac
- mp3
- mp4
- mpeg
- mpga
- m4a
- ogg
- wav
- webm