import random
# creating a list from 0 to 100: (persigalvojau)
#numbers = []
#for i in range(101):
#    numbers.append(i)
def guess():
    a = input('Make a guess. ')
    return a

num_to_win = random.randint(1,100)
player_lives = 0

print("Welcome to the Number guessing game!")
print(f"I'm thinking of a number between 1 and 100.")
mode = input("Choose dificulity. Type 'hard' or 'easy'.")

if mode == 'hard':
    player_lives += 5
    print("You have 5 attempts to guess the number.")
else:
    player_lives += 10
    print('You have 10 attempts to guess the number.')
    
win = False

while win == False:    
    if int(guess()) == num_to_win:
        win = True
        print('You guessed the number.')
    else:
        player_lives -= 1
        if player_lives <= 0:
            print('You are out of lives.')
        else:
            print(f'You have {player_lives} attempts left.')                
            if int(guess()) < num_to_win:
                print('Too low.')                       
            elif int(guess()) > num_to_win:
                print('Too high.')       



#while loop till num_to_win == guess, wrong answer: player lives -= 1