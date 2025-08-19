from gameparts import Board
from gameparts.exceptions import BoardIndexError, CellOccupiedError


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Move make the {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.board_size:
                    raise BoardIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.board_size:
                    raise BoardIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except BoardIndexError:
                print(f'The value must be non-negative and less than {game.board_size}')
                print('Enter other coordinates')
                continue
            except CellOccupiedError:
                print('Cell is busy')
                print('Enter other coordinates')
            except ValueError:
                print('You can not enter letters. Only numbers')
                print('Enter other coordinates')
                continue
            except Exception as e:
                print(f'An error occurred: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            result = f'Winner {current_player}!'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Draw!'
            print(result)
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
