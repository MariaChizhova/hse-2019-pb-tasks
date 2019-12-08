import pytest_mock
from tictactoe_user_handler import TicTacToeUserHandler


def test_game_not_started(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('O 2 1')
    bot.handle_message('Hello')
    assert send_message.call_args_list == [
        mocker.call('Game is not started'),
        mocker.call('Game is not started')]


def test_game_many_starts(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('start')
    bot.handle_message('start')
    bot.handle_message('start')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('...\n...\n...'),
        mocker.call('...\n...\n...'),
        mocker.call('...\n...\n...')]


def test_x_wins(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 1 1')
    bot.handle_message('O 1 2')
    bot.handle_message('X 0 0')
    bot.handle_message('O 2 2')
    bot.handle_message('X 0 2')
    bot.handle_message('O 2 0')
    bot.handle_message('X 0 1')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('...\n.X.\n...'),
        mocker.call('...\n.X.\n.O.'),
        mocker.call('X..\n.X.\n.O.'),
        mocker.call('X..\n.X.\n.OO'),
        mocker.call('X..\n.X.\nXOO'),
        mocker.call('X.O\n.X.\nXOO'),
        mocker.call('X.O\nXX.\nXOO'),
        mocker.call('Game is finished, X wins')]


def test_o_wins(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 0 1')
    bot.handle_message('O 2 2')
    bot.handle_message('X 0 0')
    bot.handle_message('O 0 2')
    bot.handle_message('X 1 2')
    bot.handle_message('O 2 0')
    bot.handle_message('X 1 1')
    bot.handle_message('O 2 1')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('...\nX..\n...'),
        mocker.call('...\nX..\n..O'),
        mocker.call('X..\nX..\n..O'),
        mocker.call('X..\nX..\nO.O'),
        mocker.call('X..\nX..\nOXO'),
        mocker.call('X.O\nX..\nOXO'),
        mocker.call('X.O\nXX.\nOXO'),
        mocker.call('X.O\nXXO\nOXO'),
        mocker.call('Game is finished, O wins')]


def test_draw(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 0 0')
    bot.handle_message('O 1 1')
    bot.handle_message('X 1 0')
    bot.handle_message('O 2 0')
    bot.handle_message('X 0 2')
    bot.handle_message('O 0 1')
    bot.handle_message('X 2 1')
    bot.handle_message('O 1 2')
    bot.handle_message('X 2 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('X..\n...\n...'),
        mocker.call('X..\n.O.\n...'),
        mocker.call('XX.\n.O.\n...'),
        mocker.call('XXO\n.O.\n...'),
        mocker.call('XXO\n.O.\nX..'),
        mocker.call('XXO\nOO.\nX..'),
        mocker.call('XXO\nOOX\nX..'),
        mocker.call('XXO\nOOX\nXO.'),
        mocker.call('XXO\nOOX\nXOX'),
        mocker.call('Game is finished, draw')]


def test_many_invalid_turns(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('O 1 1')
    bot.handle_message('X 1 1')
    bot.handle_message('X 2 2')
    bot.handle_message('O 0 0')
    bot.handle_message('O 2 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('Invalid turn'),
        mocker.call('...\n.X.\n...'),
        mocker.call('Invalid turn'),
        mocker.call('O..\n.X.\n...'),
        mocker.call('Invalid turn')]


def test_wrong_symbols(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 0 0')
    bot.handle_message('A 1 1')
    bot.handle_message('B 2 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('X..\n...\n...'),
        mocker.call('Invalid turn'),
        mocker.call('Invalid turn')]
