from ytmusicapi import YTMusic

# Initialize the YTMusic client
ytmusic = YTMusic('oauth.json')

# Fetch the user's playlists
playlists = ytmusic.get_library_playlists(limit=100)  # Adjust limit as needed

# Display the playlists and ask the user to choose one
print("Your playlists:")
for index, playlist in enumerate(playlists):
    print(f"{index + 1}. {playlist['title']}")

playlist_choice = int(input("Enter the number of the playlist you want to pick: ")) - 1
chosen_playlist = playlists[playlist_choice]
print(chosen_playlist['title'])

# Fetch the details of the chosen playlist
playlist_details = ytmusic.get_playlist(playlistId=chosen_playlist['playlistId'], limit=590)  # Adjust limit as needed

# Sorting function
def sort_tracks(tracks, sort_by='song'):
    if sort_by == 'artist':
        return sorted(tracks, key=lambda x: x['artists'][0]['name'])
    else:  # Default to sorting by song title
        return sorted(tracks, key=lambda x: x['title'])

# Ask the user how they want to sort the tracks
sort_choice = input("Do you want to sort by 'artist' name or 'song' name? ")

# Sort the tracks
sorted_tracks = sort_tracks(playlist_details['tracks'], sort_choice)

# Update the playlist
# Note: This will remove all tracks and re-add them in sorted order, which can be destructive
video_ids = [track['videoId'] for track in sorted_tracks]
ytmusic.remove_playlist_items(chosen_playlist['playlistId'], playlist_details['tracks'])
res = ytmusic.add_playlist_items(chosen_playlist['playlistId'], video_ids, None, True)

print(res['status'])

# Display the sorted tracks
print(f"Updated playlist '{chosen_playlist['title']}' with tracks sorted by {sort_choice}:")
for track in sorted_tracks:
    artist_names = ", ".join([artist['name'] for artist in track['artists']])
    print(f"{track['title']} by {artist_names}")
