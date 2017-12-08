class manager:
    def __init__(self):
        self.archived_url = set()
        self.queue = set()
    def addNewUrl(self, urls):
        if urls is None:
            return
        if isinstance(urls, list) or isinstance(urls, tuple):
            new_urls = set(urls) - (set(urls) & self.archived_url)
            self.queue = new_urls | self.queue
        else:
            if urls not in self.archived_url:
                self.queue.add(urls)
    def isEmpty(self):
        return len(self.queue) == 0
    def getUrl(self):
        ret = self.queue.pop()
        self.archived_url.add(ret)
        return ret
    def getAllUrls(self):
        self.archived_url.update(self.queue)
        ret = list(self.queue)
        self.queue = set()
        return ret