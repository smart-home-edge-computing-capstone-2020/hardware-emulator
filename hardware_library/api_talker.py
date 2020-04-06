import requests, sys

URL = "http://127.0.0.1:8000/emulator/"

if sys.argv[1] == 'GET':
    r = requests.get(url=URL+sys.argv[2])
    data = r.json();
    print(data);

elif sys.argv[1] == 'POST':
    data = {'name':sys.argv[3],
            'description':sys.argv[4]}
    r = requests.post(url=URL+sys.argv[2], data=data)
    print(r.json())