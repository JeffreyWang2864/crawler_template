from crawl import url_manager
from crawl import outputer
from crawl import parser
from crawl import downloader
import time
import random
import os
from threading import Thread, Event
from concurrent.futures import ThreadPoolExecutor as tpe

class crawler:
    def __init__(self):
        self.urls = url_manager.manager()
        self.downloader = downloader.download()
        self.parser = parser.parse()
        self.buffer_trigger = Event()
        self.outputer = outputer.output(self.buffer_trigger)
        self.count = 0
        self.thread_pool_size = 3
        self.write_method = self.outputer.writeTXT
    def startCrawl(self, root_url, toggle_print = True):
        def parse_once(new_url):
            try:
                if toggle_print:
                    print("crawling %d : %s" % (self.count, new_url))
                #do something
            except: print("failed\n")
            else: print("successful\n")
        assert isinstance(toggle_print, bool)
        self.urls.addNewUrl(root_url)
        path = str(os.path.dirname(os.path.abspath(__file__))) + "/example.txt"
        write_thread = Thread(target=self.write_method, args=(path, ))
        write_thread.start()
        while not self.urls.isEmpty():
            executor = tpe(self.thread_pool_size)
            all_urls = self.urls.getAllUrls()
            executor.map(parse_once, all_urls)
            executor.shutdown(wait=True)
            if len(self.outputer.data) > self.outputer.buffer_size:
                self.buffer_trigger.set()
        self.outputer.end_writing = True
        self.buffer_trigger.set()
        write_thread.join()
        print("\n\nwrote %d lines of file in total. file located at: %s"%(self.outputer.total_data_count, path))
