This script pulls all audio files for a specific question in a specific KoboToolbox project, checks the length of each file, and stores the result in a CSV file. 


1. Download or clone the Python file on your computer
1. Download the data from the KoboToolbox project as a CSV in the same directory using XML/names.
   Only include the most important columns to make it easy to read, but it must include the audio question (with the URL checkbox ticked in export settings)
   since that will be used to pull the actual audio files. The uuid column is always included by default. 
1. Set the API key for your account that contains the project
1. Set the CSV file name 
1. Set the name of the audio file URL column (e.g. "experience_joint_decision_URL")
1. Run the Python script with `python get_audio_length.py` or `python3 get_audio_length.py`, depending on your setup.
1. It will iterate over all audio files, downloading them and writing the length to the CSV file (as well as download status for each one). This may take a while depending on the number of files.
   If you don't see an error this means it's working. You will also see the CSV updating as long as the script keeps running. 
