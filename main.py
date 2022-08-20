import requests, threading, time
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random

url = 'https://rojansapkota.com.np'
urll = 'https://www.google.com/url?sa=t&source=web&rct=j&url=https://rojansapkota.com.np/&ved=2ahUKEwjoz-jWwtT5AhWjR2wGHfMJC10QFnoECAsQAQ&usg=AOvVaw1_l83Z7fWhL-Xh5GNY8ukh'

headers = {
    "User-Agent":
    agent
}

def requests_sender():
	while True:
		requests.get(url, headers=headers)
		agent = ua.random
		print(f"Request Sent as {agent}")

if __name__ == "__main__":
	requests_sender()
