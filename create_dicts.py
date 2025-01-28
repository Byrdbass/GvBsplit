import json

def parse_file_to_dicts(file_path):
    """Parses a text file into an array of dictionaries with track, artist, title, and time."""
    result = []

    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if line.strip():
                # Split the line into segments
                try:
                    # Separate the track number and artist
                    track_and_artist, rest = line.split("::", 1)
                    track, artist = track_and_artist.strip().split(" ", 1)
                    
                    # Separate the title and time
                    title, time = rest.rsplit(" ", 1)

                    # Add to the result as a dictionary
                    result.append({
                        "track": track.strip(),
                        "artist": artist.strip(),
                        "title": title.strip(),
                        "time": time.strip()
                    })
                except ValueError:
                    print(f"Skipping malformed line: {line.strip()}")

    return result

array_of_dicts = parse_file_to_dicts('playlist.txt')
with open('playlist.json', 'w') as json_file:
    json.dump(array_of_dicts, json_file, indent=4)
print(array_of_dicts)
