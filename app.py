import os
from flask import Flask, jsonify, render_template, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='/static')

MUSIC_BASE_DIR = 'static' # This is where our song folders are

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/api/songs')
def list_songs():
    """
    Create an API endpoint to list the available songs,
    including their display name, MP3 path, and cover art path.
    """
    songs_data = []
    for song_folder in os.listdir(MUSIC_BASE_DIR):
        song_folder_path = os.path.join(MUSIC_BASE_DIR, song_folder)
        if os.path.isdir(song_folder_path): # Ensure it's a directory
            mp3_file = None
            cover_file = None

            for file in os.listdir(song_folder_path):
                if file.endswith('.mp3'):
                    mp3_file = file
                elif file.startswith('cover.') and (file.endswith('.jpg') or file.endswith('.png')):
                    cover_file = file

            if mp3_file and cover_file:
                songs_data.append({
                    'display_name': song_folder, # The folder name is now the display name
                    'mp3_path': f'/static/{song_folder}/{mp3_file}',
                    'cover_path': f'/static/{song_folder}/{cover_file}'
                })
    return jsonify(songs_data)

# This route allows access to any static file within the static folder
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)