import pandas as pd
import requests
from pydub import AudioSegment
import os
import csv

# Kobo API key
api_key = 'abcd1234abcd1234abcd1234abcd1234abcd1234'

# Source CSV and column name of the audio URL question
input_csv = 'input_file_name.csv'
audio_question_url = 'audio_question_URL'

# Function to download the audio file
def download_file(url, filename):
    headers = {'Authorization': 'Token ' + api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return "Downloaded"
    else:
        return f"Failed to download (Status code: {response.status_code})"

# Get the length of the audio file
def get_audio_length(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000  # Length in seconds
    except:
        return "Failed to process audio file"

# Main process
def process_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv, delimiter=';')
    df['audio_length_seconds'] = None
    df['download_status'] = None

    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write header
        writer.writerow(list(df.columns))

        for index, row in df.iterrows():
            url = row[audio_question_url]
            length = None
            download_status = "No URL provided"
            
            if pd.notna(url):
                filename = url.split('/')[-1]
                download_status = download_file(url, filename)

                if download_status == "Downloaded":
                    length = get_audio_length(filename)
                    os.remove(filename)  # Remove the file after processing
                else:
                    length = "N/A"

            # Update the DataFrame and write to CSV
            df.at[index, 'audio_length_seconds'] = length
            df.at[index, 'download_status'] = download_status
            writer.writerow(df.iloc[index])

# Replace 'input.csv' and 'output.csv' with your file names
process_csv(input_csv, 'output.csv')




