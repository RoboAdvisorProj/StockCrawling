from Core import WebCrawler, CrawlBasicInfo, CrawlDetailInfo
from Setting import DefineManager
from Utils import LogManager

class CrawlRoutineManager(object):
    def __init__(self, targetUrl = "", targetDetailUrl = ""):
        self.targetUrl = targetUrl
        self.targetDetailUrl = targetDetailUrl
        self.companyCodes = []
        self.crawlDataArray = []
        LogManager.PrintLogMessage("CrawlRoutineManager", "__init__", "init routine manager", DefineManager.LOG_LEVEL_INFO)
        return

    def OpenWebDriver(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "OpenWebDriver", "open web driver", DefineManager.LOG_LEVEL_INFO)
        self.webCrawler = WebCrawler.WebCrawler()

    def SetCrawlCompanyCode(self, companyCodes):
        LogManager.PrintLogMessage("CrawlRoutineManager", "SetCrawlCompanyCode", "setup companyCodes", DefineManager.LOG_LEVEL_INFO)
        self.companyCodes = companyCodes

    def RunCrawling(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "RunCrawling", "running company stock price crawling", DefineManager.LOG_LEVEL_INFO)
        for indexOfCompanyCode in self.companyCodes:
            companyCode = indexOfCompanyCode
            self.targetUrl = "http://finance.naver.com/item/main.nhn?code=" + companyCode
            self.targetDetailUrl = "http://finance.naver.com/item/coinfo.nhn?code=" + companyCode + "&target=finsum_more"
            LogManager.PrintLogMessage("CrawlRoutineManager", "RunCrawling", "start crawling company: " + companyCode, DefineManager.LOG_LEVEL_INFO)
            self.StartCrawl()

    def StartCrawl(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "StartCrawl", "crawl data", DefineManager.LOG_LEVEL_INFO)
        crawlDataDic = {}
        crawlBasicInfo = CrawlBasicInfo.CrawlBasicInfo(self.webCrawler, self.targetUrl)
        crawlDataDic["Name"] = crawlBasicInfo.CrawlCompanyName() or ""
        crawlDataDic["Code"] = crawlBasicInfo.CrawlCompanyStockCode() or ""
        crawlDataDic["Price"] = crawlBasicInfo.CrawlStockPrice() or ""
        crawlDataDic["D_PRH"] = crawlBasicInfo.CrawlHighestStockPrice() or ""
        crawlDataDic["D_PRL"] = crawlBasicInfo.CrawlLowestStockPrice() or ""
        crawlDataDic["Y_PRH"] = crawlBasicInfo.CrawlBestYearPrice() or ""
        crawlDataDic["Y_PRL"] = crawlBasicInfo.CrawlWorstYearPrice() or ""
        crawlDataDic["D_IV"] = crawlBasicInfo.CrawlDividendYield() or ""
        crawlDataDic["Change"] = crawlBasicInfo.CrawlPriceChangedPercent() or ""
        crawlDataDic["Value"] = crawlBasicInfo.CrawlMarketCapitalization() or ""
        crawlDataDic["Beta"] = crawlBasicInfo.CrawlYearBeta() or ""
        crawlDataDic["PER"] = crawlBasicInfo.CrawlPER() or ""
        crawlDataDic["PBR"] = crawlBasicInfo.CrawlPBR() or ""
        crawlDataDic["EPS"] = crawlBasicInfo.CrawlEPS() or ""

        crawlDetailInfo = CrawlDetailInfo.CrawlDetailInfo(self.webCrawler, self.targetDetailUrl)
        crawlDataDic["SALEQ2"] = crawlDetailInfo.Crawl3YearsBeforeSale() or ""
        crawlDataDic["SALEQ1"] = crawlDetailInfo.Crawl2YearsBeforeSale() or ""
        crawlDataDic["SALEQ0"] = crawlDetailInfo.Crawl1YearsBeforeSale() or ""
        crawlDataDic["NIQ2"] = crawlDetailInfo.Crawl3YearsBeforeNetIncome() or ""
        crawlDataDic["NIQ1"] = crawlDetailInfo.Crawl2YearsBeforeNetIncome() or ""
        crawlDataDic["NIQ0"] = crawlDetailInfo.Crawl1YearsBeforeNetIncome() or ""
        crawlDataDic["ACT"] = crawlDetailInfo.CrawlActQ3() or ""
        crawlDataDic["DPT"] = crawlDetailInfo.CrawlDptQ3() or ""
        crawlDataDic["CAP"] = crawlDetailInfo.CrawlCapQ3() or ""

        for key in crawlDataDic:
            LogManager.PrintLogMessage("CrawlRoutineManager", "StartCrawl", "" + key + ": " + crawlDataDic[key], DefineManager.LOG_LEVEL_DEBUG)

        self.crawlDataArray.append(crawlDataDic)
        LogManager.PrintLogMessage("CrawlRoutineManager", "StartCrawl", "saved crawl data size: " + str(self.crawlDataArray.__len__()), DefineManager.LOG_LEVEL_INFO)

    def CloseWebDriver(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "CloseWebDriver", "shut down web driver", DefineManager.LOG_LEVEL_INFO)
        self.webCrawler.CloseDriver()

    def GetCrawlDataArray(self):
        LogManager.PrintLogMessage("CrawlRoutineManager", "GetCrawlDataArray", "return crawled data array", DefineManager.LOG_LEVEL_INFO)
        return self.crawlDataArray

    def __del__(self):
        return