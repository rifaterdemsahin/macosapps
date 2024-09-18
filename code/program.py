import os
import subprocess
import json

def get_installed_apps():
    # Run system_profiler to get installed apps
    result = subprocess.run(['system_profiler', 'SPApplicationsDataType', '-json'], capture_output=True, text=True)
    
    # Parse the JSON output
    installed_apps = json.loads(result.stdout)
    
    # Save to a JSON file for reporting
    with open('installed_apps.json', 'w') as f:
        json.dump(installed_apps, f, indent=4)

    return installed_apps

installed_apps = get_installed_apps()
print(f"Found {len(installed_apps['SPApplicationsDataType'])} installed applications.")
