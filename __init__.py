import subprocess
import sys

root_dir = '/Users/ByrdBass/Desktop/Musick/Music/various/'
#FORMAT SHOULD BE "MONTH YEAR"
month_dir = 'JULY 2014/' #make sure this ends in a slash
file_mp3 = f'{root_dir}{month_dir}GORILLA VS BEAR JULY 2014.mp3'
cover_art = f'{root_dir}{month_dir}gvsb_july2014_b-575x575.jpg'

try:
    # Run first two sequentially - will raise exception if either fails
    subprocess.run(["python", "create_dicts.py"], check=True)
    subprocess.run(["python", "create_tracks.py", file_mp3, cover_art], check=True)
    
    # Only run third if both succeeded
    subprocess.run(['python', 'copy_playlist.py'])
    
except subprocess.CalledProcessError as e:
    print(f"SCRIPT FAILED!!! => {e}")
    sys.exit(1)