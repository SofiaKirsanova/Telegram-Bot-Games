import random

def Field(field):
    print('   |   |')
    print(' ' + field[7] + ' | ' + field[8] + ' | ' + field[9])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + field[4] + ' | ' + field[5] + ' | ' + field[6])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + field[1] + ' | ' + field[2] + ' | ' + field[3])
    print('   |   |')

def Field2(field):#append добавляет в конец
	field2 = []
	for i in field:
		field2.append(i)
	return field2

def Place(field):
	#true если нет места
	for i in range(1, 10):
		if field[i] == ' ':
			return False
	return True

def Win(field, sign):
	return ((field[1] == sign and field[2] == sign and field[3] == sign) or (field[4] == sign and field[5] == sign and field[6] == sign) or
	(field[7] == sign and field[8] == sign and field[9] == sign) or (field[1] == sign and field[4] == sign and field[7] == sign) or
    (field[2] == sign and field[5] == sign and field[8] == sign) or (field[3] == sign and field[6] == sign and field[9] == sign) or
	(field[1] == sign and field[5] == sign and field[9] == sign) or (field[3] == sign and field[5] == sign and field[7] == sign))

def MoveP(field):
	slot = ''
	while slot not in '1 2 3 4 5 6 7 8 9'.split() or not field[int(slot)] == ' ':
		print('Yout turn (1-9):')
		slot = input()
	return int(slot)

def MoveC(field, signC):
#ИИ
	for i in range(1, 10):
		copy = Field2(field)
		if copy[i] == ' ':
			copy[i] = signP
			if Win(copy, signP):
				return i
	for i in range(1, 10): #player`s next turn is win
		copy = Field2(field)
		if copy[i] == ' ':
			copy[i] = signC
			if Win(copy, signC):
				return i
	#занять угол
	slot = SlotRandom(field, [1, 3, 7, 9])
	if slot != None:
		return slot
	#занять центр
	if field[5] == ' ':
		return 5
	#занять боковушку
	return SlotRandom(field, [2, 4, 6, 8])

def SlotRandom(field, slots):
	slot_free = []
	for i in slots:
		if field[i] == ' ':
			slot_free.append(i)
	if len(slot_free) != 0:
		return random.choice(slot_free)
	else:
		return None


def Again():
	print('Again? (yes/no)')
	inp = input().lower()
	if inp == 'yes':
		return True
	else:
		return False

#start
while True:
	print('Choose X or O')
	sign = input().upper()
	turn = ''
	if sign == 'X':
		turn = 'player'
		signP = 'X'
		signC = 'O'
	else:
		turn = 'computer'
		signP = 'O'
		signC = 'X'
	now = 10*[' ']
	game = True
	while game:
		if turn == 'player':
			#ход игрока
			Field(now)
			slot = MoveP(now)
			now[slot] = signP
			if Win(now, signP):
				Field(now)
				print ('You won')
				game = False
				Again()
			else:
				if Place(now):
					Field(now)
					print('Draw')
					break
					Again()
				else:
					turn = 'computer'
					
		else:
			#Ход компьютера
			slot = MoveC(now, signC)
			now[slot] = signC
			if Win(now, signC):
				Field(now)
				print('You lose')
				game = False
				Again()
			else:
				if Place(now):
					Field(now)
					print('Draw')
					break
					Again()
				else:
					turn = 'player'

