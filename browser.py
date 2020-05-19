import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
init(autoreset=True)

folder_list = []
website_data = []
history = []
url_list = []


def web_page(url):
    try:
        r = requests.get(url)
    except:
        return "404 Not Found"
    if r:
        tag_list = ['p', 'a', 'h1']
        soup = BeautifulSoup(r.content, "html.parser")
        site_main = soup.children
        html = None
        body = None
        text = []
        for elements in site_main:
            if elements.name == "html":
                html = elements
                break
        for element in list(html.children):
            if element.name == 'body':
                body = element
                break
        for items in body.find_all(tag_list):
            if items.name == "a":
                text.append(Fore.BLUE + items.get_text().strip().replace("\n", " "))
                continue
            text.append(Fore.BLACK + items.get_text().strip().replace("\n", " "))
        final_text = ""
        for items in text:
            final_text += items + "\n"
        return final_text
    else:
        print("Error 404")
        exit(0)


def url(urls):
    web = web_page(urls)
    url_list.append(urls)
    a = urls.rfind(".")
    filename = urls[0:a]
    filename = filename.replace("https://", "")
    current_path = os.getcwd()
    file_path = os.path.join(current_path, folder_list[0])
    if filename not in website_data:
        with open(os.path.join(file_path, filename+".txt"), "w", encoding="utf-8") as file:
            file.write(web)
            file.close()
            website_data.append(filename)
    else:
        pass
    history.append(filename)
    return web


def url_validation(urls):
    if "<" in urls or '>' in urls or "." not in urls:
        return "Error: Invalid URL"
    else:
        if urls in website_data:
            current_path = os.getcwd()
            file_path = os.path.join(current_path, folder_list[0])
            with open(os.path.join(file_path, urls + ".txt"), "r", encoding="utf-8") as file:
                return file.read()
        elif not urls.startswith("https://"):
            urls = "https://" + urls
            return url(urls)
        else:
            return "Error: Invalid URL"


def make_folders(folder_name):
    try:
        folder_list.append(folder_name)
        os.mkdir(folder_name)
    except FileExistsError:
        pass


def back():
    try:
        return history[-2]
    except IndexError:
        return history[0]


make_folders("tb_tabs")
while True:
    url_enter = input()
    if url_enter == "exit":
        break
    if url_enter == "back":
        site = back()
        print(url_validation(site))
    print(url_validation(url_enter))
