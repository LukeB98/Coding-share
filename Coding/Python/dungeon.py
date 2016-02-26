import random
import pickle
stored_info = {}

def save_data():
# Pickle dictionary and write it into file
	file_name = 'dungeon_save'
	output = open(file_name, 'wb')
	stored_info['COLUMNS'] = input('How many rows should the map be? ')
	stored_info['ROWS'] = input('How many columns should the map be? ')
	stored_info['ENEMIES'] = input('How many enemies, 1 or 2? ')
	pickle.dump(stored_info, output)
	output.close()

def load_data():
#retreive pickles dictionary and print
	pickled_file = open('dungeon_save', 'rb')
	stored_info = pickle.load(pickled_file)
	return stored_info
	
answer = input('Adjust map size? Y/N: ')

if answer == 'Y':
	save_data()
else:
	stored_info = load_data()
	
def create_cells(rows, columns):
	cells = []
	m = 0
	n = 0
	#(m,n)
	while n < columns:
		
		while m < rows:
			
			cells.append((n,m))
			m += 1
			
		m = 0	
		n += 1	
		
	return cells
	
rows = int(stored_info['ROWS'])
columns = int(stored_info['COLUMNS'])
CELLS = create_cells(rows, columns)
	
def get_locations():
	monster = random.choice(CELLS)
	monster_b = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	if monster == door or monster == start or door == start or monster_b == door or monster_b == start or monster_b == monster:
		return get_locations()
	if stored_info['ENEMIES'] == '2':
		return monster, monster_b, door, start
	else:
		return monster, door, start

def move_player(player, move):
	
	x, y = player
	
	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1

	return x, y
	
def move_monster(monster):

	x, y = monster
	move_options = get_monster(monster)
	
	move = random.choice(move_options)
	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1

	return x, y

def get_monster(monster):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	a,b = monster
	monster_position = [a, b]
	if monster[1] == 0:
		moves.remove('LEFT')
	if monster[1] == rows - 1:
		moves.remove('RIGHT')
	if monster[0] == 0:
		moves.remove('UP')
	if monster[0] == columns - 1:
		moves.remove('DOWN')
	if player[0] < monster_position[0]:
		try:
			moves.remove('DOWN')
		except:
			pas
	if player[0] > monster_position[0]:
		try:
			moves.remove('UP')
		except:
			pass
	if player[1] > monster_position[1]:
		try:
			moves.remove('LEFT')
		except:
			pass
	if player[1] < monster_position[1]:
		try:
			moves.remove('RIGHT')
		except:
			pass	
	
	return moves


	
def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']


	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == rows - 1:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == columns - 1:
			moves.remove('DOWN')

	return moves
def print_map():

	grid = [
				"|X|",
				"| |",
				"|G|"
			]
	final_grid = []
	n = 0
	for item in CELLS:		
		
		if stored_info['ENEMIES'] == '2':
			if item == player:
				final_grid.append(grid[0])
			elif item == monster:
				final_grid.append(grid[2])
			elif item == monster_b:
				final_grid.append(grid[2])
			else:
				final_grid.append(grid[1])
		else:
			if item == player:
				final_grid.append(grid[0])
			elif item == monster:
				final_grid.append(grid[2])
			else:
				final_grid.append(grid[1])
	count = 0					
	while count < columns + 1:		
		print(''.join(final_grid[((count - 1) * rows):(count * rows)]))
		count += 1
	
try:
	monster, monster_b, door, player = get_locations()
except:
	monster, door, player = get_locations()
	
print("Welcome to the dungeon!")
print_map()
while True:
	moves = get_moves(player)
		
	
	print("You're currently in room {}".format(player))
	print("You can move {}".format(moves)) 
	print("Enter QUIT to quit")

	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
	
		if stored_info['ENEMIES'] == '2':
			monster_b = move_monster(monster_b)
			player = move_player(player, move)
			monster = move_monster(monster)
		else:
			player = move_player(player, move)
			monster = move_monster(monster)
			
		print_map()
		
	else:
		print("** Walls are hard, stop walking into them! **")
		continue

	if player == door:
		print("You escaped!")
		break
	elif player == monster or player == monster_b:
		print("You were eaten by the grue!")
		break