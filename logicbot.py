
def action_punch_punch(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance - p2.hand * p2.precision_punch * p2.endurance

def action_punch_kick(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance - p2.leg * p2.precision_kick * p2.endurance + 0.65

def action_punch_block(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance * (1 - p2.precision_block) - 2.6

def action_punch_wait(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance - 10.4

def action_kick_punch(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance - p2.hand * p2.precision_punch * p2.endurance - 0.65

def action_kick_kick(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance - p2.leg * p2.precision_kick * p2.endurance

def action_kick_block(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance * (1 - p2.precision_block) - 3.25

def action_kick_wait(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance - 11.05

def action_block_punch(p1, p2):
	return -p2.hand * p2.precision_punch * p2.endurance * (1 - p1.precision_block) + 2.6

def action_block_kick(p1, p2):
	return -p2.leg * p2.precision_kick * p2.endurance * (1 - p1.precision_block) + 3.25

def action_block_block(p1, p2):
	return (p2.endurance - p1.endurance) * 0.65

def action_block_wait(p1, p2):
	return -(13 - p2.endurance - p1.endurance) * 0.65

def action_wait_punch(p1, p2):
	return -p2.hand * p2.precision_punch * p2.endurance + 10.4

def action_wait_kick(p1, p2):
	return -p2.leg * p2.precision_kick * p2.endurance + 11.05

def action_wait_block(p1, p2):
	return (13 - p1.endurance - p2.endurance) * 0.65

def action_wait_wait(p1, p2):
	return (p2.endurance - p1.endurance) * 0.65
