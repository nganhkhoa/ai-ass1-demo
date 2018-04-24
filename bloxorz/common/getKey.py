from bloxorz.common.moves import moves
import click
from platform import system


def getKey():
    k = click.getchar()

    if system() == "Linux":
        if k == '\033[A':
            return moves.up
        elif k == '\033[B':
            return moves.down
        elif k == '\033[C':
            return moves.right
        elif k == '\033[D':
            return moves.left
        elif k == ' ':
            return ' '
        elif ord(k) == 13:
            return '\n'

        elif ord(k) == 3:
            raise KeyboardInterrupt

        # linux needs this
        # input()

    elif system() == "Windows":
        if ord(k) == 72:
            return moves.up
        elif ord(k) == 80:
            return moves.down
        elif ord(k) == 77:
            return moves.right
        elif ord(k) == 75:
            return moves.left
        elif k == ' ':
            return ' '
        elif ord(k) == 13:
            return '\n'

    elif system() == "Darwin":
        if k == ' ':
            return ' '
        elif ord(k) == 13:
            return '\n'
