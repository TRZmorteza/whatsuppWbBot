import os
import shutil


def move(name,date):
    
    ff = slice(-5, None)  

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

    destination_dir = os.path.join(os.getcwd(), 'downlods', name,date)

    os.makedirs(destination_dir, exist_ok=True)  
    for f in (files):
        print(f[ff])  
        if f[ff] in ['.jpeg', '.jpg']: 
            shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))

