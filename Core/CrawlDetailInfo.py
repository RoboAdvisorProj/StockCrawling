from Setting import DefineManager
from Utils import LogManager

class CrawlDetailInfo(object):
    def __init__(self, webCrawler, crawlUrl):
        self.webCrawler = webCrawler
        self.crawlUrl = crawlUrl
        urlStatus = str(self.webCrawler.SetDriverUrl(crawlUrl))
        crawlerStatus = str(self.webCrawler.GetDriverStatus())
        msg = "web driver status: " + crawlerStatus + " url status: " + urlStatus
        LogManager.PrintLogMessage("CrawlDetailInfo", "__init__", msg, DefineManager.LOG_LEVEL_INFO)

    def Crawl3YearsBeforeSale(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialSaleRow = financialRows[DefineManager.FINANCIAL_SALE_ROW_POINT]
            financialSaleStr = financialSaleRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_SALE_3_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl3YearsBeforeSale", "crawl 3 years before sale successfully: " + financialSaleStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialSaleStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl3YearsBeforeSale", "crawl 3 years before sale failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def __del__(self):
        return