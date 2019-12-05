from abc import ABC, abstractmethod
from typing import Callable, Dict, Type, TypeVar


class Bot(ABC):
    """Абстрактный класс бота.
    Требуется переопределить метод handle_message.
    Внутри бота доступен метод self.send_message.
    """
    def __init__(self, send_message: Callable[[int, str], None]) -> None:
        """Конструктор бота.
        send_message --- функция, которую бот должен вызвать для отправки сообщения.
            Она принимает два параметра: номер пользователя-получателя сообщения и
            текст сообщения.
             """
        self.send_message = send_message

    @abstractmethod
    def handle_message(self, from_user_id: int, message: str) -> None:
        """Метод, который вызывается у бота, чтобы отправить ему сообщение.
        from_user_id -- номер пользователя, отправившего сообщение.
        message -- текст сообщения.
        """


T = TypeVar('T', bound='UserHandler')
"""Здесь написано, что вместо T должен быть класс, реализующий UserHandler """


class UserIndependentBot(Bot):
    """Конкретная реализация бота, работающего с пользователями независимо.
    send_message -- функция, которую бот должен вызвать для отправки сообщения.
        Она будет передана в конструктор класса Bot.
    user_handler -- класс, реализующий интерфейс UserHandler.
        Для каждого пользователя будет создан независимый экземпляр этого класса.
    """
    def __init__(self, send_message: Callable[[int, str], None], user_handler: Type[T]) -> None:
        super(UserIndependentBot, self).__init__(send_message)
        self.user_handler = user_handler
        self.users: Dict[int, T] = {}

    def handle_message(self, from_user_id: int, message: str) -> None:
        if from_user_id not in self.users:
            self.users[from_user_id] = self.user_handler(
                lambda out_msg: self.send_message(from_user_id, out_msg)
            )
        self.users[from_user_id].handle_message(message)


class UserHandler(ABC):
    """Абстрактный класс обработчика пользователей.
    В нём содержится основная логика обработки пользователей.
    Предполагается, что все пользователи независимы. Обработчик не знает номер своего пользователя.
    Каждый бот создаёт ровно один такой обработчик на каждого пользователя."""
    def __init__(self, send_message: Callable[[str], None]) -> None:
        """Конструктор обработчика.
        send_message -- функция, которую обработчик должен вызвать для отправки сообщения
            пользователю. Она принимает ровно один параметр: текст сообщения."""
        self.send_message = send_message

    @abstractmethod
    def handle_message(self, message: str) -> None:
        """Метод, который бот вызывает у обработчка, чтобы передать ему сообщение
        от пользователя."""
