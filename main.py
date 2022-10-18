import requests, threading, time
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random

url = 'https://dsc.gg/invitededsec'

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
