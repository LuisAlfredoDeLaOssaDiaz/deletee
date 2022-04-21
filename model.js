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
