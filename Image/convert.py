#!/usr/bin/python3.3

__author__ = 'j.d.'

from os import system

person = [
	'person_punch_punch', 'person_punch_kick', 'person_punch_block', 'person_punch_wait',
	'person_kick_punch', 'person_kick_kick', 'person_kick_block', 'person_kick_wait',
	'person_block_punch', 'person_block_kick', 'person_block_block', 'person_block_wait',
	'person_wait_punch', 'person_wait_kick', 'person_wait_block', 'person_wait_wait'
]

for i in person:
	system('convert {0}.png -channel Alpha -threshold 80% -resize 620x200 {0}.gif'.format(i))

скрипт конвертирует .png картинки в .gif картинки
#convert *.png -channel Alpha -threshold 80% -resize 620x200 *.gif

