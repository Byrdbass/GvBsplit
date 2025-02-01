import sys
from pydub import AudioSegment
import json
import os
import math
from pathlib import Path

if len(sys.argv) < 2:
    print("Error: missing file_mp3 name in main script")
    sys.exit(1)

file_mp3 = sys.argv[1]
cover_art = sys.argv[2]
input_file = 'playlist.json'

if not os.path.isfile(file_mp3):
    print(f"THE PROVIDED FILE IS NOT AN MP3 FILE")
    sys.exit(1)

if not os.path.isfile(cover_art):
    print("THE PROVIDED COVER ART IS NOT A JPG")
    sys.exit(1)

# fix segment or segment length
def split_audio(file_path, cover_art):
    playlistMix = AudioSegment.from_mp3(file_path)
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    playlistMix_duration = len(playlistMix) - 1000

    #for file paths that llok like /Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/GvsB Dec 2013.mp3
    file_parts = file_path.split('/various/')
    mix_month_year = file_parts[1].split('/')[0] if len(file_parts) > 1 else "Album_Not_Extracted"
    album_parts = mix_month_year.split()
    if len(album_parts):
        month, year = album_parts
        formatted_month = month.capitalize()[:3]
        album = f"{formatted_month} {year}"
        
    album_file = 'recent_album.json'
    with open(album_file, 'w') as f:
        json.dump({'album': album}, f)
    export_folder = f"/Users/ByrdBass/Desktop/Musick/Music/GvsB-Tracks/{album}" 

    for i, song in enumerate(data):
        track = song['track']
        artist = song['artist']
        title = song['title']

        time_string_start = song['time']
        time_parts_start = list(map(int, time_string_start.split(':')))
        time_string_end = data[i + 1]['time'] if i +1 < len(data) else None
        print(f"Start at {time_string_start} end at {time_string_end}" )
        if time_string_end != None:
            time_parts_end = list(map(int, time_string_end.split(':')))
            if len(time_parts_end) == 3:
                hours, minutes, seconds = time_parts_end
                end_time = (hours * 3600 + minutes * 60 + seconds) * 1000
            else: 
                minutes, seconds = time_parts_end
                end_time = (minutes * 60 + seconds) * 1000
        else:
            end_time = playlistMix_duration


        if len(time_parts_start) == 3:
            hours, minutes, seconds = time_parts_start
            start_time = (hours * 3600 + minutes * 60 + seconds) * 1000
        elif len(time_parts_start) == 2:  
            minutes, seconds = time_parts_start
            start_time = (minutes * 60 + seconds) * 1000
        else:
            raise ValueError(f"Unexpected time format: {time_string_start}")

        duration = end_time - start_time

        segment = playlistMix[start_time:end_time] #slicing specific to pydub library
        output_file = f"{title} by {artist} from {album} #{track}.mp3"
        Path(export_folder).mkdir(parents=True, exist_ok=True)
        output_path = os.path.join(export_folder, output_file)
        segment.export(output_path, 
                       format="mp3", 
                       bitrate='320k',
                       tags={'title': title, 
                             'artist': artist, 
                             'album': album, 
                             'duration': duration},
                        cover=cover_art
                        )
        print(f"Song {title} was {time_string_start} and ended at {format((end_time/1000)/60, '.2f')} minutes at index {i}")
        print(f"Exported: {output_file}")

split_audio(file_mp3, cover_art)