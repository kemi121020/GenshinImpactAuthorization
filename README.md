# Simple **Go** Server to encrypt **Genshin Impact** passwords! :mushroom::dolls::flags::ribbon:
## Example of usage:
```python
import requests
inputPassword = input('Enter password:\t') # text there password
resultPassword = requests.post("http://127.0.0.1:6663", data = {'password': inputPassword}).text # Send request to server(post)
# resultPassword = requests.get(f"http://127.0.0.1:6663?password={inputPassword}").text Get Request example
print(f"result: {resultPassword}") # Print result
```
## Result
```
C:\>python example.py
Enter password: 1234
result: IzueGK6L2mEmjbcai3VJ5P9Kodr44yF6cvVA4GmFohj6VzKQLT2g40Deul+u/XIrejo01nIpqz4WRADF7wknvEsP69fzWitKYWDL0GFGsveW/Zd3jSoeWDBxBIQrA2sVoFI9tDEvWszf2fJUxIX8RoS7218r6QQAMZ/rM7XPCqA=
C:\>
```
