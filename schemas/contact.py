def contactEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "lastname":item["lastname"],
        "address":item["address"],
        "email":item["email"],
        "birthday":item["birthday"]
    }

def contactsEntity(entity) -> list:
    return [contactEntity(item) for item in entity]