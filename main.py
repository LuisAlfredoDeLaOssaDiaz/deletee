# import requests
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

record = [
    {
        "id_record": "int",
        "user": {
            "id": "int",
            "role": {
                "teacher": "int",
                "student": "int",
                "administrative": "int"
            }
        },
        "vehicle": {
            "plate": {
                "number": "string",
                "captureDate": "date"
            },
            "owoner": {
                "teacher": "int",
                "student": "int",
                "administrative": "int",
                "visitor": "init"
            }
        },
        "status": {
            "notUpdated": "int",
            "updated": "int"
        },
        "notes": "string"

    }
]

@app.route('/record', methods=['GET'])
def getAllUsers():
    return jsonify(record), 200

@app.route('/record/<id_record>', methods=['GET'])
def getlRecordByid_record(id_record):
    result = next((idRecord for idRecord in record if idRecord["id_record"] == id_record),None)
    if result is not None:
        return jsonify(result), 200
    else: 
        return "User not found", 404

@app.route('/record', methods=['POST'])
def addRecord():
    body = json.loads(request.data)

    idRecord = body["id_record"]
    # User = body["user"]
    UserId = body["user"]["id"]
    # UserRole = body["user"]["role"]
    UserRoleTeacher = body["user"]["role"]["teacher"]
    UserRoleStudent = body["user"]["role"]["student"]
    UserRoleAdministrative = body["user"]["role"]["administrative"]
    # Vehicle = body["vehicle"]
    # VehiclePlate = body["vehicle"]["plate"]
    VehiclePlateNumber = body["vehicle"]["plate"]["number"]
    VehiclePlateCapturedate = body["vehicle"]["plate"]["captureDate"]
    #  VehicleOwoner = body["vehicle"]["owoner"]
    VehicleOwonerTeacher = body["vehicle"]["owoner"]["teacher"]
    VehicleOwonerStudent = body["vehicle"]["owoner"]["student"]
    VehicleOwonerAdministrative = body["vehicle"]["owoner"]["administrative"]
    VehicleOwonerVisitor = body["vehicle"]["owoner"]["visitor"]
    # Status = body["status"]
    StatusNotupdated = body["status"]["notUpdated"]
    StatusUpdated = body["status"]["updated"]
    Notes = body["notes"]

    #print(idRecord)
    ## print(User)
    #print(UserId)
    ## print(UserRole)
    #print(UserRoleTeacher)
    #print(UserRoleStudent)
    #print(UserRoleAdministrative)
    ## print(Vehicle)
    ## print(VehiclePlate)
    #print(VehiclePlateNumber)
    #print(VehiclePlateCapturedate)
    ## print(VehicleOwoner)
    #print(VehicleOwonerTeacher)
    #print(VehicleOwonerStudent)
    #print(VehicleOwonerAdministrative)
    #print(VehicleOwonerVisitor)
    ## print(Status)
    #print(StatusNotupdated)
    #print(StatusUpdated)
    #print(Notes)

    newRecord = {
        "id_record": idRecord,
        "user": {
            "id": UserId,
            "role": {
                "teacher": UserRoleTeacher,
                "student": UserRoleStudent,
                "administrative": UserRoleAdministrative
            }
        },
        "vehicle": {
            "plate": {
                "number": VehiclePlateNumber,
                "captureDate": VehiclePlateCapturedate
            },
            "owoner": {
                "teacher": VehicleOwonerTeacher,
                "student": VehicleOwonerStudent,
                "administrative": VehicleOwonerAdministrative,
                "visitor": VehicleOwonerVisitor
            }
        },
        "status": {
            "notUpdated": StatusNotupdated,
            "updated": StatusUpdated
        },
        "notes": Notes

    }

    # uri = "https://parcial-flask.herokuapp.com/users"
    # response = requests.post(uri, json=newUser)
    record.append(newRecord)
    return jsonify(newRecord), 200


@app.route('/users/<username>', methods=['DELETE'])
def deleteUser(username):
    userFound = None
    for index, user in enumerate(record):
        if user["Username"] == username:
            userFound = user
            record.pop(index)
    if userFound is not None:
        return "User deleted", 200
    else: 
        return "User not found", 404

@app.route('/users/<username>', methods=['PUT'])
def updateUser(username):
    body = json.loads(request.data)

    newUsername = body["Username"]
    newAge = body["Age"]

    updatedUser = {
        "Username": newUsername,
        "Age": newAge
    }

    userUpdated = None

    for index, user in enumerate(record):
        if user["Username"] == username:
            userUpdated = updatedUser
            record[index] = updatedUser
            
    if userUpdated is not None:
        return "User Updated", 200
    else: 
        return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)




#    https://parcial-flask.herokuapp.com/record method='GET'
#    https://parcial-flask.herokuapp.com/record/<id_record> method='GET'
#
#    https://parcial-flask.herokuapp.com/record method='POST'
#
#    https://parcial-flask.herokuapp.com/record/<id_record> method='DELETE'
#
#    https://parcial-flask.herokuapp.com/record/<id_record> method='PUT'
