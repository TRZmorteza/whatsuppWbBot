import shutil
import os
from datetime import datetime
import http.client
import requests
import json
import re
import cv2
import traceback
from ultralytics import YOLO
model=YOLO('best.pt')
img_end=['.jpg', '.jpeg']

base_xamp_dir = r'C:\\xampp\\htdocs\\whatsapp\\'
base_xamp_temp=r'C:\\xampp\\htdocs\\whatsapp\\tempRead'
base_xamp_temp_date=r'C:\\xampp\\htdocs\\whatsapp\\tempReadDate'
url='whatsapp/tempReadDate'
def contains_table(img_base_path, img_name):
    try:
        img_path = os.path.join(img_base_path, img_name)
        img = cv2.imread(img_path)

        results = model(img_path)

        # Check if there are any detected tables (class 0)
        for box in results[0].boxes:
            if box.cls == 0:  # Table class (class 0)
                return True  # Found a table, return True

        return False  # No table detected, return False
    except Exception as e:
         print('contains_tabels:',e)
         traceback.print_exc()


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def model_cut_img(img_base_path, img_name):
    try:
        
        # Process each image file
        img_path = os.path.join(img_base_path, img_name)
        img = cv2.imread(img_path)

        results = model(img_path)
        index = 1
        output_paths = []  # List to hold paths of cropped images

        for box in results[0].boxes:
            if box.cls == 0:  
                xmin, ymin, xmax, ymax = map(int, box.xyxy[0])  

                cropped_table = img[ymin:ymax, xmin:xmax]
                output_name, img_type = os.path.splitext(img_name)
                output_path = f'cut_date___{datetime.now().hour}___{datetime.now().minute}___{datetime.now().second}___{output_name}{index}{img_type}'

                # Save cropped image
                cv2.imwrite(output_path, cropped_table)
                output_paths.append(output_path)  # Store output paths
                index += 1
                
    except Exception as e:
        print('model_cut_img:',e)
        traceback.print_exc()


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def digit(text):
    try:
        # Regex to find the content between + and .
        pattern = r'\!([\d]+)\.'  # Matches anything between + and .
        
        # Search for the pattern
        match = re.search(pattern, text)
        if match:
            # Return the content between + and .
            return int(match.group(1))
        else:
            return -1  # If no match is found
    except Exception as e:
        print('digit:',e)
        traceback.print_exc()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def api_call(dir_name, date, file_name,cs):
    try:
        imgUrl = f'http://46.105.184.179/whatsapp/{dir_name}/{date}/{file_name}'
        conn = http.client.HTTPSConnection("openl-translate.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': '75333e0af4mshe2b8a14812fe4b5p18963cjsn55a9d4410cc4',
            'x-rapidapi-host': 'openl-translate.p.rapidapi.com',
            'Content-Type': 'application/json'
        }

        # Prepare payload with image URL
        payload = f'{{"target_lang":"en","url":"{imgUrl}"}}'
        print(imgUrl)

        # Send the request
        conn.request("POST", "/translate/image", payload.encode('utf-8'), headers)

        # Get response
        res = conn.getresponse()
        data = res.read(), date, file_name  # Store the response, date, and filename as tuple

        resName = f'ocr__{dir_name}___{date}___{cs}____{datetime.now().hour}____{datetime.now().minute}____{datetime.now().second}.txt'

        # Process the response
        if res.status == 200:
            json_response = data[0].decode("utf-8")  # Decode the first element of the tuple (the response)
            print("Response JSON:", json_response)

            response_dict = json.loads(json_response)  # Parse the JSON
            cleaned_response = response_dict.get("translatedText", "")

            # Write the response to a file (for example, result.txt)
            with open(resName, 'a', encoding='utf-8') as f:
                f.write(cleaned_response)

    except Exception as e:
         print('api_call:',e)
         traceback.print_exc()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def seek(dir_name, date):
    try:
        dir_name=dir_name.replace(' ','-')
        current_work_dir = os.path.join(base_xamp_dir, dir_name, date)
        current_work_dir_temp_date=os.path.join(base_xamp_temp_date,date)
        
        os.makedirs(base_xamp_dir, exist_ok=True)
        os.makedirs(base_xamp_temp, exist_ok=True)
        os.makedirs(base_xamp_temp_date, exist_ok=True)
        os.makedirs(current_work_dir, exist_ok=True)
        os.makedirs(current_work_dir_temp_date, exist_ok=True)
        
        all_files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
        img_count = 0
        txt_count = 0
        biggest_number_img = 0
        biggest_number_text = 0
        img_to_ocr = []

        if os.path.isdir(current_work_dir):
            dir_files = [f for f in os.listdir(current_work_dir) if os.path.isfile(os.path.join(current_work_dir, f))]
            
            
            for old_clrearnames in dir_files:
                _, file_type = os.path.splitext(old_clrearnames)
                if file_type in img_end:
                    biggest_number_img += 1
                    check = digit(old_clrearnames)
                    if check > biggest_number_img:
                        biggest_number_img = check
                elif file_type == '.txt':
                    biggest_number_text += 1
                    check = digit(old_clrearnames)
                    if check > biggest_number_text:
                        biggest_number_text = check
        if biggest_number_img:
            img_count = biggest_number_img
        if biggest_number_text:
            txt_count = biggest_number_text

        for file in all_files:
            _, file_ext = os.path.splitext(file)

            if file_ext.lower() in img_end:
                img_name = f'{date}___{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}______{dir_name}!{img_count}{file_ext}'
                os.rename(file, img_name)
                img_to_ocr.append(img_name)
                img_count += 1
                shutil.copy(img_name, os.path.join(current_work_dir, img_name))
                shutil.copy(img_name, os.path.join(current_work_dir_temp_date, img_name))
                shutil.move(img_name, os.path.join(base_xamp_temp, img_name))
            elif file_ext.lower() == '.txt':
                txt_name = f'{date}___{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}______t{dir_name}!{txt_count}{file_ext}'
                os.rename(file, txt_name)
                shutil.copy(txt_name, os.path.join(base_xamp_temp, txt_name))
                shutil.copy(txt_name, os.path.join(current_work_dir_temp_date, txt_name))
                shutil.move(txt_name, os.path.join(current_work_dir, txt_name))
                txt_count += 1

        # OCR part for original images
        tables_exists=False

        for imgs in img_to_ocr:
            if contains_table(current_work_dir,imgs):
                tables_exists=True
                if tables_exists:

                    SERVER_URL = "http://45.156.187.58:5000/process_image_url"  # Local Flask server URL

                    # Read and encode the image
                    send_url=os.path.join('http://46.105.184.179',url, date,imgs).replace('\\','/')

                
                    # Prepare JSON payload
                    json_payload = {
                        "filename": "uploaded_image.jpg",  # Name for the uploaded file
                        "image_url": send_url
                    }

                    # Send request to Flask server
                    response = requests.post(SERVER_URL, json=json_payload)
                    name,_=os.path.splitext(imgs)
                    data = response.json()  # Convert response to JSON

                    with open(f"{name}.txt", "w", encoding="utf-8") as f:
                        if "text" in data:
                            for text in data['text']:
                                f.write(text )    

                last_check = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
                for last_move_files in last_check:
                        _,file_type=os.path.splitext(last_move_files)
                        if file_type in  img_end or file_type=='.txt':
                            shutil.copy(last_move_files, os.path.join(current_work_dir, last_move_files))  # Copy to the current working dir
                            shutil.copy(last_move_files, os.path.join(current_work_dir_temp_date, last_move_files))  # Copy to the current working dir
                            shutil.move(last_move_files, os.path.join(base_xamp_temp, last_move_files))
            else:
                os.remove( os.path.join(current_work_dir, imgs))  #remove the unwanted images
                os.remove( os.path.join(current_work_dir_temp_date, imgs))  #remove the unwanted images
                os.remove( os.path.join(current_work_dir, imgs))
                
        # After cutting images, handle cropped images
    except Exception as e:
        print('seek:',e)
        traceback.print_exc()    





# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
if __name__=="__main__":
    seek('ls', '2025_2_12')