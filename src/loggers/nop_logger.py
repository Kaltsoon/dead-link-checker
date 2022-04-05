from loggers.logger import Logger


class NopLogger(Logger):
    def info(self, message: str):
        pass

    def success(self, message: str):
        pass

    def warning(self, message: str):
        pass

    def error(self, message: str):
        pass
