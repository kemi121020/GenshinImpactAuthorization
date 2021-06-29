import requests
inputPassword = input('Enter password:\t')
resultPassword = requests.post("http://127.0.0.1:6663", data = {'password': inputPassword}).text
print(f"result: {resultPassword}")
