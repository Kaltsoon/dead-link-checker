class Logger:
    def info(self, message: str) -> None:
        raise NotImplementedError()

    def success(self, message: str) -> None:
        raise NotImplementedError()

    def warning(self, message: str) -> None:
        raise NotImplementedError()

    def error(self, message: str) -> None:
        raise NotImplementedError()
