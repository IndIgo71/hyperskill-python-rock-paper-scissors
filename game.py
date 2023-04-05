import random
import os


class Game:
    @staticmethod
    def __get_rating(name):
        filename = 'rating.txt'
        if os.path.exists(filename):
            with open('rating.txt', 'r') as file:
                ratings = {k: int(v) for k, v in (line.split() for line in file.readlines())}
            return ratings.get(name, 0)
        else:
            return 0

    @staticmethod
    def get_rules(options):
        if len(options) == 0:
            return {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        options = list(options.split(','))
        rules = {option: [] for option in options}
        size = len(rules)

        for option in rules:
            pos = options.index(option)
            if pos + (size - 1) // 2 < size:
                rules[option] = options[pos + 1: pos + 1 + (size // 2)]
            else:
                rules[option] = options[pos + 1:] + options[: pos + 1 + (size // 2) - size]
        return rules

    def start(self):
        player_name = input('Enter your name: ')
        print(f'Hello, {player_name}')
        score = self.__get_rating(player_name)
        rules = self.get_rules(input())
        print("Okay, let's start")
        while True:
            user_choice = input()

            if user_choice == '!exit':
                print('Bye!')
                break
            elif user_choice == '!rating':
                print(f'Your rating: {score}')
            else:
                if user_choice in rules:
                    pc_choice = random.choice(list(rules.keys()))
                    if user_choice == pc_choice:
                        score += 50
                        print(f'There is a draw ({user_choice})')
                    elif pc_choice in rules[user_choice]:
                        print(f'Sorry, but the computer chose {pc_choice}')
                    elif user_choice in rules[pc_choice]:
                        score += 100
                        print(f'Well done. The computer chose {pc_choice} and failed')
                else:
                    print('Invalid input')
                    continue


if __name__ == '__main__':
    game = Game()
    game.start()
