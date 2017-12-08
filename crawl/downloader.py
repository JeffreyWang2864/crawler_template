from urllib import request

class download:
    def __init__(self, url):
        self.url = url
    def startDownload(self, url = None):
        if url is None:
            assert self.url is not None
        res = request.urlopen(self.url)
        if res.getcode() == 200:
            return res.read()
        else:
            raise ConnectionError("download failed")