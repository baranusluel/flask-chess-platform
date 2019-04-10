#!/usr/bin/env python3


# coding : utf-8

from flask import Flask, Response, request
import chess, chess.pgn

class Player(object):
    def __init__(self, board):
        self.__current_board = board

    def make_move(self, move):
        raise NotImplementedError()


class Player1(Player):
    def __init__(self, board):
        self.__current_board = board

    def get_board(self):
        return self.__current_board


class Player2(Player):
    def __init__(self, board):
        self.__current_board = board

    def get_board(self):
        return self.__current_board




if __name__ == "__main__":
    start_demo()

