# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 10

# Image Downloader from URL
import requests
import os

def download_image(url, folder="images"):
    """
    Downloads an image from a URL and saves it to a folder.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Get the filename from the URL
        filename = os.path.join(folder, url.split("/")[-1])

        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Image downloaded successfully to {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None

# Example usage with a placeholder image URL
image_url = "https://via.placeholder.com/150"
download_image(image_url)

# Output:
# Image downloaded successfully to images/150 