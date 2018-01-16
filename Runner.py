from Core import WebCrawler, CrawlBasicInfo, CrawlDetailInfo
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
crawlBasicInfo.CrawlPER()
crawlBasicInfo.CrawlPBR()
crawlBasicInfo.CrawlEPS()

crawlDetailInfo = CrawlDetailInfo.CrawlDetailInfo(webCrawler, DefineManager.TEST_CRAWL_DETAIL_URL)
crawlDetailInfo.Crawl3YearsBeforeSale()
crawlDetailInfo.Crawl2YearsBeforeSale()
crawlDetailInfo.Crawl1YearsBeforeSale()

webCrawler.CloseDriver()