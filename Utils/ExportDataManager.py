from Setting import DefineManager
from Utils import LogManager
import csv

class ExportDataManager(object):
    def __init__(self):
        LogManager.PrintLogMessage("ExportDataManager", "__init__", "init", DefineManager.LOG_LEVEL_INFO)
        self.dataArray = []
        return

    def SetDataArray(self, dataArray):
        LogManager.PrintLogMessage("ExportDataManager", "SetDataArray", "setup data array", DefineManager.LOG_LEVEL_INFO)
        self.dataArray = dataArray

    def ExportDataArrayAsCSV(self, fileName = "", saveKeyList = []):
        LogManager.PrintLogMessage("ExportDataManager", "ExportDataArrayAsCSV", "export data array size: " + str(self.dataArray.__len__()), DefineManager.LOG_LEVEL_INFO)

        try:
            fileManager = open(fileName, "w", encoding="utf-8", newline="")
            csvWriter = csv.writer(fileManager)
            for indexOfDataArray in self.dataArray:
                csvRow = []
                for key in indexOfDataArray:
                    if any(key in keyItem for keyItem in saveKeyList) == True:
                        csvRow.append(indexOfDataArray[key])
                csvWriter.writerow(csvRow)
            fileManager.close()

            LogManager.PrintLogMessage("ExportDataManager", "ExportDataArrayAsCSV", "exported done!",
                                       DefineManager.LOG_LEVEL_INFO)
        except:
            LogManager.PrintLogMessage("ExportDataManager", "ExportDataArrayAsCSV", "export failed", DefineManager.LOG_LEVEL_ERROR)
        return

    def __del__(self):
        return