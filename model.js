record = [
    {
        "id_recorod": "int",
        "user": {
            "id": "int",
            "role": {
                "teacher": "int",
                "student": "int",
                "administrative": "int"
            }
        },
        "vehiculo": {
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


def addRecord():
    print(request.data)
    body = json.loads(request.data)
    print(body)
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
    VehiclePlateCaptuuredate = body["vehicle"]["plate"]["captureDate"]
    #  VehicleOwoner = body["vehicle"]["owoner"]
    VehicleOwonerTeacher = body["vehicle"]["owoner"]["teacher"]
    VehicleOwonerStudent = body["vehicle"]["owoner"]["student"]
    VehicleOwonerAdministrative = body["vehicle"]["owoner"]["administrative"]
    VehicleOwonerVisitor = body["vehicle"]["owoner"]["visitor"]
    # Status = body["status"]
    StatusNotupdated = body["status"]["notUpdated"]
    StatusUpdated = body["status"]["updated"]
    Notes = body["notes"]

    print(idRecord)
    print(User)
    print(UserId)
    print(UserRole)
    print(UserRoleTeacher)
    print(UserRoleStudent)
    print(UserRoleAdministrative)
    print(Vehicle)
    print(VehiclePlate)
    print(VehiclePlateNumber)
    print(VehiclePlateCaptuuredate)
    print(VehicleOwoner)
    print(VehicleOwonerTeacher)
    print(VehicleOwonerStudent)
    print(VehicleOwonerAdministrative)
    print(VehicleOwonerVisitor)
    print(Status)
    print(StatusNotupdated)
    print(StatusUpdated)
    print(Notes)

    userName = 1
    print(userName)

    newUser = {
        "id_record": userName
    }
    # uri = "https://parcial-flask.herokuapp.com/users"
    # response = requests.post(uri, json=newUser)
    record.append(newUser)
    return jsonify(newUser), 200
