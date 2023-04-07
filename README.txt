
upload audio


pip install -r requirements.tzt


./config.txt

{
}


request

Content-Type: text/plain
body
{
    'audio': base64 wav bin
    'message': speech message
    'uid': uid
}


response

{
    "status": True / False,
    "complete": 0 / 1,
    'speech_wavs': speech_wavs,
    'speech_texts': speech_texts,
}


port
13132


task structure has
+ config file (.txt) include
{
    sample_file (filename)
    message
}
+ sample_file - sample wav


output structure has
+ config file (.txt) include
{
    speech_wavs: list of (filename)
    speech_texts: list of texts
}
+ speech_files - sample wav


run
launch_worker.bat

