import requests, threading, time
from fake_useragent import UserAgent

url = 'https://dsc.gg/joindedsec'

def requests_sender():
	while True:
		ua = UserAgent()
		agent = ua.random
		headers = {
    "User-Agent":
    agent
}
		requests.get(url, headers=headers)
		print(f"Request Sent as {agent}")

if __name__ == "__main__":
	requests_sender()
