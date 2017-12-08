from crawl import crawler

root_url = "https://www.yelp.com/biz/godavari-woburn-2?start=10"
obj_spider = crawler.crawler()
obj_spider.startCrawl(root_url)