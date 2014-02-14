from random import randint

def event(p1, p2):
	action = int(input('Действие: '))

	if action == 1:
		p1.punch(p2)
	elif action == 2:
		p1.kick(p2)
	elif action == 3:
		action = p1.block()
	else:
		p1.wait()

	return action
	
def event_2(p2, p1):
	action = randint(1, 4)

	if action == 1:
		p2.punch(p1)
	elif action == 2:
		p2.kick(p1)
	elif action == 3:
		action = p2.block()
	else:
		p2.wait()

	return action