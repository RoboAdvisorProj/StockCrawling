from Core import WebCrawler, CrawlBasicInfo
from Setting import DefineManager

webCrawler = WebCrawler.WebCrawler()

crawlBasicInfo = CrawlBasicInfo.CrawlBasicInfo(webCrawler, DefineManager.TEST_CRAWL_URL)
crawlBasicInfo.CrawlCompanyName()
crawlBasicInfo.CrawlCompanyStockCode()
crawlBasicInfo.CrawlStockPrice()
crawlBasicInfo.CrawlHighestStockPrice()
crawlBasicInfo.CrawlLowestStockPrice()
crawlBasicInfo.CrawlBestYearPrice()
crawlBasicInfo.CrawlWorstYearPrice()
crawlBasicInfo.CrawlDividendYield()
crawlBasicInfo.CrawlPriceChangedPercent()
crawlBasicInfo.CrawlMarketCapitalization()
crawlBasicInfo.CrawlYearBeta()

webCrawler.CloseDriver()