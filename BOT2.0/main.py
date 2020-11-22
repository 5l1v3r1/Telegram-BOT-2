import requests

f = open("token.0", "r")
token = f.readline()
f.close()

server_id = "-443895120"
send_message = "Bot works!"
web_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={server_id}&text='{send_message}'"
requests.get(web_url)