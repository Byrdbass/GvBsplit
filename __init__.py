import subprocess

create_dicts = subprocess.Popen(["python", "create_dicts.py"])
create_tracks = subprocess.Popen(["python", "create_tracks.py"])

create_dicts.wait()
create_tracks.wait()