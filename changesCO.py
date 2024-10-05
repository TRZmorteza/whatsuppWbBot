from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import os
import time
import json
import re
import requests

def paksazi(name):
    """Sanitize filename to avoid invalid characters and limit to 5 characters."""
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def save_cookies(driver, filename='cookies.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(driver.get_cookies(), file)
        print(f"Cookies saved to {filename}.")
    except Exception as e:
        print(f"Error saving cookies: {e}")
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def searchIMG(driver):
    try:
        img_elements = driver.find_elements(By.XPATH, "//div[@role='application']//img")
        valid_img_elements = []

        for img in img_elements:
            # Check if the image is in the header (or any specific area you want to ignore)
            if "header" in img.get_attribute("class"):
                print("Ignoring image found in header.")
                continue  # Skip images in the header

            valid_img_elements.append(img)

        if valid_img_elements:
          
            print("Images are present in this chat (excluding header images).")
            return valid_img_elements  
        else:
            print("No valid images found in this chat.")
            return None

    except Exception as e:
        print(f"An error occurred while checking for images: {e}")
        return None
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def find_and_click_buttons(driver):
    try:
        buttons = driver.find_elements(By.XPATH, "//button[.//span[@data-icon='media-download']]")
        
        if buttons:
            print(f"Found {len(buttons)} buttons with media download icon:")
            for button in buttons:
                print("Button found :-)")
                button.click()
                time.sleep(1)  
        else:
            print("No buttons found with media download icon.")
    except Exception as e:
        print(f"An error occurred while finding or clicking buttons: {e}")
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def create_directory(path):
    """Create a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def create_chat_directory(base_directory, chat_name):
    """Create a directory for the clicked chat under the base directory only if it doesn't already exist."""
    chat_directory = os.path.join(base_directory, paksazi(chat_name))
    
    # Check if the directory already exists
    if not os.path.exists(chat_directory):
        create_directory(chat_directory)
        print(f"Chat directory created: {chat_directory}")
    else:
        print(f"Chat directory already exists: {chat_directory}")
    
    return chat_directory  # Return the path for further use
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def save_image_from_base64(base64_str, file_path):
    """Save an image from a base64 string."""
    # Remove the header if present
    if base64_str.startswith('data:image/png;base64,'):
        base64_str = base64_str.replace('data:image/png;base64,', '')
    elif base64_str.startswith('data:image/jpeg;base64,'):
        base64_str = base64_str.replace('data:image/jpeg;base64,', '')

    # Decode and write to file
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(base64_str))
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def get_blob_image_data(driver, blob_url):
    """Retrieve image data from a blob URL."""
    # Use JavaScript to convert blob URL to base64
    script = f"""
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '{blob_url}', true);
    xhr.responseType = 'blob';
    xhr.onload = function() {{
        var reader = new FileReader();
        reader.onloadend = function() {{
            return reader.result;  // This will be a base64 string
        }};
        reader.readAsDataURL(xhr.response);
    }};
    xhr.send();
    """
    
    # Execute script and get result
    result = driver.execute_script(script)
    
    # Wait for result (you may need to implement a better waiting mechanism)
    time.sleep(2)  # Adjust this based on your needs
    
    return result
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
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

def get_blob_image_data(driver, blob_url):
    script = """
    return new Promise((resolve, reject) => {
        fetch(arguments[0])
            .then(response => response.blob())
            .then(blob => {
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.onerror = reject;
                reader.readAsDataURL(blob);
            })
            .catch(reject);
    });
    """#mok kerden respons 
    return driver.execute_script(script, blob_url)
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def save_text_messages(driver, chat_name, base_directory):
    chat_name = paksazi(chat_name)  # Clean chat name

    # Create a folder for text messages inside the chat directory
    messages_folder = os.path.join(base_directory, "Messages")  # All messages will be saved here
    create_directory(messages_folder)

    try:
        message_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'message')]//span[@dir='auto']")
        
        text_content = []
        
        for message in message_elements:
            text_content.append(message.text)

        text_file_path = os.path.join(messages_folder, f"{chat_name}_messages.txt")
        
        # Check if the text file already exists to avoid overwriting
        if os.path.exists(text_file_path):
            print(f"Text file already exists: {text_file_path}. Skipping saving messages.")
            return

        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            for line in text_content:
                text_file.write(line + '\n')

        print(f"Text messages saved to: {text_file_path}")
    
    except Exception as e:
        print(f"An error occurred while saving text messages: {e}")
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def chayI(chat_name):
    chay=''
    for i in chat_name:
                if i!='\\':
                    print(i,end='')
                    chay+=i
                else:
                 print()
                 return chay
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def session():
    driver = webdriver.Chrome()
    
    driver.get("https://web.whatsapp.com")
    
    input("Scan the QR code and press Enter after logging in on your phone...")
    
    save_cookies(driver)  
    
    # Set main directory path at C:\xampp\webdav
    main_directory_path = r'C:\xampp\webdav'
    
    while True:
        chat_elements = driver.find_elements(By.XPATH, "//div[contains(@role,'listitem')]")
        
        for chat in chat_elements:
            chat_name = (chat.text.replace('/', '_')).replace('\n','\\')  # Clean chat name
            print("Chat found:", chat_name)
            chay=chayI(chat_name)
            
            print(chay,'after for')
            try:
                chat.click()
                time.sleep(2)  
                
                find_and_click_buttons(driver)
                time.sleep(2)  
                
                img_elements = searchIMG(driver)
                
                # Create a directory for this specific chat within the main directory
                chat_directory = create_chat_directory(main_directory_path, chay)

                if img_elements and main_directory_path:  # Ensure main directory path is valid
                    download_images(driver, img_elements, chay, chat_directory)  
                    save_text_messages(driver, chay, chat_directory)  
                
                else:
                    save_text_messages(driver, chat_name, chat_directory)  

            except Exception as e:
                print(f"An error occurred while processing chat '{chay}': {e}")

        time.sleep(100)  # Wait 5 minutes before next iteration
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == "__main__":
    session()