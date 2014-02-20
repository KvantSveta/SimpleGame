def	display(p1, p2):
	length = 9
	tab = ' ' * 44
	print('Name'.ljust(length), p1.name.ljust(7), tab, 'Name'.ljust(length), p2.name.ljust(7))
	print('Health'.ljust(length), '[', str(p1.health).rjust(2), ' ]', tab ,'Health'.ljust(length), '[', str(p2.health).rjust(2), ' ]')
	print('Precision'.ljust(length), '[', p1.precision, '%]', tab,  'Precision'.ljust(length), '[', p2.precision, '%]')
	print('Punch'.ljust(length), '[ ', p1.hand, ' ]', tab, 'Punch'.ljust(length), '[ ', p2.hand, ' ]')
	print('Kick'.ljust(length), '[ ', p1.leg, ' ]', tab, 'Kick'.ljust(length), '[ ', p2.leg, ' ]')
	print('Endurance'.ljust(length), '[', str(p1.endurance).rjust(2), ' ]', tab, 'Endurance'.ljust(length), '[', str(p2.endurance).rjust(2), ' ]')
