import subprocess

root_dir = '/Users/ByrdBass/Desktop/Musick/Music/various/'
month_dir = 'august 2011/'
file_mp3 = f'{root_dir}{month_dir}august 2011.mp3'
cover_art = f'{root_dir}{month_dir}GVSB-AUGUST-20111.jpg'

create_dicts = subprocess.Popen(["python", "create_dicts.py"])
create_dicts.wait()

create_tracks = subprocess.Popen(["python", "create_tracks.py", file_mp3, cover_art])
create_tracks.wait()

copy_playlist = subprocess.Popen(['python', 'copy_playlist.py'])
copy_playlist.wait()