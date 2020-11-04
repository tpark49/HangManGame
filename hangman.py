import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for i in secret_word: 
        if i in letters_guessed: 
            continue
        else: 
            return False 
    return True 


def get_guessed_word(secret_word, letters_guessed):
  
    answer = ""
    for i in secret_word: 
        if i in letters_guessed: 
            answer+=i
        else: 
            answer+="_"
    return answer



def get_available_letters(letters_guessed):


    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_word = list(string.ascii_lowercase)
    for i in letters_guessed: 
        if i in list_word: 
            list_word.remove(i)
        else: 
            continue 
    return "".join(list_word)
    
    
    

def hangman(secret_word):
    
    
 

    guesses = 6
    warning = 3
    letters_guessed = []
    guessed_before = False
    
    print("Welcome to hangman. You will have 6 guesses to guess the correct word....Good luck")
    print("The secret word has " + str(len(secret_word)) + " letters")
    
    
    while guesses >0: 
        word_sofar = get_guessed_word(secret_word, letters_guessed)
        #get input from user 
        user_input = input("Please enter your guess?")
        
        if len(user_input)<2:
            #check if user guessed this word before
            if user_input in letters_guessed:
                guessed_before = True 
                if warning == 1:
                    print("you've run out of warnings, we will deduct a guess")
                    guesses -=1
                else: 
                    warning-=1
            else:
                guessed_before = False 
        else: 
            if user_input == secret_word: 
                print("Congrats, you won!")
                return 
            else: 
                guesses-=1
            
        
        #add new guess to letters_gussed list 
        letters_guessed.append(user_input)
    
        
        #check if user got the correct word 
        if is_word_guessed(secret_word, letters_guessed): 
            print("congratulations you won!")
            return 
        else:
            #check if user is asking for hint 
            if user_input == "*":
                pass
            else: 
                guesses -=1
        
        
        
        #if it hasn't been guessed, is it correct? 
        word_sofar = get_guessed_word(secret_word, letters_guessed)
        if guessed_before:
            print("the letter has been guessed before: " + str(word_sofar))
        else: 
            if user_input in secret_word:
                print("Good job! You've guessed: " + str(word_sofar))
                print("you have this many guesses left: " + str(guesses))
            else: 
                print("try again! You've guessed: " + str(word_sofar))
                print("you have this many guesses left: " + str(guesses))
                
                
        #give hint if * was entered 
        hint = []
        if user_input == "*":
            wordlist = load_words()
            for i in wordlist: 
                if len(secret_word) == len(i) and match_with_gaps(word_sofar, i):
                    hint.append(i)
            print(hint)
    
                
    print("Sorry you have lost...!")
    print("The word was..." + secret_word)
    return 
                



def match_with_gaps(my_word, other_word):

    for i in range(len(my_word)):
        if my_word[i] == "_" or my_word[i] == other_word[i]:
            continue 
        else: 
            return False 
    return True 




if __name__ == "__main__":
        
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
