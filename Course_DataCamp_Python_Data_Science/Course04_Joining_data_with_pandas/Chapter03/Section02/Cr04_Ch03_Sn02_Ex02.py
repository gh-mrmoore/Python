# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master,
                               tracks_ride,
                               tracks_st],
                               sort=True, ignore_index=True)
print(tracks_from_albums)