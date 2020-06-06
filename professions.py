import json


class Professions:
    __profs = {}

    def __upload_professions(self):
        with open('data.txt') as json_file:
            self.__profs = json.load(json_file)

    def get_professions(self):
        self.__upload_professions()
        return self.__profs
