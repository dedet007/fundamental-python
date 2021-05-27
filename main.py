import requests

print('Hello Pluto')

try:
    rl = requests.get('https://mail.google.com')
    print(rl.status_code)
    if rl.status_code == 200:
        print(rl.text)
except Exception as e:
    print('ada error', e)
