# Concatenate the tracks, show only columns names that are in all tables
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master,
                               tracks_ride,
                               tracks_st],
                               sort=True, join='inner')
print(tracks_from_albums)