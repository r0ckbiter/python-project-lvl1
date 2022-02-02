#!/usr/bin/env python

from brain_games.games import brain_even
from brain_games.common_logic import get_games_engine


def main():
    get_games_engine(brain_even)


if __name__ == '__main__':
    main()
