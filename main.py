import requests, threading, time
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random

url = 'https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=rojansapkota.com.np&count_bg=%2379C83D&title_bg=%23555555&icon=v.svg&icon_color=%234ACCC8&title=Website+Views&edge_flat=true'
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
