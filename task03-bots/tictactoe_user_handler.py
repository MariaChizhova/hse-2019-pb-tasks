from typing import Callable, Optional
from bot import UserHandler
from tictactoe import Player, TicTacToe


class TicTacToeUserHandler(UserHandler):
    def __init__(self, send_message: Callable[[str], None]) -> None:
        super(TicTacToeUserHandler, self).__init__(send_message)
        self.game: Optional[TicTacToe] = None

    def handle_message(self, message: str) -> None:
        if message == 'start':
            self.start_game()
        elif not self.game:
            self.send_message('Game is not started')
        else:
            mark, col, row = message.split()
            player = {'X': Player.X, 'O': Player.O}.get(mark)
            if mark != 'X' and mark != 'O':
                self.send_message('Invalid turn')
            else:
                assert player
                self.make_turn(player, row=int(row), col=int(col))

    def start_game(self) -> None:
        self.game = TicTacToe()
        self.send_field()

    def make_turn(self, player: Player, *, row: int, col: int) -> None:
        assert self.game
        if not self.game.can_make_turn(player, row=row, col=col):
            self.send_message('Invalid turn')
        else:
            self.game.make_turn(player, row=row, col=col)
            self.send_field()
            if self.game.is_finished():
                self.send_message(
                    'Game is finished, {}'.format({None: 'draw', Player.X: 'X wins',
                                                   Player.O: 'O wins'}.get(self.game.winner())))
                self.game = None

    def send_field(self) -> None:
        assert self.game
        field = []
        for row in self.game.field:
            field.append(''.join([col.name if col else '.' for col in row]))
        self.send_message('\n'.join(field))
>>>>>>> df773e0a0839d8887fae58c54a7190f4a7564abc
