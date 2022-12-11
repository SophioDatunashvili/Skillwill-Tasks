import datetime


class Diary:
    last_id = 0

    def __init__(self, memo, tags=' '):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        Diary.last_id += 1

        self.id = Diary.last_id

    def match(self, filter_text):
        return filter_text in self.memo or filter_text in self.tags


class DiaryBook:
    def __init__(self):
        self.diaries = []

    def new_diary(self, memo, tags=' '):
        self.diaries.append(Diary(memo, tags))

    def search_diary(self, filter_text):
        filtered_diaries = []
        for diary in self.diaries:
            if diary.match(filter_text):
                filtered_diaries.append(diary)
        return filtered_diaries

    def sort_diary(self, sort_method):
        sorted_diaries = []
        for diary in self.diaries:
            sorted_diaries.append({"id": diary.id,
                                   "memo": diary.memo})
        if sort_method.lower() == "1":
            return sorted(sorted_diaries, key=lambda x: x["id"], reverse=True)
        elif sort_method.lower() == "2":
            return sorted(sorted_diaries, key=lambda x: x["memo"])
        elif sort_method.lower() == "3":
            return sorted(sorted_diaries, key=lambda x: x["memo"], reverse=True)
        else:
            print("Enter Valid Method")