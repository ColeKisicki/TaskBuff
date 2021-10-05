from random import randrange
import hashlib 

def returnTrueIfUnique(innerComponent, entireList):
	for i in entireList:
		if innerComponent == i:
			return False
	return True

alreadyExistingKeysList = []
trueOrFalse = ["true", "false"]
for i in range(10000):
	userID = randrange(1, 5000)
	taskID = randrange(1, 5000)
	toBeCompared = [userID, taskID]
	while returnTrueIfUnique(toBeCompared, alreadyExistingKeysList) == False:
		userID = randrange(1, 5000)
		taskID = randrange(1, 5000)
		toBeCompared = [userID, taskID]
		print("relapsed")

	trueOrFalse[randrange(0, 2)]
	"""
	print(userID, end=', ')
	print(taskID, end=', ')
	print(trueOrFalse[randrange(0, 2)], end=', ')
	print(trueOrFalse[randrange(0, 2)])
	"""
	print("INSERT INTO usertasksfact(usertasks_userid, usertasks_taskid, usertasks_isowner, usertasks_iscreator) VALUES ('", userID, "', '", taskID, "', '", trueOrFalse[randrange(0, 2)], "', '", trueOrFalse[randrange(0, 2)], "');", sep='') 




















