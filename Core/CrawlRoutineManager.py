from Core import WebCrawler, CrawlBasicInfo, CrawlDetailInfo
from Setting import DefineManager
from Utils import LogManager

class CrawlRoutineManager(object):
    def __init__(self, targetUrl, targetDetailUrl):
        self.targetUrl = targetUrl
        self.targetDetailUrl = targetDetailUrl
        self.crawlDataArray = []
        LogManager.PrintLogMessage("CrawlRoutineManager", "__init__", "init routine manager", DefineManager.LOG_LEVEL_INFO)
        return

    def OpenWebDriver(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "OpenWebDriver", "open web driver", DefineManager.LOG_LEVEL_INFO)
        self.webCrawler = WebCrawler.WebCrawler()

    def StartCrawl(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "StartCrawl", "crawl data", DefineManager.LOG_LEVEL_INFO)
        crawlDataDic = {}
        crawlBasicInfo = CrawlBasicInfo.CrawlBasicInfo(self.webCrawler, self.targetUrl)
        crawlDataDic["Name"] = crawlBasicInfo.CrawlCompanyName()
        crawlDataDic["Code"] = crawlBasicInfo.CrawlCompanyStockCode()
        crawlDataDic["Price"] = crawlBasicInfo.CrawlStockPrice()
        crawlDataDic["D_PRH"] = crawlBasicInfo.CrawlHighestStockPrice()
        crawlDataDic["D_PRL"] = crawlBasicInfo.CrawlLowestStockPrice()
        crawlDataDic["Y_PRH"] = crawlBasicInfo.CrawlBestYearPrice()
        crawlDataDic["Y_PRL"] = crawlBasicInfo.CrawlWorstYearPrice()
        crawlDataDic["D_IV"] = crawlBasicInfo.CrawlDividendYield()
        crawlDataDic["Change"] = crawlBasicInfo.CrawlPriceChangedPercent()
        crawlDataDic["Value"] = crawlBasicInfo.CrawlMarketCapitalization()
        crawlDataDic["Beta"] = crawlBasicInfo.CrawlYearBeta()
        crawlDataDic["PER"] = crawlBasicInfo.CrawlPER()
        crawlDataDic["PBR"] = crawlBasicInfo.CrawlPBR()
        crawlDataDic["EPS"] = crawlBasicInfo.CrawlEPS()

        crawlDetailInfo = CrawlDetailInfo.CrawlDetailInfo(self.webCrawler, self.targetDetailUrl)
        crawlDataDic["SALEQ2"] = crawlDetailInfo.Crawl3YearsBeforeSale()
        crawlDataDic["SALEQ1"] = crawlDetailInfo.Crawl2YearsBeforeSale()
        crawlDataDic["SALEQ0"] = crawlDetailInfo.Crawl1YearsBeforeSale()
        crawlDataDic["NIQ2"] = crawlDetailInfo.Crawl3YearsBeforeNetIncome()
        crawlDataDic["NIQ1"] = crawlDetailInfo.Crawl2YearsBeforeNetIncome()
        crawlDataDic["NIQ0"] = crawlDetailInfo.Crawl1YearsBeforeNetIncome()
        crawlDataDic["ACT"] = crawlDetailInfo.CrawlActQ3()
        crawlDataDic["DPT"] = crawlDetailInfo.CrawlDptQ3()
        crawlDataDic["CAP"] = crawlDetailInfo.CrawlCapQ3()

        for key in crawlDataDic:
            LogManager.PrintLogMessage("CrawlRoutineManager", "StartCrawl", "" + key + ": " + crawlDataDic[key], DefineManager.LOG_LEVEL_DEBUG)

        self.crawlDataArray.append(crawlDataDic)

    def CloseWebDriver(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "CloseWebDriver", "shut down web driver", DefineManager.LOG_LEVEL_INFO)
        self.webCrawler.CloseDriver()

    def GetCrawlDataArray(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "GetCrawlDataArray", "return crawled data array", DefineManager.LOG_LEVEL_INFO)
        return self.crawlDataArray

    def __del__(self):
        return