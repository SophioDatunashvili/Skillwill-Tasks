import json
import sys
import os.path

from diarybook import Diary, DiaryBook
from usersdata import UserData, User
from util import read_from_json_into_application, write_json, user_login_register


class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.sort,
            '6': self.quit
        }

    def display_menu(self):
        print(""" 
                     Notebook Menu  
                    1. Show diaries
                    2. Add diary
                    3. Search diaries
                    4. Populate database
                    5. Sort diaries
                    6. Quit program
                    """)

    def run(self):

        username = input("Enter username: ")
        password = input("Enter password: ")

        user1 = {"username": username, "password": password}
        user_login_register(username, password, user1)

        global file_name
        file_name = username + ".json"
        if os.path.isfile(file_name):
            pass
        else:
            with open(file_name, "a") as file:
                file.write("[]")


        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_diaries(self, diaries=None):
        if not diaries:
            diaries = self.diarybook.diaries
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        memo = input("Enter a memo:         ")
        tags = input("add tags:             ")
        self.diarybook.new_diary(memo, tags)
        with open(file_name) as json_file:
            data = json.load(json_file)
            y = {"memo": memo, "tags": tags}
            data.append(y)

        write_json(data, file_name)
        print("Your note has been added")


    def search_diaries(self):

        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def quit(self):

        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application(file_name)
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

    def sort(self):
        sort_method = input(''' Sort Options:
                        1. Sort by descending id
                        2. Sort memo A-Z
                        3. Sort memo Z-A
    Enter an Option: ''')
        diaries = self.diarybook.sort_diary(sort_method)
        for diary in diaries:
            print(f"{diary['id']}-{diary['memo']}")


if __name__ == "__main__":
    Menu().run()
