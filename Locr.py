import cv2
import traceback
from ultralytics import YOLO
from paddleocr import PaddleOCR  # Import PaddleOCR

# Initialize YOLO model
model = YOLO('best.pt')

# Initialize PaddleOCR model for Persian and English languages
ocr_model = PaddleOCR(use_angle_cls=True, lang='en')  # 'fa' for Persian, 'en' is default

def contains_table(img_base_path):
    try:
        img = cv2.imread(img_base_path)  # Read the image in color (BGR)
        results = model(img)  # Pass the color image to YOLO

        # Check if there are any detected tables (class 0)
        for box in results[0].boxes:
            if box.cls == 0:  # Table class (class 0)
                return True  # Found a table, return True

        return False  # No table detected, return False
    except Exception as e:
        print('contains_table:', e)
        
        return False

def ocr(img_base_path):
    try:
        extract = []
        img = cv2.imread(img_base_path)  # Read the image in color (BGR)
        results = model(img)  # Pass the color image to YOLO
        for box in results[0].boxes:
                try:
                    if box.cls == 1:  # Class 1 (row)
                        xmin, ymin, xmax, ymax = map(int, box.xyxy[0])  # Get the coordinates of the row
                        cropped_row = img[ymin:ymax, xmin:xmax]
                    
                        if cropped_row is None or cropped_row.size == 0:
                            print("Warning: Skipping empty cropped image")
                            continue
                        
                        # Use PaddleOCR to extract text from the cropped row
                        ocr_result = ocr_model.ocr(cropped_row, cls=True)  # OCR on the cropped image
                        
                        if not ocr_result or not ocr_result[0]:
                            print("Warning: OCR returned empty result")
                            continue
                        
                        # Process the OCR result
                        result_text = ' '.join([line[1][0] for line in ocr_result[0]]) + '\n'
                        result_text = result_text.replace(',', '').replace('.', '')
                        extract.append(result_text)
        
                except Exception as e:
                    print('Error processing a box:', e)
        return extract  # ✅ Returning the extracted text
    except Exception as e:
        print('model_cut_img:', e)
        traceback.print_exc()
        return []

def strater(img_path):
    
    if contains_table(img_path):
        result= ocr(img_path)
        print(result)
        return result
