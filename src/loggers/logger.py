class Logger:
    def info(self, message: str):
        raise NotImplementedError()

    def success(self, message: str):
        raise NotImplementedError()

    def warning(self, message: str):
        raise NotImplementedError()

    def error(self, message: str):
        raise NotImplementedError()
