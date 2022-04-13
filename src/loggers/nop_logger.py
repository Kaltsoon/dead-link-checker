from loggers.logger import Logger


class NopLogger(Logger):
    def info(self, message: str) -> None:
        pass

    def success(self, message: str) -> None:
        pass

    def warning(self, message: str) -> None:
        pass

    def error(self, message: str) -> None:
        pass
