import requests, threading, time
from fake_useragent import UserAgent
from flask import Flask, render_template

app = Flask(__name__)
ua = UserAgent()
agent = ua.random

@app.route('/')
def index():
  return render_template("index.html")

url ='https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRojanGamingYT%2FRojanGamingYT'

urll = 'https://l.instagram.com/?u=https%3A%2F%2Frojansapkota.com.np%2F&e=ATOOyL2K5Q0S91Mk-jqZPvf5UY-xewGCP2RGEtcxXhJWnN_VZOirdnVBPlyHDwfCQg0AuQuUG2cVKHijBljlUg&s=1'

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
app.run(host='0.0.0.0', port=8080)