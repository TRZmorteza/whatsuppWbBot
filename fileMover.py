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
import Locr
model=YOLO('best.pt')
img_end=['.jpg', '.jpeg','.png']

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
                img_to_ocr.append(os.path.join(current_work_dir_temp_date, img_name))
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

                    

                    # Read and encode the image
                    result=Locr.strater(imgs)

                
                    name,_=os.path.splitext(imgs)

                    with open(f"{name}.txt", "w", encoding="utf-8") as f:
                        for line in result:
                            f.write(line)

                last_check = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
                for last_move_files in last_check:
                        _,file_type=os.path.splitext(last_move_files)
                        if file_type in  img_end or file_type=='.txt':
                            shutil.copy(last_move_files, os.path.join(current_work_dir, last_move_files))  # Copy to the current working dir
                            shutil.copy(last_move_files, os.path.join(current_work_dir_temp_date, last_move_files))  # Copy to the current working dir
                            shutil.move(last_move_files, os.path.join(base_xamp_temp, last_move_files))
            
                
        # After cutting images, handle cropped images
    except Exception as e:
        print('seek:',e)
        traceback.print_exc()    





# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
if __name__=="__main__":
    seek('ls', '2025_2_12')