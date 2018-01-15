from Setting import DefineManager
from Utils import LogManager

class CrawlBasicInfo(object):
    def __init__(self, webCrawler, crawlUrl):
        self.webCrawler = webCrawler
        self.crawlUrl = crawlUrl
        urlStatus = str(self.webCrawler.SetDriverUrl(crawlUrl))
        crawlerStatus = str(self.webCrawler.GetDriverStatus())
        msg = "web driver status: " + crawlerStatus + " url status: " + urlStatus
        LogManager.PrintLogMessage("CrawlBasicInfo", "__init__", msg, DefineManager.LOG_LEVEL_INFO)

    def __del__(self):
        return