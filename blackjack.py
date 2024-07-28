'''This program runs a simplified version of Blackjack.'''

#Importing modules random and math
import random
import math

#------------ Definitions of Functions ------------

#Defining a function called check_username(username) to check if the entered username follows all requirements
def check_username(username):

  #Splits and joins the name to make sure that usernames that have a space in between can be a username as well
  modifiedName = username.split()
  modifiedName = "".join(modifiedName)

  #If the username is longer than 20 characters, if it does not have at least 2 characters, and if it contains any numbers or illegal characters, the program will ask the user to enter another username
  while len(username) > 20 or len(username) < 2 or modifiedName.isalpha() == False:
    if len(username) > 20:
      print("\n\n\033[31m" + "-" * 48 + "\nYour username cannot be more than 20 characters!\n" + "-" * 48 + "\033[39m")
    elif len(username) == 1:
      print("\n\n\033[31m" + "-" * 44 + "\nYour username must be at least 2 characters!\n" + "-" * 44 + "\033[39m")
    elif modifiedName.isalpha() == False:
      print("\n\n\033[31m" + "-" * 35 + "\nYour username must be only letters!\n" + "-" * 35 + "\033[39m")
    username = input("\n\nEnter your username: ")
    modifiedName = username.split()
    modifiedName = "".join(modifiedName)

  #When the requirements are fulfilled, the function will return the username back to the main program
  return username

#Defining a function called signin(username) to store a username's data if it does not already exist in the .txt file
def signin(username):
  balance = 1000
  content = open("users.txt", "a")
  data = [username, str(balance)]
  content.write(" ".join(data) + "\n")
  content.close()
  return balance

#Defining a function called login(username) to recover data from an existing username and return the balance back to the main program
def login(username):
  content = open("users.txt")
  for line in content:
    if username in line:
      name, savedBal = line.split()
  username = name
  balance = int(savedBal)
  content.close()
  return balance

#Defining a function called instructionsPage() to print out the instructions of the game
def instructionsPage():
  print("\n\n\n" + "-" * 36 + "\n\t\t\tINSTRUCTIONS\n" + "~" * 36)

  #After reading each block of information, the user can press enter to continue reading
  enter1 = input("Welcome to the simplified version of Blackjack!\n\n (Enter to continue)")
  enter2 = input("\n\nThis game uses a conventional deck of cards that consists of 52 cards and the 4 suits: clubs, hearts, diamonds, and spades.\n\n (Enter to continue)") 
  enter3 = input("\n\nThe objective of the game is to beat the dealer by receiving a count (sum of points) as close to 21 as possible without going over, also known as busting.\n\n (Enter to continue)") 
  enter4 = input("\n\nThe game starts with the dealer giving out one card to themselves and one card to the player. The player has two choices: stand (not ask for another card and stick with the cards they have) or hit (ask for another card to get a count closer to 21).\n\n (Enter to continue)")
  enter5 = input("\n\nIn this program, the dealer can hit whenever he wants to, even if he chose to stand in a previous turn. \n\n (Enter to continue)")
  enter6 = input("\n\nEvery card has its own value in points.\nFor example, an 8 of hearts is worth 8 points, while a Jack, Queen or King is worth 10 points. However, the Ace card has two values in two different scenarios in the game. \n\nThe Ace card is worth 11 points, though if it results in a bust, the card will be worth one point instead. \n\n (Enter to continue)") 
  enter7 = input("\n\nWhen you lose, you lose all the money that you bet on the game. Contrastingly, when you win, you will win a randomized percentage, from 75% to 300%, of your wager.\n\n\t\tRemember to always have fun!\n" + "-" * 44 + "\n\n (Enter to exit)")

#Defining a function called check_bet(balance) to check if the amount of money the user wants to bet follows the requirements
def check_bet(balance):
  while True:
    try:
      bet = int(input("\nEnter how much you want to bet: "))
      #The program will keep asking the user to enter an amount of money to bet if they enter too much money or they bet no money or a negative number
      while bet > (balance / 4 * 3) or bet <= 0:
        if bet == balance:
          print("\n\n\033[31m" + "-" * 56 + "\nYou can't bet all your money! You're gonna become broke!\n" + "-" * 56 + "\033[39m")
        elif bet > balance:
          print("\n\n\033[31m" + "-" * 58 + "\nYou can't bet more than you have! Are you trying to cheat?\n" + "-" * 58 + "\033[39m")
        elif bet > (balance / 4 * 3):
          print("\n\n\033[31m" + "-" * 69 + "\nYou can't bet more than 75% of your money! You're gonna become broke!\n" + "-" * 69 + "\033[39m")
        elif bet == 0:
          print("\n\n\033[31m" + "-" * 32 + "\nYou can't bet nothing you dumbo.\n" + "-" * 32 + "\033[39m")
        elif bet < 0:
          print("\n\n" + "-" * 52 + "\nWhy are you trying to bet negative amounts of money?\n" + "-" * 52)
        bet = int(input("\n\nEnter how much you want to bet: "))
      return bet
    except ValueError:
      print("\n\n\033[31m" + "-" * 27 + "\nPlease enter a whole number\n" + "-" * 27 + "\n\033[39m")

#Defining a function called dealer_game to run and display the dealer's side of the game
def dealer_game(dealerCount, dealerCards, listCards, listVal, playerCount, playerCards, suits):
  print("\n\n------\nDEALER\n------")

  #This if statement will only run in a very specific situation during the game. If the dealer has a count greater than 17 and the player has a count greater than the dealer, the player will obviously stand. Therefore, the dealer can only hit because there is still a small chance that they might tie or even win
  if dealerCount > 16 and playerCount - dealerCount > 0:
    x = random.choice(listCards)
    dealerCard = random.choice(suits) + x
    while dealerCard in dealerCards or dealerCard in playerCards:
      x = random.choice(listCards)
      dealerCard = random.choice(suits) + x
    dealerCards.append(dealerCard)
    print("Cards:",str(" ".join(dealerCards)))

    #The program will give the Ace card a value of 11 points if the dealer's count will not go over 21 points. If the Ace card is given 11 points and the dealer's count will go over 21 points, the Ace card will be worth 1 point instead.
    if x == "A":
      if dealerCount + 11 > 21:
        dealerCount += 1
        print("Count:",dealerCount)
      else:
        dealerCount += 11
        print("Count:",dealerCount)
    else:
      dealerCount += listVal[listCards.index(x)]
      print("Count:",dealerCount)
    return dealerCount, dealerCards
  elif dealerCount > 16:
    print("Cards:",str(" ".join(dealerCards)))
    print("Count:",dealerCount)
    return dealerCount, dealerCards
  else:
    x = random.choice(listCards)
    dealerCard = random.choice(suits) + x
    while dealerCard in dealerCards or dealerCard in playerCards:
      x = random.choice(listCards)
      dealerCard = random.choice(suits) + x 
    dealerCards.append(dealerCard)
    print("Cards:",str(" ".join(dealerCards)))
    if x == "A":
      if dealerCount + 11 > 21:
        dealerCount += 1
        print("Count:",dealerCount)
      else:
        dealerCount += 11
        print("Count:",dealerCount)
    else:
      dealerCount += listVal[listCards.index(x)]
      print("Count:",dealerCount)
  return dealerCount, dealerCards

#Defining a function called player_game that runs and displays the player side of the game.
def player_game(playerCount, playerCards, listCards, listVal, bet, username, dealerCards, suits):
  print("\n\n" + "-" * len(username) + "\n" + username + "\n" + "-" * len(username))
  x = random.choice(listCards)
  playerCard = random.choice(suits) + x
  while playerCard in dealerCards or playerCard in playerCards:
    x = random.choice(listCards)
    playerCard = random.choice(suits) + x
  playerCards.append(playerCard)
  print("Cards:",str(" ".join(playerCards)))

  #The program will give the Ace card a value of 11 points if the player's count will not go over 21 points. If the Ace card is given 11 points and the player's count will go over 21 points, the Ace card will be worth 1 point instead.
  if x == "A":
    if playerCount + 11 > 21:
      playerCount += 1
      print("Count:",playerCount)
      print("Wager: $" + str(bet))
    else:
      playerCount += 11
      print("Count:",playerCount)
      print("Wager: $" + str(bet))
  else:
    playerCount += listVal[listCards.index(x)]
    print("Count:",playerCount)    
    print("Wager: $" + str(bet))
  return playerCount, playerCards

#Defining a function called check_count to determine if the player loses, ties, or wins the game against the dealer. The randomized percentage between 75% and 300% will be generated if the player wins their game. The money will be given to the player if they win.
def check_count(dealerCount, playerCount, balance, bet):

  #If both the dealer and the player bust (go over 21), the game will result in a tie and the money will be returned to the player.
  if dealerCount > 21 and playerCount > 21:
    print("\n\nIt's a tie! You and the dealer both busted!\nYour money is returned back to you.")
    print("\nYour balance: $" + str(balance))
    return balance

  #If the player busts (goes over 21), the game will result in a loss and the money that the player bet on the game will be subtracted from their balance.
  elif dealerCount <= 21 and playerCount > 21:
    print("\n\nYou busted! You lose your wager.")
    print("\n\033[31mYou lost $" + str(bet) + "\033[39m")
    balance = balance - bet
    print("\nYour balance: $" + str(balance))
    return balance

  #If the dealer busts (goes over 21), the game wil result in a win and the player will be given a randomized percentage between 75% and 300% of the money they bet on the game.
  elif dealerCount > 21 and playerCount <= 21:
    print("\n\n\033[32mYou won! The dealer busted!\033[39m")
    winPercentage = random.randint(75, 300)
    print("\nPercentage of wager:",str(winPercentage) + "%")
    print("Money won: $" + str(math.ceil(bet * winPercentage / 100)))
    balance = math.ceil(balance + ((bet * winPercentage) / 100))
    print("\nYour balance: $" + str(balance))
    return balance

  #If both the dealer and the player achieve a count of 21, the game will result in a tie and the money will be returned to the player.
  elif dealerCount == 21 and playerCount == 21:
    print("\n\nIt's a tie! You and the dealer both achieved a count of 21!\nYour money is returned back to you.")
    print("\nYour balance: $" + str(balance))
    return balance

    #If the dealer achieves a count of 21 before the player, the game will result in a loss and the money that the player bet on the game will be subtracted from their balance.
  elif dealerCount == 21 and playerCount != 21:
    print("\n\nThe dealer achieved a count of 21! You lose your wager.")
    print("\n\033[31mYou lost $" + str(bet) + "\033[39m")
    balance = balance - bet
    print("\nYour balance: $" + str(balance))
    return balance

  #If the player achieves a count of 21 before the dealer, the game wil result in a win and the player will be given a randomized percentage between 75% and 300% of the money they bet on the game.
  elif dealerCount != 21 and playerCount == 21:
    print("\n\n\033[32mYou won! You achieved a count of 21!\033[39m")
    winPercentage = random.randint(75, 300)
    print("\nPercentage of wager:",str(winPercentage) + "%")
    print("Money won: $" + str(math.ceil(bet * winPercentage / 100)))
    balance = math.ceil(balance + ((bet * winPercentage) / 100))
    print("\nYour balance: $" + str(balance))
    return balance
    
  #If both the dealer and the player end off with the same count, the game will result in a tie and the money will be returned to the player.
  elif 21 - dealerCount == 21 - playerCount:
    print("\n\nIt's a tie!\nYour money is returned back to you.")
    print("\nYour balance: $" + str(balance))
    return balance

    #If the dealer achieves a count closer to 21 than the player, the game will result in a loss and the money that the player bet on the game will be subtracted from their balance.
  elif 21 - dealerCount < 21 - playerCount:
    print("\n\nThe dealer achieved a count closer to 21 than you! You lose your wager.")
    print("\n\033[31mYou lost $" + str(bet) + "\033[39m")
    balance = balance - bet
    print("\nYour balance: $" + str(balance))
    return balance

  #If the player achieves a count closer to 21 than the dealer, the game wil result in a win and the player will be given a randomized percentage between 75% and 300% of the money they bet on the game.
  elif 21 - dealerCount > 21 - playerCount:
    print("\n\n\033[32mYou won! You achieved a count closer to 21!\033[39m")
    winPercentage = random.randint(75, 300)
    print("\nPercentage of wager:",str(winPercentage) + "%")
    print("Money won: $" + str(math.ceil(bet * winPercentage / 100)))
    balance = math.ceil(balance + ((bet * winPercentage) / 100))
    print("\nYour balance: $" + str(balance))
    return balance  

#Defining a function called game to run the entire game of Blackjack. It includes the list of the dealer's cards, the list of the player's cards, the symbols for the suits of cards, the names of the cards, the values of the cards, and the counts of the dealer and the player.
def game(username, balance):
  dealerCards = []
  playerCards = []
  suits = ['\033[31m♥\033[39m','\033[31m♦\033[39m','\033[30m♣\033[39m','\033[30m♠\033[39m']
  listCards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  listVal = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  dealerCount = 0
  playerCount = 0

  #Checks if the amount of money the user wagered follows the requirements.
  bet = check_bet(balance)

  #The dealer's count, the player's count, the dealer's cards, and the player's cards will be reassigned with the return values from the functions dealer_game and player_game.
  dealerData = dealer_game(dealerCount, dealerCards, listCards, listVal, playerCount, playerCards, suits)
  playerData = player_game(playerCount, playerCards, listCards, listVal, bet, username, dealerCards, suits)
  dealerCount = dealerData[0]
  playerCount = playerData[0]
  dealerCards = dealerData[1]
  playerCards = playerData[1]

  #The game will continue to run if the dealer and the player do not have a count of 21 or more.
  while dealerCount < 21 and playerCount < 21: 
    game_option = input("\n\nOptions (Hit/Stand): ")
    while game_option.lower() != "hit" and game_option.lower() != "stand":
      print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
      game_option = input("\nOptions (Hit/Stand): ")

    #If the player chooses the option "hit", the program will call the dealer_game and player_game functions again and reassign the dealer's count, the player's count, the dealer's cards, and the player's cards.
    if game_option.lower() == "hit":
      dealerData = dealer_game(dealerCount, dealerCards, listCards, listVal, playerCount, playerCards, suits)
      playerData = player_game(playerCount, playerCards, listCards, listVal, bet, username, dealerCards, suits)
      dealerCount = dealerData[0]
      playerCount = playerData[0]
      dealerCards = dealerData[1]
      playerCards = playerData[1]

    #If the user chooses the option "stand", the program will call the function dealer_game but display the same cards and count of the player.
    elif game_option.lower() == "stand":
      while dealerCount <= 16:
        dealerData = dealer_game(dealerCount, dealerCards, listCards, listVal, playerCount, playerCards, suits)
        dealerCount = dealerData[0]
        dealerCards = dealerData[1]
        print("\n\n" + "-" * len(username) + "\n" + username + "\n" + "-" * len(username))
        print("Cards:",str(" ".join(playerCards)))
        print("Count:",playerCount)
        print("Wager: $" + str(bet))

        #This while loop will only run in a very specific situation during the game. If the dealer has a count greater than 17 and the player has a count greater than the dealer, the player will obviously stand. Therefore, the dealer can only hit because there is still a small chance that they might tie or even win
      while dealerCount > 16 and playerCount - dealerCount > 0:
        dealerData = dealer_game(dealerCount, dealerCards, listCards, listVal, playerCount, playerCards, suits)
        dealerCount = dealerData[0]
        dealerCards = dealerData[1]
        print("\n\n" + "-" * len(username) + "\n" + username + "\n" + "-" * len(username))
        print("Cards:",str(" ".join(playerCards)))
        print("Count:",playerCount)
        print("Wager: $" + str(bet))

#The balance of the user will be reassigned to the return value of the function check_count, which determines if the player loses, ties, or wins against the dealer.
      else:
        balance = check_count(dealerCount, playerCount, balance, bet)
        return balance
  balance = check_count(dealerCount, playerCount, balance, bet)
  return balance

#Defining a function called showBal to display the balance of the user. If the balance is equal to 1, the program will print a special line on the console.
def showBal(balance):
  if balance == 1:
    print("\n\033[31m" + "-" * 34 + "\nYou already know you only have $1.\n" + "-" * 34 + "\033[39m")
    enter = input("\n(Enter to return)")
  else:
    print("\n\033[32m-------------\nYour balance: $" + str(balance) + "\n-------------\033[39m")
    enter = input("\n(Enter to return)")

#Defining a function called userInput to run the main menu of the program. It asks the user what they would like to do and will run accordingly.
def userInput(username, balance):
  choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")
  while True:

    #The program will redirect the user to the instructions page if the user enters "i".
    if choice.lower() == "i":
      instructionsPage()
      choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")
    elif choice.lower() == "p":

      #The program will prevent the user to gamble if the user only has a balance of 1.
      if balance == 1:
        print("\n\n\033[31m" + "-" * 56 + "\nYou only have $1! You can't gamble with only one dollar!\n" + "-" * 56 + "\033[39m")
        choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")
        continue
      else:
        pass

      #The game of Blackjack will continue to run if the user wants to continue to play by responding "y" for yes
      playerContinue = "y"
      while playerContinue.lower() == "y":
        balance = game(username, balance)

        #When the user's balance reaches $1 after losing a game of Blackjack, the program will print a special line and redirect them to the main menu where they are asked what they would like to do.
        if balance == 1:
          print("\n\n\033[31m" + "-" * 73 + "\nYou only have $1! This is why you don't play Blackjack! You're broke now!\n" + "-" * 73 + "\033[39m")

          #Stores the balance in the .txt file
          content = open("users.txt")
          for line in content:
            if username in line:
              name, savedBal = line.split()
              replaceData = open("users.txt").read()
              replaceData = replaceData.replace(savedBal, str(balance))
              content = open("users.txt", "w")
              content.write(replaceData)
            else:
              continue
            content.close()
          break
        else:
          
          #Stores the balance in the .txt file
          content = open("users.txt")
          for line in content:
            if username in line:
              name, savedBal = line.split()
              replaceData = open("users.txt").read()
              replaceData = replaceData.replace(savedBal, str(balance))
              content = open("users.txt", "w")
              content.write(replaceData)
            else:
              continue
          content.close()

          #Asks the user if they would like to continue playing the game of Blackjack.
          playerContinue = input("\n\nDo you want to keep playing? (y for yes/n for no): ")
          while playerContinue.lower() != "y" and playerContinue.lower() != "n":
            print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
            playerContinue = input("\nDo you want to keep playing? (y for yes/n for no): ")  
          if playerContinue.lower() == "y":
            continue
          else:
            break
      choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")
      continue

    #Calls the showBal function if the user enters "b"
    elif choice.lower() == "b":
      showBal(balance)
      choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")

    #If the user enters "l", the program will ask the user again for confirmation.
    elif choice.lower() == "l":
      question = input("\nAre you sure you want to log out? (y for yes/n for no): ")

      #The program ill keep asking the user to enter a valid option if they do not respond to the question.
      while question.lower() != "n" and question.lower() != "y":
        print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
        question = input("\nAre you sure you want to log out? (y for yes/n for no): ")

      #If the user does not want to log out, the program will ask them would they would like to do, which runs the entire while loop of the userInput function again
      if question.lower() == "n":
        choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")

      #If the user responds with "y", the program will return True back to the main program where the user will be prompted to enter a username.
      elif question.lower() == "y":
        return True

    #If the user enters "e", the program will ask again for confirmation.
    elif choice.lower() == "e":
      question = input("\nAre you sure you want to exit the game? (y for yes/n for no): ")

      #The program will keep asking the user to respond to the question if the user does not respond with a valid option.
      while question.lower() != "n" and question.lower() != "y":
        print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
        question = input("\nAre you sure you want to exit the game? (y for yes/n for no):")

      #If the user responds with "n", the program will ask them would they would like to do, which runs the entire while loop of the userInput function again 
      if question.lower() == "n":
        choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")

      #If the user wants to exit the game and responds with "y", the program will return False back to the main program of the code, which breaks the entire program.
      elif question.lower() == "y":
        return False
    else:
      print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
      choice = input("\n" + "-" * 9 + "\nMAIN MENU\n" + "-" * 9 + "\n\n\033[35mWhat would you like to do?\033[39m\n\ni for instructions\np to play\nb to view balance\nl to logout\ne to exit the game\n\nChoice:  ")

#------------------- Main Program -------------------

#Creates a new .txt file named "users.txt"
content = open("users.txt", "a")

#This while loop runs the entire program.
while True:
  print("\n\n\033[32m---------------------------------\n\t\t\tBLACKJACK\n---------------------------------\033[39m")

  #Asks the user to enter a username and checks it by calling the check_username function
  username = input("\nEnter your username: ")
  username = check_username(username)

  #If the username is in the .txt file, the program will find and retrieve the data of that existing username by calling the login function
  if username in open("users.txt").read():
    balance = login(username)
    print("\n\n\n\033[33mWelcome to Blackjack!\n---------------------\033[39m")
    print("\n\033[36mHappy to see you back",username + "!\033[39m")

    #If the user wanted to exit the game, the userInput function would have returned with False. The program will send a farewell message and stop the entire program.
    if userInput(username, balance) == False:
      print("\n\nSad to see you go :(")
      break
    else:
      continue

  #If the username is not in the .txt file, the program will add the username into the file and give the new username a default balance of $1000 by calling the signin function.
  else:
    balance = signin(username)
    print("\n\n\n\033[33mWelcome to Blackjack!\n---------------------\033[39m")
    print("\nHello new user,",username + "!")

    #If the username is new, the program will ask the user if they know how to play Blackjack.
    instructions = input("Do you know how to play Blackjack? (y for yes/n for no): ")
    while instructions.lower() != "n" and instructions.lower() != "y":
      print("\n\033[31m" + "-" * 27 + "\nPlease enter a valid option\n" + "-" * 27 + "\n\033[39m")
      instructions = input("Do you know how to play Blackjack? (y for yes/n for no): ")

    #If the new user does not know how to play Blackjack, the program will redirect the user to the instructions page by calling the instructionsPage function.
    if instructions.lower() == "n":
        instructionsPage()

        #If the user wanted to exit the game, the userInput function would have returned with False. The program will send a farewell message and stop the entire program.
        if userInput(username, balance) == False:
          print("\n\nSad to see you go :(")
          break
        else:
          continue
    elif instructions.lower() == "y":

        #If the user wanted to exit the game, the userInput function would have returned with False. The program will send a farewell message and stop the entire program.
        if userInput(username, balance) == False:
          print("\n\nSad to see you go :(")
          break
        else:
          continue
