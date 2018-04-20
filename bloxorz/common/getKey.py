from bloxorz.common.moves import moves
import click


def getKey():
    k = click.getchar()

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

    elif k == '\n':
        return '\n'

    input()