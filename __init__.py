import subprocess

file_mp3 = '/Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/GvsB Dec 2013.mp3'
cover_art = '/Users/ByrdBass/Desktop/Musick/Music/various/DECEMBER 2013/gvsb_december2013-575x575.jpg'

create_dicts = subprocess.Popen(["python", "create_dicts.py"])
create_dicts.wait()

create_tracks = subprocess.Popen(["python", "create_tracks.py", file_mp3, cover_art])
create_tracks.wait()