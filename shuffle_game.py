from random import shuffle

list = ['' ,'' ,'0']

def shuffle_list(l):
  shuffle(l)
  return l

def player_guess():
  guess = ''
  while guess not in ['0','1','2']:
    guess = input('print your guess:-  ')

  return int(guess)


def check_guess(list,guess):
  if list[guess] =='0':
    print('correct.')
  else:
    print('wrong')
    print(list)


sl = shuffle_list(list)

guess = player_guess()

print(check_guess(sl,guess))
