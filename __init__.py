from pydub import AudioSegment
# import ffmpeg
# import math


def split_audio(file_path, segment_length):
    song = AudioSegment.from_mp3(file_path)
    # total_length = 300000 #5min
    num_segments = 1
    for i in range(num_segments):
        start_time = i * segment_length
        end_time = 300000
        segment = song[start_time:end_time]
        
        output_file = f"{file_path[:-4]}_part{i+1}.mp3"
        segment.export(output_file, format="mp3")
        print(f"Exported: {output_file}")

split_audio(r"/Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/GvsB Dec 2013.mp3", 300000)