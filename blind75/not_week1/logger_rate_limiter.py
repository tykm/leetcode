class Logger:

    def __init__(self):
        self.times = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.times:
            self.times[message] = timestamp
            return True
        else:
            if timestamp - self.times[message] >= 10:
                self.times[message] = timestamp
                return True
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)