from flask import Flask, render_template, jsonify
import json
import os

# Create the Flask application object
app = Flask(__name__)  # This must come BEFORE any route definitions

@app.route('/apps', methods=['GET'])  # Note the '@' sign
def get_apps():
    try:
        # Build the path to the JSON file, relative to this script's location
        json_path = os.path.join(os.path.dirname(__file__), 'installed_apps.json')
        
        # Open and load the JSON file
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Extract the list of apps under "SPApplicationsDataType"
        apps = data.get("SPApplicationsDataType", [])
        
        # Check if the list is empty and handle it
        if not apps:
            return jsonify({'error': 'No apps found in JSON'}), 404
        
        # Pass the apps to the template for rendering
        return render_template('apps.html', apps=apps)
    
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    
    except json.JSONDecodeError:
        return jsonify({'error': 'Error decoding JSON'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5005, debug=True)
