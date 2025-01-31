import subprocess

file_mp3 = '/Users/ByrdBass/Desktop/Musick/Music/various/BestOf 2015/GORILLA vs BEAR x 2015.mp3'

create_dicts = subprocess.Popen(["python", "create_dicts.py"])
create_dicts.wait()

create_tracks = subprocess.Popen(["python", "create_tracks.py", file_mp3])
create_tracks.wait()