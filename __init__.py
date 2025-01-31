from pydub import AudioSegment
import json
import os
import math
from pathlib import Path
# import ffmpeg
# import math

input_file = 'playlist.json'

# fix segment or segment length
def split_audio(file_path):
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
        
    export_folder = f"/Users/ByrdBass/Desktop/Musick/Music/GvsB-Tracks/{album}" 

    for i, song in enumerate(data):
        track = song['track']
        artist = song['artist']
        title = song['title']

        time_string_start = song['time']
        time_parts_start = list(map(int, time_string_start.split(':')))
        time_string_end = data[i + 1]['time'] if i +1 < len(data) else None
        if time_string_end != None:
            time_parts_end = list(map(int, time_string_end.split(':')))
            if len(time_parts_end) == 3:
                hours, minutes, seconds = time_parts_start
                end_time = (hours * 3600 + minutes * 60 + seconds) * 1000
            else: 
                minutes, seconds = time_parts_end
                end_time = (minutes * 60 + seconds) * 1000
        else:
            end_time = playlistMix_duration


        if len(time_parts_start) == 3:
            hours, minutes, seconds = time_parts_start
            start_time = (hours * 3600 + minutes * 60 + seconds) * 1000
        else:  
            minutes, seconds = time_parts_start
            start_time = (minutes * 60 + seconds) * 1000

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
                             'duration': duration,
                             'year': year})
        print(f"Song {title} was {time_string_start} and ended at {format((end_time/1000)/60, '.2f')} minutes at index {i}")
        print(f"Exported: {output_file}")

file_mp3 = r"/Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/GvsB Dec 2013.mp3"
split_audio(file_mp3)