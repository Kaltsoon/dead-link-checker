class Logger:
    def info(self, message):
        raise NotImplementedError()

    def success(self, message):
        raise NotImplementedError()

    def warning(self, message):
        raise NotImplementedError()

    def error(self, message):
        raise NotImplementedError()
