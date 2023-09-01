import random

myCards = []
dealersCards = []
cards = ["A", 2,3,4,5,6,7,8,9,10,"J","Q","K"]
cardValues={
  "A":11,
  2:2, 3:3, 4:4,5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
  "J":10,
  "Q":10,
  "K":10
}
playersValue = 0
dealersValue = 0
def hitPlayer():
  myCards.append(random.choice(cards))
def hitDealer():
  dealersCards.append(random.choice(cards))
def calculateScore():
  global playersValue
  global dealersValue
  playersCardValue =0
  dealersCardValue =0
  for cards in myCards:
    playersCardValue += cardValues[cards]
  for cards in myCards:
    if cards == "A" and playersCardValue >21:
      playersCardValue -= 10
  playersValue = playersCardValue

  for cards in dealersCards:
    dealersCardValue += cardValues[cards]
  for cards in myCards:
    if cards == "A" and dealersCardValue >21:
      dealersCardValue -= 10
  dealersValue = dealersCardValue


#start of game
def blackJack():
    global playersValue
    global dealersValue
    global myCards
    global dealersCards
    hitPlayer()
    hitPlayer()
    hitDealer()
    hitDealer()
    calculateScore()
    print(f"Your cards: {myCards}")
    print(f"Your Total: {playersValue}")
    print(f"Dealers cards: {dealersCards}")
    print(f"Dealers Total: {dealersValue}")

    keepPlaying = True

    while keepPlaying:
      option = input("Type 'h' to hit and 's' to stand.: ").lower()
      if option.lower() == 'h':
        hitPlayer()
        print(f"Your cards: {myCards}")
        calculateScore()
        print(f"Your Total: {playersValue}")
        print(f"Dealers cards: {dealersCards}")
        print(f"Dealers Total: {dealersValue}")
        #case: bust / lose
        if playersValue > 21:
          #call next game
          print("You busted :(")
          keepPlaying = False
        
      else: #player is standing
        print(f"Your cards: {myCards}")
        print(f"Your Total: {playersValue}")
        #After players stands, dealers starts playing
        while dealersValue <= 16:
          hitDealer()
          calculateScore()
        print(f"Dealers Total: {dealersValue}")
        print(f"Dealers cards: {dealersCards}")
        #Deciding winner
        if playersValue > dealersValue or dealersValue > 21:
          print("You Win!")
        elif playersValue == dealersValue:
          print("It's a draw")
        else: print("You lose :(")
        keepPlaying = False
    #reset players nad dealers hands for enxt gmae
    myCards = []
    dealersCards = []
    playersValue = 0
    dealersValue = 0
    response = input("Do you want to play another game?: ").lower()
    if response == "yes" or response == "y": 
      blackJack()


blackJack()
    
