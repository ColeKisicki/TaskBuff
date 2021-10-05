from random import randrange
import hashlib 

def returnRandName():
	f=open('dummyNames.txt')
	with open('dummyNames.txt') as f:
		lines = f.read().splitlines() 
	return lines[randrange(0,4059)]
'''
def returnRandDate():
	randYear = (randrange(2021,2023))
	randMonth = (randrange(1, 13))
	if randMonth < 10:
		randMonth = "0" + str(randMonth)
	else:
		randMonth = str(randMonth)
	randDay = (randrange(1, 31))
	if randDay < 10:
		randDay = "0" + str(randDay)
	else:
		randDay = str(randDay)
	randHour = (randrange(0, 25))
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
	return finalString
'''
def returnRandEmail():
	sufficies = ["@gmail.com", "@yahoo.com", "@outlook.com"]
	email = str(randrange(1, 10000)) + sufficies[randrange(0, 3)]
	return email

def trueIfUnique(inputString, listToCompare):
	for i in listToCompare:
		if inputString == i:
			return False
	return True

createdUsernames = []
createdEmails = []
for i in range(5000):
	username = returnRandName() + str(randrange(0, 10000))
	while trueIfUnique(username, createdUsernames) == False:
		username = returnRandName() + str(randrange(0, 10000))
	createdUsernames.append(username)
	str2hash = username + str(randrange(0, 1000000)) + returnRandName()
	passwordMid = hashlib.md5(str2hash.encode())
	email = username + returnRandEmail()
	while trueIfUnique(email, createdEmails) == False:
		email = username + returnRandEmail()
	createdEmails.append(email)
	print("INSERT INTO usersdimension(users_firstname, users_lastname, users_email, users_username, users_hashedpass) VALUES ('", returnRandName(), "', '", returnRandName(), "', '", email, "', '", username, "', '", passwordMid.hexdigest(), "');", sep='') 




















