import json
import sys

from diarybook import Diary


def read_from_json_into_application(path):
    file = open(path)
    data = json.loads(file.read())
    diaries = []
    for entry in data:
        diaries.append(Diary(entry['memo'], entry['tags']))

    return diaries


def write_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def user_login_register(username, password, user1):
    with open('userdata.json') as json_file:
        data = json.load(json_file)
        temp = data["users"]
        lst_all = [username for elem in temp for username in elem.values()]
        if username in lst_all:
            for user in data['users']:
                if username == user['username'] and password != user["password"]:
                    print("incorrect password")
                    sys.exit(0)

                if username == user['username'] and password == user["password"]:
                    print("you are logged in")
                    break

        else:
            temp.append(user1)
            print("user added")

    write_json(data, 'userdata.json')
