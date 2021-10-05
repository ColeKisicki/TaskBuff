from random import randrange
import hashlib 

def returnRandTitle():
	f=open('dummyWords.txt')
	with open('dummyWords.txt') as f:
		lines = f.read().splitlines() 
	finalString = lines[randrange(0,10000)].capitalize() + ' ' + lines[randrange(0,10000)].capitalize() + ' ' + lines[randrange(0,10000)].capitalize() + ' ' + lines[randrange(0,10000)].capitalize()
	#print("built randTitle:", finalString)
	return finalString

def returnRandNotes():
	f=open('dummyWords.txt')
	with open('dummyWords.txt') as f:
		lines = f.read().splitlines()
	loopCounter = 0
	finalString = ''
	while loopCounter < 15:
		if loopCounter != 14:
			finalString = finalString + lines[randrange(0,10000)] + ' '
		else:
			finalString = finalString + lines[randrange(0,10000)]
		#print("on iteration:", loopCounter)
		loopCounter = loopCounter + 1
	#print("built randNotes:", finalString)
	return finalString	

def returnRandRating():
	ratingList = ["low", "medium", "high"]
	return ratingList[randrange(0, 3)]	

def returnRandDate():
	randYear = (randrange(2021,2023))
	randMonth = (randrange(3, 13))
	if randMonth < 10:
		randMonth = "0" + str(randMonth)
	else:
		randMonth = str(randMonth)
	randDay = (randrange(1, 31))
	if randDay < 10:
		randDay = "0" + str(randDay)
	else:
		randDay = str(randDay)
	randHour = (randrange(0, 24))
	if randHour < 10:
		randHour = "0" + str(randHour)
	else:
		randHour = str(randHour)
	randMin = (randrange(0, 60))
	if randMin < 10:
		randMin = "0" + str(randMin)
	else:
		randMin = str(randMin)
	randSec = (randrange(0, 60))
	if randSec < 10:
		randSec = "0" + str(randSec)
	else:
		randSec = str(randSec)
	finalString = str(randYear) + '-' + str(randMonth) + '-' + str(randDay) + ' ' + str(randHour) + ':' + str(randMin) + ':' + str(randSec)
	#print("built randDate:", finalString)
	return finalString

for i in range(5000):
	print("INSERT INTO tasksdimension(tasks_title, tasks_notes, tasks_priority, tasks_duedate, tasks_difficulty) VALUES ('", returnRandTitle(), "', '", returnRandNotes(), "', '", returnRandRating(), "', '", returnRandDate(), "', '", returnRandRating(), "');", sep='') 




















