import os
import requests

def download_file(url, directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Define the full path for the file
    file_name = os.path.join(directory, 'spidetect.py')
    
    # Send a GET request to download the file
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to {file_name}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/cyberyom/SPIDEVexamples/main/spidetect.py"
    directory = "/mnt/data/"  # Replace with your directory path
    download_file(url, directory)
