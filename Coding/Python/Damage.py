import random

sword_dict = {'name' : 'regular sword', 'damage' : '60', 'crit_hit' : '10', 'accuracy' : '50 100'}
katana_dict = {'name' : 'regular katana', 'damage' : '40', 'crit_hit' : '20', 'accuracy' : '60 100'}
damage_delt = 0
def get_damage(weapon):

	#chance of critical hit
	if random.randint(0, 100) < int(weapon['crit_hit']):
		print('Critical hit!')
		damage_delt = 2 * int(weapon['damage'])
		return damage_delt
	
	#damage of attack
	else:
		accuracy_range = (weapon['accuracy']).split()
		percent_damage = random.randint(int(accuracy_range[0]), int(accuracy_range[1]))
		damage_delt = (percent_damage/100) * int(weapon['damage'])
		return damage_delt
	
#calling the function
damage_delt = get_damage(sword_dict)
print(sword_dict['name'] + ' delt: ' + str(damage_delt))

damage_delt = get_damage(katana_dict)
print(katana_dict['name'] + ' delt: ' + str(damage_delt))

#improved damage
#sword_dict['damage'] = int(sword_dict['damage']) + 10
#damage_delt = get_damage(sword_dict)
#print(damage_delt)