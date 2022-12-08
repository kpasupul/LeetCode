class Logger:

    def __init__(self):
        self.loggerdata = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.loggerdata:
            self.loggerdata[message] = timestamp
            return True

        if timestamp < self.loggerdata[message] + 10:
            return False 
        else:
            self.loggerdata[message] = timestamp
            return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
