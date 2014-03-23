from tkinter import *

def action_punch_punch(p1, p2):
	if p1.endurance >= 3 and p2.endurance >= 3:
		return 0.0
	elif p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	elif p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_punch_kick(p1, p2):
	if p1.endurance >= 3 and p2.endurance >= 5:
		return p1.hand * p1.precision_punch  + (-p2.leg) * p2.precision_kick
	elif p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	elif p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_punch_block(p1, p2):
	if p1.endurance >= 3:
		return p1.hand * p1.precision_punch * (1 - p2.precision_block)
	else:
		return 0.0

def action_punch_wait(p1, p2):
	if p1.endurance >= 3:
		return p1.hand * p1.precision_punch
	else:
		return 0.0

def action_kick_punch(p1, p2):
	if p1.endurance >= 5 and p2.endurance >= 3:
		return p1.leg * p1.precision_kick + (-p2.hand) * p2.precision_punch
	elif p1.endurance >= 5:
		return p1.leg * p1.precision_kick
	elif p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_kick_kick(p1, p2):
	if p1.endurance >= 5 and p2.endurance >= 5:
		return 0.0
	elif p1.endurance >= 5:
		return p1.leg * p1.precision_kick
	elif p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_kick_block(p1, p2):
	if p1.endurance >= 5:
		return p2.leg * p2.precision_kick * (1 - p1.precision_block)
	else:
		return 0.0

def action_kick_wait(p1, p2):
	if p1.endurance >= 5:
		return p2.leg * p2.precision_kick
	else:
		return 0.0

def action_block_punch(p1, p2):
	if p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch * (1 - p1.precision_block)
	else:
		return 0.0

def action_block_kick(p1, p2):
	if p1.endurance >= 5:
		return (-p1.leg) * p1.precision_kick * (1 - p2.precision_block)
	else:
		return 0.0

def action_block_block(p1, p2):
	return 0.0

def action_block_wait(p1, p2):
	return -1.0

def action_wait_punch(p1, p2):
	if p2.endurance >= 3:
		return (-p2.hand) * p2.precision_punch
	else:
		return 0.0

def action_wait_kick(p1, p2):
	if p2.endurance >= 5:
		return (-p2.leg) * p2.precision_kick
	else:
		return 0.0

def action_wait_block(p1, p2):
	return 1.0

def action_wait_wait(p1, p2):
	return 0.0
