from dataclasses import dataclass, field
from rich.console import Console
from loggers.logger import Logger


@dataclass
class ConsoleLogger(Logger):
    console: Console = field(default_factory=Console)

    def info(self, message: str) -> None:
        self.console.log(message)

    def success(self, message: str) -> None:
        self.console.log(f'[green]{message}[/]')

    def warning(self, message: str) -> None:
        self.console.log(f'[yellow]{message}[/]')

    def error(self, message: str) -> None:
        self.console.log(f'[red]{message}[/]')
