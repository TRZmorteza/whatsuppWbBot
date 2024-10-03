from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import base64

def paksazi(chat_name):
    # Implement your chat name cleaning logic here
    return chat_name

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_image_from_base64(base64_string, file_path):
    image_data = base64.b64decode(base64_string.split(',')[1])
    with open(file_path, 'wb') as file:
        file.write(image_data)

def get_blob_image_data(driver, blob_url):
    # JavaScript to fetch blob data
    script = """
    var xhr = new XMLHttpRequest();
    xhr.open('GET', arguments[0], true);
    xhr.responseType = 'blob';
    xhr.onload = function() {
        var reader = new FileReader();
        reader.readAsDataURL(xhr.response);
        reader.onload = function() {
            window.blobData = reader.result;
        };
    };
    xhr.send();
    return window.blobData;
    """
    return driver.execute_script(script, blob_url)

def download_images(driver, img_elements, chat_name, base_directory):
    chat_name = paksazi(chat_name)  # Clean chat name

    # Create a folder for images inside the chat directory
    images_folder = os.path.join(base_directory, "Images")  # All images will be saved here
    create_directory(images_folder)

    for index, img in enumerate(img_elements):
        try:
            if img.is_displayed():  # Check if the image is visible
                src = img.get_attribute("src")
                if src.startswith("data:image"):  # Base64 encoded image
                    file_path = os.path.join(images_folder, f"{chat_name}_image_{index}.png")
                    save_image_from_base64(src, file_path)
                    print(f"Saved Base64 image to {file_path}")
                elif src.startswith("blob:"):  # Blob URL detected
                    blob_data = get_blob_image_data(driver, src)
                    if blob_data:
                        file_path = os.path.join(images_folder, f"{chat_name}_image_{index}.png")
                        save_image_from_base64(blob_data, file_path)
                        print(f"Saved Blob image to {file_path}")
                else:
                    print(f"Image URL: {src} (not saved)")

        except Exception as e:
            print(f"An error occurred while capturing image: {e}")

# Example usage
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://example.com")

# Assuming img_elements is a list of image elements
img_elements = driver.find_elements(By.TAG_NAME, 'img')
download_images(driver, img_elements, "ChatName", "/path/to/base/directory")

driver.quit()
"""
Sure! Let’s go through the code step by step and highlight the changes made to handle blob URLs.

Original Code Explanation
The original function download_images is designed to download images from a list of image elements (img_elements) and save them to a specified directory. Here’s a breakdown of the original code:

Function Definition:
download_images(driver, img_elements, chat_name, base_directory): This function takes a Selenium WebDriver instance, a list of image elements, a chat name, and a base directory as input.
Clean Chat Name:
chat_name = paksazi(chat_name): This line cleans the chat name using the paksazi function.
Create Images Folder:
images_folder = os.path.join(base_directory, "Images"): This line creates a path for the images folder inside the base directory.
create_directory(images_folder): This line creates the images folder if it doesn’t already exist.
Iterate Through Image Elements:
The function iterates through each image element in img_elements.
Check If Image Is Visible:
if img.is_displayed(): This line checks if the image is visible.
Get Image Source:
src = img.get_attribute("src"): This line gets the source URL of the image.
Handle Base64 Encoded Images:
if src.startswith("data:image"): This line checks if the image source is a Base64 encoded image.
save_image_from_base64(src, file_path): This line saves the Base64 encoded image to the specified file path.
Handle Blob URLs:
elif src.startswith("blob:"): This line checks if the image source is a blob URL.
blob_data = get_blob_image_data(driver, src): This line gets the blob image data using the get_blob_image_data function.
save_image_from_base64(blob_data, file_path): This line saves the blob image data to the specified file path.
Print Image URL:
print(f"Image URL: {src} (not saved)"): This line prints the image URL if it is not saved.
**Exception Handling
"""