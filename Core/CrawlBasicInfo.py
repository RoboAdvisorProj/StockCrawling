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

    def CrawlCompanyName(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            companyElements = webDriver.find_element_by_class_name("wrap_company")
            companyName = companyElements.find_element_by_tag_name("a").text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name successfully: " + companyName, DefineManager.LOG_LEVEL_INFO)
            return companyName
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def __del__(self):
        return