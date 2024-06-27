from flask import Flask, render_template
import pandas as pd
import folium

app = Flask(__name__)

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to render map.html with Folium map
@app.route('/map')
def show_map():
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv('garage_data.csv')

    # Create a Folium map centered around New York
    map_center = [40.7128, -74.0060]  # Coordinates for New York
    folium_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers to the map for each garage location
    for index, row in df.iterrows():
        popup_text = f"{row['House No']}, {row['Street Address']}, {row['City']}"
        folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(folium_map)

    # Save the map to an HTML file
    folium_map.save('templates/map.html')

    # Render map.html with the map
    return render_template('map.html')

@app.route('/dashboard')
def show_dashboard():
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv('garage_data.csv')

    # Render dashboard.html with garage data
    return render_template('dashboard.html', data=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
