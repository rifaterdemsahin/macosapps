from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route('/apps', methods=['GET'])
def get_apps():
    try:
        with open('installed_apps.json') as f:
            apps = json.load(f)
        # Render the table with colored lines and headers
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Installed Apps</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th {
                    background-color: #4CAF50;
                    color: white;
                    padding: 8px;
                }
                td {
                    border: 1px solid #ddd;
                    padding: 8px;
                }
                tr:nth-child(even) {
                    background-color: #f2f2f2;
                }
                tr:hover {
                    background-color: #ddd;
                }
                th, td {
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <h2>Installed Apps</h2>
            <table>
                <thead>
                    <tr>
                        <th>App Name</th>
                        <th>Version</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {% for app in apps %}
                    <tr>
                        <td>{{ app.name }}</td>
                        <td>{{ app.version }}</td>
                        <td>{{ app.description }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
        </html>
        ''', apps=apps)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Error decoding JSON'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5005)
