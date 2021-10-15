import chalk
from loggers.logger import Logger


class ConsoleLogger(Logger):
    def info(self, message):
        print(message)

    def success(self, message):
        print(chalk.green(message))

    def warning(self, message):
        print(chalk.yellow(message))

    def error(self, message):
        print(chalk.red(message))
