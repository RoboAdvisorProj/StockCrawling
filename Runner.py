from Core import CrawlRoutineManager
from Utils import ExportDataManager

# SK하이닉스, 한올바이오파마, 아남전자, 삼성중공업, 삼성전, 한국항공우주, 카카오. 일진다이, 지엠비코리아, 삼성엔지니어링
companyCodeList = [
    "000660", "009420", "008700", "010140", "005930", "047810", "035720", "081000", "013870", "028050"
]

crawlRoutineManager = CrawlRoutineManager.CrawlRoutineManager()
crawlRoutineManager.OpenWebDriver()
crawlRoutineManager.SetCrawlCompanyCode(companyCodeList)
crawlRoutineManager.RunCrawling()
crawlRoutineManager.CloseWebDriver()

exportDataManager = ExportDataManager.ExportDataManager()
exportDataManager.SetDataArray(crawlRoutineManager.GetCrawlDataArray())
exportDataManager.ExportDataArrayAsCSV()