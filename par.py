from bs4 import BeautifulSoup
import requests as req


class Parser(object):
    def __init__(self):
        self.torrent_url = 'http://5.45.70.162'

    def get_torrents(self, name):
        url = self.torrent_url + '/search/' + name
        data = self.parse(url)
        a = data.find_all("tr", {"class": "gai"})
        dic = {}
        for i in range(len(a)):
            if len(a[i].contents[1].contents) == 2:
                dic[a[i].text] = a[i].contents[1].contents[1].attrs['href']
        return dic

    def download_torrent(self, link):
        url = self.torrent_url + link
        data = self.parse(url)
        a = data.find_all('div', {"id": "download"})
        name = a[0].contents[5].attrs.get('href').split('/')[4]
        download = 'http://5.45.70.162' + a[0].contents[5].attrs.get('href')
        print(download)
        torrent_file = open(name + '.torrent', 'wb')
        t_file = req.get(download)
        torrent_file.write(t_file.content)
        torrent_file.close()

    @staticmethod
    def parse(link):
        head = {'user-agent': 'Chrome'}
        resp = req.get(link, headers=head)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        return soup
