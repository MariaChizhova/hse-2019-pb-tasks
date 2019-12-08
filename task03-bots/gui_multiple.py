#!/usr/bin/env python3
import tkinter
import traceback
from typing import Callable, Dict, Optional
from chat_bot import ChatBot


class UserWidget(tkinter.LabelFrame):
    """Класс, реализующий графический интерфейс для работы с одним пользователем."""
    def __init__(self,
                 text: str,
                 send_message_cb: Callable[[str], None],
                 master: Optional[tkinter.Tk] = None):
        """Конструктор.
        send_message_cb - функция, которую нужно вызвать, чтобы отправить сообщение боту."""
        super().__init__(master, text=text)
        self.send_message_cb = send_message_cb
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создаёт часть интерфейса для одного пользователя."""
        self.lines = tkinter.Text(self, wrap='word', state=tkinter.DISABLED, width=1, height=1)
        self.lines.pack(expand=1, fill=tkinter.BOTH, padx=4, pady=4)

        self.send_frame = tkinter.Frame(self, pady=4)
        self.send_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        self.new_command = tkinter.Entry(self.send_frame, width=1)
        self.new_command.bind('<Return>', lambda event: self.send_message())
        self.new_command.pack(side=tkinter.LEFT, expand=1, fill=tkinter.X, padx=4)

        self.send_button = tkinter.Button(self.send_frame, text='Send', command=self.send_message)
        self.send_button.pack(side=tkinter.RIGHT, padx=4)

    def received_message(self, message: str) -> None:
        """Эту функцию вызывает бот для отправки сообщения пользователю.
        Она печатает сообщение в чат."""
        self.add_lines(message)

    def send_message(self) -> None:
        """Эта функция вызвается при отправке сообщения пользователем.
        Отправляет сообщение боту и печатает его в чат."""
        message = self.new_command.get()  # type: ignore
        self.new_command.delete(0, len(message))
        self.add_lines('> ' + message)
        self.send_message_cb(message)

    def add_lines(self, line: str) -> None:
        """Печатает текст в чат пользователя."""
        self.lines.configure(state=tkinter.NORMAL)
        self.lines.insert(tkinter.END, line + '\n')  # type: ignore
        self.lines.configure(state=tkinter.DISABLED)


def main() -> None:
    user_widgets: Dict[int, UserWidget] = {}

    bot = ChatBot(
        send_message=lambda user_id, message: user_widgets[user_id].received_message(message)
    )

    def handle_message(user_id: int, message: str) -> None:
        try:
            bot.handle_message(user_id, message)
        except Exception:  # pylint: disable=W0703
            traceback.print_exc()

    def create_widget(user_id: int) -> None:
        user_widgets[user_id] = UserWidget(
            f'User #{user_id}',
            lambda message: handle_message(user_id, message),
            root
        )

    root = tkinter.Tk()
    root.title('Chat bot debug GUI example')
    root.geometry('640x480')

    rows = 2
    columns = 2
    for row in range(rows):
        tkinter.Grid.rowconfigure(root, row, weight=1)
    for column in range(columns):
        tkinter.Grid.columnconfigure(root, column, weight=1)

    user_id = 1
    for row in range(rows):
        for column in range(columns):
            create_widget(user_id)
            user_widgets[user_id].grid(
                row=row,
                column=column,
                sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E
            )
            user_id += 1

    root.mainloop()


if __name__ == '__main__':
    main()
