from loggers.logger import Logger


class NopLogger(Logger):
    def info(self, message):
        pass

    def success(self, message):
        pass

    def warning(self, message):
        pass

    def error(self, message):
        pass
