# Extract relevant columns and prepare the data for deck.gl
deck_gl_data = metro_trips_data[['start_lat', 'start_lon', 'end_lat', 'end_lon']].copy()

# Rename columns for clarity in deck.gl
deck_gl_data.rename(columns={
    'start_lat': 'sourceLat',
    'start_lon': 'sourceLon',
    'end_lat': 'targetLat',
    'end_lon': 'targetLon'
}, inplace=True)

# Convert the data to a JSON-like structure suitable for deck.gl
deck_gl_formatted_data = deck_gl_data.to_dict(orient='records')

# Save the formatted data to a JSON file for easy use in the deck.gl visualization
output_file_path = '/mnt/data/bike_rides_deckgl.json'
deck_gl_data.to_json(output_file_path, orient='records', lines=False)

output_file_path
