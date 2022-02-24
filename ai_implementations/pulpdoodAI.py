import random
from re import I

from WordleAI import LetterInformation, WordleAI


class PulpDood(WordleAI):

    def guess(self, guess_history):
        # print("\n")
        if(len(guess_history) == 0):
            return random.choice(self.words)

        words = []
        results = []
        correct_letters = ["","","","",""]
        present_letters = [] 
        incorrect_letters = []
        
        for previous_guess in guess_history:
            word = previous_guess[0]
            result = previous_guess[1]

            words.append(word)
            results.append(result)

            for index, letter in enumerate(word):
                if(result[index] == LetterInformation.CORRECT):
                    correct_letters[index] = letter
                if(result[index] == LetterInformation.PRESENT):
                    present_letters.append(letter)
                if(result[index] == LetterInformation.NOT_PRESENT):
                    incorrect_letters.append(letter)

        candidate_words = []
        skip_word = 0

        for legal_word in self.words:
            skip_word = 0
            for index, letter in enumerate(present_letters):
                if letter not in legal_word:
                    skip_word = 1
                    break

            for index, letter in enumerate(correct_letters):
                if legal_word[index] != correct_letters[index] and correct_letters[index] != "":
                    skip_word = 1
                    break

            for index, letter in enumerate(legal_word):
                if letter in incorrect_letters:
                    skip_word = 1
                    break

            if skip_word == 0:
                candidate_words.append(legal_word)

        # print(random.choice(candidate_words))
        return random.choice(candidate_words)

    def get_author(self):
        return "pulpdood"


# find all words that have correct letter in the index
# and does not contain incorrect letters
# and includes present letters in position not in index
