#!/usr/bin/python3.3

__author__ = 'j.d.'

from os import system

person = [
	'p1_start', 'p2_start', 'p1_punch',	'p2_punch', 'p1_kick', 'p2_kick', 'p1_block',
	'p2_block', 'p1_wait', 'p2_wait', 'p1_win', 'p2_win', 'p1_death', 'p2_death'
]

for i in person:
	system('convert {0}.png -channel Alpha -threshold 80% -resize 620x200 {0}.gif'.format(i))

#скрипт конвертирует .png картинки в .gif картинки
#convert *.png -channel Alpha -threshold 80% -resize 620x200 *.gif

