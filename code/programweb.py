from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/apps', methods=['GET'])
def get_apps():
    with open('installed_apps.json') as f:
        apps = json.load(f)
    return jsonify(apps)

if __name__ == '__main__':
    app.run(port=5000)
