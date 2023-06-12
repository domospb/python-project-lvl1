#!/usr/bin/env python3

from brain_games.game_engine import play
from brain_games.games import progression


def main():
    """Start the "Brain-Even Game"."""
    play(progression)


if __name__ == '__main__':
    main()
