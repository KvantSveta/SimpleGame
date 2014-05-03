
def action_punch_punch(p1, p2):
	return (p1.hand * p1.precision_punch * p1.endurance - p2.hand * p2.precision_punch * p2.endurance) / 13

def action_punch_kick(p1, p2):
	return (p1.hand * p1.precision_punch * p1.endurance - p2.leg * p2.precision_kick * p2.endurance) / 13 + 0.05

def action_punch_block(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance * (1 - p2.precision_block) / 13 - 0.2

def action_punch_wait(p1, p2):
	return p1.hand * p1.precision_punch * p1.endurance / 13 - 0.8

def action_kick_punch(p1, p2):
	return (p1.leg * p1.precision_kick * p1.endurance - p2.hand * p2.precision_punch * p2.endurance) / 13 - 0.05

def action_kick_kick(p1, p2):
	return (p1.leg * p1.precision_kick * p1.endurance - p2.leg * p2.precision_kick * p2.endurance) / 13

def action_kick_block(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance * (1 - p2.precision_block) / 13 - 0.25

def action_kick_wait(p1, p2):
	return p1.leg * p1.precision_kick * p1.endurance / 13 - 0.85

def action_block_punch(p1, p2):
	return -p2.hand * p2.precision_punch * p2.endurance * (1 - p1.precision_block) / 13 + 0.2

def action_block_kick(p1, p2):
	return -p2.leg * p2.precision_kick * p2.endurance * (1 - p1.precision_block) / 13 + 0.25

def action_block_block(p1, p2):
	return (p2.endurance - p1.endurance) / 20

def action_block_wait(p1, p2):
	return -(13 - p2.endurance - p1.endurance) / 20

def action_wait_punch(p1, p2):
	return -p2.hand * p2.precision_punch * p2.endurance / 13 + 0.8

def action_wait_kick(p1, p2):
	return -p2.leg * p2.precision_kick * p2.endurance / 13 + 0.85

def action_wait_block(p1, p2):
	return (13 - p1.endurance - p2.endurance) / 20

def action_wait_wait(p1, p2):
	return (p2.endurance - p1.endurance) / 20
