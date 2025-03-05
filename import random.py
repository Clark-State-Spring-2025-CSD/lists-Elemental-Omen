import random

PlayerOne = []
PlayerTwo = []

PlayerOneWins = 0
PlayerTwoWins = 0
Ties = 0


for i in range(10):
    PlayerOne.append(random.randint(1,50))
    PlayerTwo.append(random.randint(1,50))
    
print(f"Player One = {PlayerOne}")
print(f"Player Two = {PlayerTwo}")

for i in range(10):
    if PlayerOne[i] > PlayerTwo[i]:
     PlayerOneWins += 1
    elif PlayerTwo[i] > PlayerOne[i]:
     PlayerTwoWins += 1
    else:
        PlayerOne[i] == PlayerTwo[i]
        Ties += 1
    
print(f"Player one won {PlayerOneWins} times")
print(f"Player two won {PlayerTwoWins} times")
print(f"there were {Ties} ties")

print(f"Player one's highest number is {max(PlayerOne)} at index {PlayerOne.index(max(PlayerOne))}")
print(f"Player two's highest number is {max(PlayerTwo)} at index {PlayerTwo.index(max(PlayerTwo))}")
    