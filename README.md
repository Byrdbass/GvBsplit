# GvBsplit
a script used to split long DJ mixes into individual songs

## Resources
- [venv setup](https://stackoverflow.com/questions/43069780/how-to-create-virtual-env-with-python-3)
- [pydub](https://github.com/jiaaro/pydub)
- include ffmpeg and simpleaudio from above #installation
- [make directory issue](https://stackoverflow.com/questions/61286301/pydub-cant-save-file-in-a-different-directory-properly)
- [running scripts concurrently](https://stackoverflow.com/questions/53865580/run-multiple-python-file-concurrently)

## Steps to seperate Tracks

1. WEB BROWSER - Go to mix on [GorillaVsBear.net](https://www.gorillavsbear.net/)
    - search for relevant mix
    - copy the playlist and paste correctly in `playlist.txt`
    - download the image for the mix, and save to correct folder at the `root-dir`
2. CANVA
    - convert the image from webp to jpg and name and save in correct foler where `root-dir` is
3. FINDER - right click folder of tracks in finder for location at `root-dir`
    - open "New Terminal at Folder"
4. TERMINAL
    - type in `pwd` and copy output
    - paste as value for `month_dir`
    - type in `ls`
    - copy and paste values for `file_mp3` and `cover_art`
        - make sure to copy the jpg and not webp

5. IN `.VENV`
    - type `python3 __init__.py`
    - check format of month dir if not in `{MONTH} {YEAR}`
        - if format is not correct script will error out "too many values to unpack"

## How script runs

1. In `create_dicts.py` 
    - playlist.txt => playlist.json 
2. In `create_tracks.py` (assuming month_dir path is correct & image is jpg)

        - NOTE: if `month_dir` is not `{MONTH} {YEAR}` => please full .mp3 and images into NEW FOLDER so serato doesn't loose access to metadata where full track originally was saved

    - playlist.json turns into tracks, cover art gets assigned
    - check `export_folder` on line 44 in `create_tracks.py` for output
3. playlist get's copied with correct name in processed_playlists folder
