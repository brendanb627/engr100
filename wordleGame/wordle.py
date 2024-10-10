# input
import wordbank_guess
import wordbank_answer
import random
guess_words = wordbank_guess.words
answer_words = wordbank_answer.words

word = random.choice(answer_words)

response = ""
attempts = 0
max_attempts = 6
running = True
words_used = []

print("\033[32mWelcome to WORDLE")
print("\033[0mEnter a 5 letter word")

while running == True:
    user_input = input("\033[0m\033[90minput: \033[0m").lower()
    if user_input == word:
        print("\n\033[32mCorrect! You guessed the word in " + str(attempts + 1) + " guesses!\033[0m\n")
        break
    if len(user_input) != 5:
        print("\033[31mMust be a 5 letter word")
    elif user_input not in guess_words:
        print("\033[31mWord not in word bank")
    elif user_input in words_used:
        print("\033[31mWord already used")
        
    else:
        words_used.append(user_input)
        attempts += 1
        for i in range(len(word)):
            if user_input[i] in word:
                if word[i] == user_input[i]:
                    response += "\033[1m\033[32m" + str(user_input[i])
                    response = response.replace("\033[1m\033[33m" + word[i], "\033[0m" + word[i])
                elif user_input[i] in response:
                    response += "\033[0m" + str(user_input[i])
                else:
                    response += "\033[1m\033[33m" + str(user_input[i])
            else:
                response += "\033[0m" + str(user_input[i])
        print(response)
        response = ""
        if (attempts >= max_attempts):
            print("\n\033[31mGame Over!\033[0m   The word was " + word + '\n')
            break
                    
