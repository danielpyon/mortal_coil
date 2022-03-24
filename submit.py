from solve import Board, solve
import numpy as np
import requests
import bs4

def parse(html):
    soup = bs4.BeautifulSoup(html)
    td = soup.find('td', {'id': 'pgfirst'})
    script = td.findChildren('script', recursive=False)[0]

    data = script.text.split(' = ')
    h, w = int(data[2][:1]), int(data[3][:1])
    st = data[4][1:][:-2]
    
    state = np.zeros((h, w), dtype=bool)
    for i in range(h):
        for j in range(w):
            if st[j + i * w] == 'X':
                state[i, j] = True

    return state

def submit(url, cookies, start, path):
    x, y = start
    x, y = str(x + 1), str(y + 1)
    payload = {
            'x': x,
            'y': y,
            'path': path
    }
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "Referer": "https://www.hacker.org/coil/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "DNT": "1",
    }
    if len(path) > 512:
        r = requests.post(url, cookies=cookies, data=payload, headers=headers)
    else:
        r = requests.get(url, cookies=cookies, params=payload, headers=headers)
    return r

url = 'https://www.hacker.org/coil/'
r = requests.get(url)

print(r.cookies.get_dict())
while True:
    state = parse(r.text)
    print(state)
    start, path = solve(state)
    r = submit(url, r.cookies, start, path)
    print(r.text)
