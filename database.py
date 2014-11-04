import pymongo, hashlib
connection = pymongo.Connection()

db = connection["database"]
users = db.users

#return true if valid input; false if not
def checkPassword(passwordToCheck):
    return len(passwordToCheck) > 0

def checkUsername(usernameToCheck):
    return len(usernameToCheck) > 0

def addUser(username, password):
    if (((checkUsername(username) == False) or (checkPassword(password) == False)) or (users.find({"username":username}).count()>0)):
        return False
    else:
        newUser = {"username": username,"password": hashlib.sha512(password).hexdigest()}
        users.insert(newUser)
        return True

def validateUser(username, password):
    record = users.find({"username":username})
    if (record.count() != 1):
        return False
    else:
        #print ""
        #print record[0]['password']
        return record[0]['password'] == hashlib.sha512(password).hexdigest()
       
