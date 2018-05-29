PICS = ['''

  _____
  |   |
      |
      |
      |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
      |
      |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
  |   |
      |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
 /|   |
      |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
 /|\  |
      |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
 /|\  |
 /    |
      |
~~~~~~~~''','''

  _____
  |   |
  O   |
 /|\  |
 / \  |
      |
~~~~~~~~''']

keywords = 'lyceum human king guitar music chair case pencil table memes book apple phone computer program boulevard dream university physics mathematics algebra analysis geometry chemistry biology decision property grammar hedgehog progress'.split()

import random

def Random(list):
    i = random.randint(0, len(list) - 1)
    return list[i]

def Again():
        print('Again? (yes/no)')
        inp = input().lower()
        if inp == 'yes':
            return True
        else:
            return False

def Info(PICS, wrong, right, keyword):
    print(PICS[len(wrong)])
    print()
    print('Wrong letters:', end=' ')
    for letter in wrong:
        print(letter, end=' ')
    print()
    print('Word:', end = ' ')
    star = '*' * len(keyword)
    for j in range(len(keyword)):
        if keyword[j] in right:
            star = star[:j] + keyword[j] + star[j+1:]
    for letter in star:
        print(letter, end=' ')
    print()

def Done(doneword):
    while True:
        print('Put a letter:')
        word = input().lower()
        if word in doneword:
            print ('You have tried this one. Choose another letter')
        elif word not in 'mnbvcxzlkjhgfdsapoiuytrewq':
            print('Please, put a small latin letter')
        elif len(word) != 1:
            print('Your letter:')
        else:
            return word


#start
right = ''
wrong = ''
keyword = Random(keywords)
end = False
while True:
    Info(PICS, wrong, right, keyword)
    word = Done(wrong + right)
    if word in keyword:
        right = right + word
        all = True
        for a in range(len(keyword)):
            if keyword[a] not in right:
                all = False
                break
        if all:
            print('Win!')
            end = True
    else:
        wrong = wrong + word
        if len(wrong) == len(PICS) - 1:
            Info(PICS, wrong, right, keyword)
            print('You lose. Keyword:'+keyword+'"')
            end = True
    if end:
        if Again():
            wrong = ''
            right = ''
            end = False
            keyword = Random(keywords)
        else:
            break
