import random

MAX_GUESSES = 5
START, END = 1, 20

def get_random_number():

    return random.randint(START, END)

class Game:

    def __init__(self):
        self.guesses = set()
        self.answer = get_random_number()
        self.win = False

    def guess(self):
        guess = input(f'Guess a number between {START} and {END}: ')
        if not guess:
            raise ValueError('Please enter a number')

        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END + 1):
            raise ValueError('Number not in range')

        if guess in self._guesses:
            raise ValueError('Already guessed')

        self.guesses.add(guess)
        return guess

    def _validate_guess(self, guess):

        if guess == self.answer:
            print(f'{guess} is correct!')
            return True

        else:
            high_or_low = 'low' if guess < self.answer else 'high'
            print(f'{guess} is too {high_or_low}')
            return False

    @property
    def num_guesses(self):
        return len(self.guesses)

    def __call__(self):
        while len(self.guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and "guess" or "guesses"
                print(f'It took you {self.num_guesses} {guess_str}')

    if __name__ == '__main__':
        game = Game()
        game()




