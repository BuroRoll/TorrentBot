from bs4 import BeautifulSoup
import requests as req
import webbrowser


def get_torrents(name):
    url = 'http://5.45.70.162/search/' + name
    head = {'user-agent': 'Chrome'}
    resp = req.get(url, headers=head)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    a = soup.find_all("tr", {"class": "gai"})
    dic = {}
    for i in range(len(a)):
        if len(a[i].contents[1].contents) == 2:
            dic[a[i].text] = a[i].contents[1].contents[1].attrs['href']

    return dic


def download_torrent(link):
    url = 'http://5.45.70.162' + link
    head = {'user-agent': 'Chrome'}
    resp = req.get(url, headers=head)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    a = soup.find_all('div', {"id": "download"})
    download = 'http://5.45.70.162' + a[0].contents[5].attrs.get('href')
    print(download)
    webbrowser.open(download)
