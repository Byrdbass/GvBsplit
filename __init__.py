from pydub import AudioSegment
import json
# import ffmpeg
# import math

input_file = 'playlist.json'

# fix segment or segment length
def split_audio(file_path, segment_length):
    playlistMix = AudioSegment.from_mp3(file_path)
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    # total_length = 300000 #5min
    print(data)

    previous_endDuration = 0
    for index, song in enumerate(data):
        track = song['track']
        artist = song['artist']
        title = song['title']

        # parse the data into seconds
        time_string = song['time']
        time_parts = list(map(int, time_string.split(':')))
        print(f"Time parts {time_parts}")

        # Check if the time includes hours
        if len(time_parts) == 3:
            hours, minutes, seconds = time_parts
            endDuration = hours * 3600 + minutes * 60 + seconds
        else:  # Assume it's MM:SS
            minutes, seconds = time_parts
            endDuration = minutes * 60 + seconds

        start_time = previous_endDuration #- end duration of previous song
        end_time = endDuration

        previous_endDuration = endDuration

        segment = playlistMix[start_time:end_time]
        
        output_file = f"{title} by {artist} from {file_path[:-4]} #{track}.mp3"
        segment.export(output_file, format="mp3")
        print(f"Song {title} was {time_string} or {endDuration} seconds long")
        print(f"Exported: {output_file}")

file_mp3 = r"/Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/GvsB Dec 2013.mp3"
split_audio(file_mp3)