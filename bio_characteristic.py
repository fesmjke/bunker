from random import randint

class BIO:
    __ages = []
    __merge_bio = []
    def __random_genders(self,player_number):
        return [randint(0, 1) for i in range(0, player_number)]

    def __random_ages(self,player_number):
        for i in range(0,player_number//2):
            current_age = randint(18,80)
            self.__ages.append(current_age)
            if current_age >= 50:
                next_age = randint(18,50)
                self.__ages.append(next_age)
                continue
            if current_age <= 50:
                next_age = randint(50,80)
                self.__ages.append(next_age)
                continue
        return self.__ages

    def __merge(self,player_number):
        genders = self.__random_genders(player_number)
        ages = self.__random_ages(player_number)
        for i in range(0,10):
            if genders[i] == 0:
                self.__merge_bio.append({"Мужчина": f"{ages[i]}"})
            else:
                self.__merge_bio.append({"Женщина": f"{ages[i]}"})

    def get_bio_info(self,player_number):
        self.__merge(player_number)
        return self.__merge_bio
