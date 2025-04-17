from enum import StrEnum

class GameOptions(StrEnum):
    Rock = 'R',
    Paper = 'P'
    Sissors = 'S'

game_option = input("Select a game option: ")
print(GameOptions(game_option).name)
