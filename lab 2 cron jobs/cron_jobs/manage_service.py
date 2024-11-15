import os
import subprocess
import shutil

# Function to restart a service
def restart_service(service_name):
    try:
        # For systemd-based systems 
        subprocess.run(['sudo', 'systemctl', 'stop', service_name], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
        print(f"Service '{service_name}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{service_name}': {e}")

# Function to clear the temp folder
def clear_temp_folder(temp_folder):
    try:
        shutil.rmtree(temp_folder)
        os.makedirs(temp_folder)
        print(f"Temporary folder '{temp_folder}' cleared successfully.")
    except Exception as e:
        print(f"Error clearing temporary folder '{temp_folder}': {e}")

if __name__ == "__main__":
    SERVICE_NAME = "cron"  # Replace with your service name
    TEMP_FOLDER = "/mnt/c/Users/SylvesterKafuiKofiDa/OneDrive - AmaliTech gGmbH/Desktop/AmaliTech/labs/lab 2 cron jobs/cron_jobs/temp_folder"  # Replace with your temp folder path

    restart_service(SERVICE_NAME)
    clear_temp_folder(TEMP_FOLDER)
