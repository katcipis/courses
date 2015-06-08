import pymongo
import sys

# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students                 # attach to db
collection = db.grades         # specify the colllection

try:
    cursor = collection.find({"type" : "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.DESCENDING)])
    previous = None
    for item in cursor:
        global previous

        if previous == None:
            previous = item
            continue

        if previous["student_id"] != item["student_id"]:
            print("Removing the grade: {0}".format(previous))
            collection.remove(previous)
            print("done")

        previous = item

    print("Removing last grade")
    collection.remove(previous)

except Exception as e:
    print "Error trying to read collection:", type(e), e

