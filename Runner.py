from Core import CrawlRoutineManager
from Setting import DefineManager

crawlRoutineManager = CrawlRoutineManager.CrawlRoutineManager(DefineManager.TEST_CRAWL_URL, DefineManager.TEST_CRAWL_DETAIL_URL)
crawlRoutineManager.OpenWebDriver()
crawlRoutineManager.StartCrawl()
crawlRoutineManager.CloseWebDriver()