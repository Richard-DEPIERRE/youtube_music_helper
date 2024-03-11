from ytmusicapi import YTMusic

# Initialize the YTMusic client
ytmusic = YTMusic('oauth.json')

# Function to get and display playlists for selection
def get_and_choose_playlist(prompt):
    playlists = ytmusic.get_library_playlists(limit=100)  # Adjust limit as needed
    print(prompt)
    for index, playlist in enumerate(playlists):
        print(f"{index + 1}. {playlist['title']}")

    choice = int(input("Enter the number of the playlist: ")) - 1
    return playlists[choice]['playlistId'], playlists[choice]['title']

# Function to copy all songs from one playlist to another
def copy_playlist_songs(source_playlist_id, destination_playlist_id):
    # Fetch the tracks from the source playlist
    source_playlist_tracks = ytmusic.get_playlist(playlistId=source_playlist_id, limit=600)['tracks']  # Adjust limit as needed
    source_track_ids = [track['videoId'] for track in source_playlist_tracks if 'videoId' in track]

    # Add these tracks to the destination playlist
    if source_track_ids:
        ytmusic.add_playlist_items(destination_playlist_id, source_track_ids)
        print(f"Added {len(source_track_ids)} tracks from playlist {source_playlist_id} to {destination_playlist_id}")
    else:
        print("No tracks found in the source playlist.")

# Main script
print("Select the source playlist:")
source_playlist_id, source_playlist_title = get_and_choose_playlist("Your playlists:")
print(f"Selected source playlist: {source_playlist_title}")

print("\nSelect the destination playlist:")
destination_playlist_id, destination_playlist_title = get_and_choose_playlist("Your playlists:")
print(f"Selected destination playlist: {destination_playlist_title}")

copy_playlist_songs(source_playlist_id, destination_playlist_id)
