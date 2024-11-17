import shutil
import os

def direct():
    for i in range(0, 10):
        open(f're{i}.png', 'w').close()

    seek('test', 't_e_s_t')

def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...')
    else:
        print('folder for this chat already exists....')

def seek(path, date):
    imgRe(path)
    move(path, date)

def notToDay(date, fullDate):
    os.makedirs('C:/xampp/htdocs/Watsapp/baygani/', exist_ok=True)
    new_path = f'C:/xampp/htdocs/Watsapp/baygani/{fullDate}.txt'
    os.rename('C:/xampp/htdocs/Watsapp/myfile.txt', new_path)
    return date

def imgRe(name):
    basefiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    
    for file in basefiles:
        _, ftp = os.path.splitext(file)
        counter = 0
        if ftp in ['.jpeg', '.png', '.jpg']:
            while True:
                newname = f"{name}_{counter}{ftp}"
                newname_path = os.path.join(os.getcwd(), newname)
                if not os.path.exists(newname_path):
                    os.rename(file, newname_path)
                    break
                counter += 1

def isthere():
    secDes = os.path.join(B, 'tempRead')
    basefiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    files = [f for f in os.listdir(secDes) if os.path.isfile(os.path.join(secDes, f))]
    
    if len(files) == 0:
        print('no file')
        return 'break'
    
    for file in basefiles:
        for f in files:
            fname, ftp = os.path.splitext(f)
            perent = os.path.dirname(f)
            if f == file:
                name, _ = os.path.splitext(f)
                counter = 0
                while True:
                    if len(name) > 2:
                        newname = f'{name[:-1]}_{counter}{ftp}'
                        if not os.path.exists(os.path.join(os.getcwd(), newname)) and not os.path.exists(os.path.join(secDes, newname)):
                            os.rename(f, newname)
                            return 'break'
                    else:
                        newname = name + '_' + str(counter) + ftp
                        if not os.path.isdir(os.path.join(perent, newname)):
                            if not os.path.exists(os.path.join(os.getcwd(), newname)) and not os.path.exists(os.path.join(secDes, newname)):
                                os.rename(f, newname)
                                return 'break'
                    counter += 1

B = r'C:\xampp\htdocs\Watsapp'

def move(name, date):
    isthere()

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    secDes = os.path.join(B, 'tempRead')
    destination_dir = os.path.join(B, name, date)

    os.makedirs(destination_dir, exist_ok=True)
    os.makedirs(secDes, exist_ok=True)

    for f in files:
        _, Ftypes = os.path.splitext(f)
        if Ftypes in ['.jpeg', '.jpg', '.txt','.png']:
            shutil.copy(f, os.path.join(secDes, f))
            shutil.move(f, os.path.join(destination_dir, f))

if __name__ == '__main__':
    direct()
