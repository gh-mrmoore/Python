# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

#print(metallica_tracks)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, how='inner', on='tid')

#print(tracks_invoices)

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity': 'sum'})

#print(tracks_sold)

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(by=['quantity'], ascending=False))