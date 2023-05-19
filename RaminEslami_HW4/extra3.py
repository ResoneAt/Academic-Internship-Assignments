import json


def get_database() -> dict:
    try:
        with open("database.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get database', ex)


def save(user: dict) -> None:
    dic = get_database()
    username = user['username']
    dic.update({username: user})
    try:
        with open("database.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete(username:str) -> None:
    dic = get_database()
    del dic[username]
    try:
        with open("database.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_object(username:str) -> dict | None:
    try:
        with open("database.json", "r") as fp:
            # Load the dictionary from the file
            person_dict = json.load(fp)
            user = person_dict[username]
            return user
    except Exception:
        return None

