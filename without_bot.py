import TicTacToe
import Hangman

print('Which game do you want to play?(Hangman/TicTacToe)')
text = str(input())
if text == 'TicTacToe':
    TicTacToe.main()
else:
    Hangman.main()
