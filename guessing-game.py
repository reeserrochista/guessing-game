from random import randint
n = randint(0, 5)
print('-=-' * 20)
print('I am thinking of a number between 0 and 5. Try to guess!')
print('-=-' * 20)
print('I will think of...') 
print('-=-' * 20)
player = int(input('what number did I thought?'))
print('-=-' * 20)
if player == n:
    print('You win, that was my number!')
else:
    print('You lost! I thought of the number {}'.format(n))

