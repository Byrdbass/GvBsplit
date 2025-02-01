import os
import shutil
import json

new_file = 'recent_album.json'

if not os.path.exists(new_file):
    print('ERROR: album.json not found')
    exit(1)

with open(new_file, 'r') as f:
    album_data = json.load(f)

album = album_data.get('album', "unknown")

source_file = 'playlist.txt'
save_path = 'processed_playlists'
new_playlist = f'{album}.txt'

os.makedirs(save_path, exist_ok=True)
destination_path = os.path.join(save_path, new_playlist)
shutil.copy(source_file, destination_path)
print(f'copied playlist.txt to {album}.txt')