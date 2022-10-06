import requests, threading, time
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random

url = 'https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRojanGamingYT%2FRojanGamingYT&count_bg=%2379C83D&title_bg=%23555555&icon=v.svg&icon_color=%234ACCC8&title=Profile+Views&edge_flat=false)](https://rojansapkota.com.np'

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
