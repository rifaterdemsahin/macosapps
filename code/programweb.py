from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/apps', methods=['GET'])
def get_apps():
    try:
        with open('installed_apps.json') as f:
            apps = json.load(f)
        return jsonify(apps)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Error decoding JSON'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5005)
