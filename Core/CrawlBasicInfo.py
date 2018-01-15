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
            companyElements = webDriver.find_element_by_class_name(DefineManager.COMPANY_INFO_ELEMENTS_CLASS_NAME)
            companyName = companyElements.find_element_by_tag_name("a").text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name successfully: " + companyName, DefineManager.LOG_LEVEL_INFO)
            return companyName
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlCompanyStockCode(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            companyElements = webDriver.find_element_by_class_name(DefineManager.COMPANY_INFO_ELEMENTS_CLASS_NAME)
            companyStockCode = companyElements.find_element_by_class_name("code").text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyStockCode", "crawl company code successfully: " + companyStockCode, DefineManager.LOG_LEVEL_INFO)
            return companyStockCode
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyStockCode", "crawl company code failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlStockPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            stockElements = webDriver.find_element_by_class_name(DefineManager.STOCK_PRICE_ELEMENTS_CLASS_NAME)
            stockPrice = stockElements.find_element_by_class_name(DefineManager.STOCK_NUMBER_CLASS_NAME)
            stockPriceNumberElements = stockPrice.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            stockPriceStr = ""
            for indexOfSpanNumber in stockPriceNumberElements:
                stockPriceStr = stockPriceStr + indexOfSpanNumber.text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockPrice", "crawl stock price successfully: " + stockPriceStr, DefineManager.LOG_LEVEL_INFO)

            return stockPriceStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockPrice", "crawl stock price failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlHighestStockPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            highLowPriceTable = webDriver.find_element_by_class_name(DefineManager.STOCK_HIGH_LOW_PRICE_INFO_TABLE)
            highPriceTableRow = highLowPriceTable.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.HIGHEST_PRICE_SAVED_ROW_POINT]
            highPriceTableCol = highPriceTableRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.HIGHEST_PRICE_SAVED_COL_POINT]
            highPrice = highPriceTableCol.find_element_by_class_name(DefineManager.STOCK_HIGH_NUMBER_CLASS_NAME)
            highPriceNumberElements = highPrice.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            highPriceStr = ""
            for indexOfSpanNumber in highPriceNumberElements:
                highPriceStr = highPriceStr + indexOfSpanNumber.text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlHighestStockPrice", "crawl highest stock price successfully: " + highPriceStr, DefineManager.LOG_LEVEL_INFO)
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockHighestPrice", "crawl highest stock price failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def __del__(self):
        return