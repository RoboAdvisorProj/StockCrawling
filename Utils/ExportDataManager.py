from Setting import DefineManager
from Utils import LogManager

class ExportDataManager(object):
    def __init__(self):
        LogManager.PrintLogMessage("ExportDataManager", "__init__", "init", DefineManager.LOG_LEVEL_INFO)
        self.dataArray = []
        return

    def SetDataArray(self, dataArray):
        LogManager.PrintLogMessage("ExportDataManager", "SetDataArray", "setup data array", DefineManager.LOG_LEVEL_INFO)
        self.dataArray = dataArray

    def ExportDataArrayAsCSV(self):
        LogManager.PrintLogMessage("ExportDataManager", "ExportDataArrayAsCSV", "export data array size: " + str(self.dataArray.__len__()), DefineManager.LOG_LEVEL_INFO)
        return

    def __del__(self):
        return