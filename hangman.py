import random

def load_word():

  wordList = ["hello",
              "world",
              "dog",
              "cow",
              "google",
              "tesla",
              "vanguard",
              ]

  word = random.choice(wordList)

  word = word.upper()

  return word

def start_round(loaded_word):

  hidden_word = "_" * len(loaded_word)

  print("H A N G M A N")
  print("\n")
  print(hidden_word)

  guessed = False
  
  tries = 5

  guessed_letters = []
  guessed_words = []

  while not guessed and tries > 0:
    
    print("")
    guess = input("Guess a letter or word: ").upper()

    if guess.isalpha() and len(guess) == 1:

      if guess in guessed_letters:
        print("You already guessed:", guess)

      elif guess not in loaded_word:

        print(guess, "is not in the word")
        tries -= 1
        print("Guesses Left: " + str(tries))

        guessed_letters.append(guess)

      else:

        print(guess, "is in the word")

        guessed_letters.append(guess)

        word_as_list = list(hidden_word)

        indices = [i for i, letter in enumerate(loaded_word) if letter == guess]
        
        for index in indices:
          word_as_list[index] = guess

        hidden_word = "".join(word_as_list)

        if "_" not in hidden_word:
          print("")
          print("You guessed correctly!")
          guessed = True

    elif guess.isalpha():

      if guess in guessed_words:
        print("You already guessed:", guess)

      elif guess != loaded_word:

          print(guess, "is not the word")
          tries -= 1
          guessed_words.append(guess)
          print("Guesses Left: " + str(tries))
          
      else:

        guessed = True
        print("")
        hidden_word = loaded_word
        print("You guessed correctly!")


    else:
      print("Invalid guess")

    print("")   
    print(hidden_word)

loaded_word = load_word()

start_round(loaded_word)

while input("Restart Game? Y/N:").upper() == "Y":

  loaded_word = load_word()

  start_round(loaded_word)
