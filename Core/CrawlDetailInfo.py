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

    def Crawl2YearsBeforeSale(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialSaleRow = financialRows[DefineManager.FINANCIAL_SALE_ROW_POINT]
            financialSaleStr = financialSaleRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_SALE_2_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl2YearsBeforeSale", "crawl 2 years before sale successfully: " + financialSaleStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialSaleStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl2YearsBeforeSale", "crawl 2 years before sale failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def Crawl1YearsBeforeSale(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialSaleRow = financialRows[DefineManager.FINANCIAL_SALE_ROW_POINT]
            financialSaleStr = financialSaleRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_SALE_1_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl1YearsBeforeSale", "crawl 1 years before sale successfully: " + financialSaleStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialSaleStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl1YearsBeforeSale", "crawl 1 years before sale failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def Crawl3YearsBeforeNetIncome(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialNetIncomeRow = financialRows[DefineManager.FINANCIAL_NET_INCOME_ROW_POINT]
            financialNetIncomeStr = financialNetIncomeRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_NET_INCOME_3_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl3YearsBeforeNetIncome", "crawl 3 years before net income successfully: " + financialNetIncomeStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialNetIncomeStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl3YearsBeforeNetIncome", "crawl 3 years before net income failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def Crawl2YearsBeforeNetIncome(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialNetIncomeRow = financialRows[DefineManager.FINANCIAL_NET_INCOME_ROW_POINT]
            financialNetIncomeStr = financialNetIncomeRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_NET_INCOME_2_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl2YearsBeforeNetIncome", "crawl 2 years before net income successfully: " + financialNetIncomeStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialNetIncomeStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl2YearsBeforeNetIncome", "crawl 2 years before net income failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def Crawl1YearsBeforeNetIncome(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialNetIncomeRow = financialRows[DefineManager.FINANCIAL_NET_INCOME_ROW_POINT]
            financialNetIncomeStr = financialNetIncomeRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_NET_INCOME_1_YEARS_BEFORE_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl1YearsBeforeNetIncome", "crawl 1 years before net income successfully: " + financialNetIncomeStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialNetIncomeStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "Crawl1YearsBeforeNetIncome", "crawl 1 years before net income failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlActQ3(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialActRow = financialRows[DefineManager.FINANCIAL_ACT_ROW_POINT]
            financialActStr = financialActRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.FINANCIAL_Q3_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlActQ3", "crawl ACT Q3 successfully: " + financialActStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialActStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlActQ3", "crawl ACT Q3 failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlDptQ3(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialDptRow = financialRows[DefineManager.FINANCIAL_DPT_ROW_POINT]
            financialDptStr = financialDptRow.find_elements_by_tag_name(DefineManager.TAG_TD)[
                DefineManager.FINANCIAL_Q3_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlDptQ3", "crawl DPT Q3 successfully: " + financialDptStr,
                                       DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialDptStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlDptQ3", "crawl DPT Q3 failed",
                                       DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlCapQ3(self):
        try:
            webDriver = self.webCrawler.GetDriver()

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            financialTable = webDriver.find_element_by_id(DefineManager.FINANCIAL_TABLE_ID_NAME)
            financialRows = financialTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            financialCapRow = financialRows[DefineManager.FINANCIAL_CAP_ROW_POINT]
            financialCapStr = financialCapRow.find_elements_by_tag_name(DefineManager.TAG_TD)[
                DefineManager.FINANCIAL_Q3_COL_POINT].text

            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlCapQ3", "crawl CAP Q3 successfully: " + financialCapStr,
                                       DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()

            return financialCapStr
        except:
            LogManager.PrintLogMessage("CrawlDetailInfo", "CrawlCapQ3", "crawl CAP Q3 failed",
                                       DefineManager.LOG_LEVEL_ERROR)

        return None

    def __del__(self):
        return