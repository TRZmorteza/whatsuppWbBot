import os
import shutil

def make(name):
    destination_dir = os.path.join(os.getcwd(), 'downlods', name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')

def seek():
    pass#for know
def move(name,date):
    
    ff = slice(-5, None)  

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

    destination_dir = os.path.join(os.getcwd(), 'downlods', name,date)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)  
        for f in (files):
            print(f[ff])  
            if f[ff] in ['.jpeg', '.jpg']: 
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
    else:
        print('i already get this img....')
        for f in (files):
            print(f[ff])  
            if f[ff] in ['.jpeg', '.jpg']: 
                os.remove(os.path.join(os.getcwd(), f))
        print('deleted the unwanted img...')
