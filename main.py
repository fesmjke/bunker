import json
from random import shuffle,choice
from scenario import Scenario
from professions import Professions
from health import Health
from bio_characteristic import BIO
from additional_info import AInfo
from personality_traits import PTrains
from hobbies import Hobbies
from phobias import Phobias
from special_info import SInfo

class Game:
    def __init__(self,player_number):
        self.__player_number = player_number
        # def classes objects
        self.__scenario_obj = Scenario()
        self.__professions_obj = Professions()
        self.__health_obj = Health()
        self.__bio_characteristic_obj = BIO()
        self.__additional_info_obj = AInfo()
        self.__personality_trains_obj = PTrains()
        self.__hobbies_obj = Hobbies()
        self.__phobias_obj = Phobias()
        self.__special_info_obj = SInfo()

        self.__load_data()
        self.__shuffle_data()
        self.__create_players()
        self.__make_players_files()

    def __load_data(self):
        print("Loading scenarios...")
        self.__scenario = self.__scenario_obj.get_scenarios()
        print("Loading scenarios - completed!")

        print("Loading professions...")
        self.__professions = self.__professions_obj.get_professions()
        print("Loading professions - completed!")

        print("Loading diseases (health)...")
        self.__diseases = self.__health_obj.get_diseases()
        print("Loading diseases (health) - completed!")

        print("Loading bio. characteristics...")
        self.__bio_characteristics = self.__bio_characteristic_obj.get_bio_info(self.__player_number)
        print("Loading bio. characteristics - completed!")

        print("Loading additional information...")
        self.__additional_info = self.__additional_info_obj.get_additional_info()
        print("Loading additional information - completed!")

        print("Loading personality trains...")
        self.__personality_trains = self.__personality_trains_obj.get_peronality_trains()
        print("Loading personality trains - completed!")

        print("Loading hobbies...")
        self.__hobbies = self.__hobbies_obj.get_hobbies()
        print("Loading hobbies - completed!")

        print("Loading phobias...")
        self.__phobias = self.__phobias_obj.get_phobias()
        print("Loading phobias - completed!")

        print("Loading special information...")
        self.__special_info = self.__special_info_obj.get_special_info()
        print("Loading special information - completed!")
    def __shuffle_data(self):
        # Scenarios
        keys = list(self.__scenario.keys())
        shuffle(keys)
        self.__shuffled_scenario = dict()
        for key in keys:
            self.__shuffled_scenario.update({key:self.__scenario[key]})

        # Profs
        keys = list(self.__professions.keys())
        shuffle(keys)
        self.__shuffled_professions = dict()
        for key in keys:
            self.__shuffled_professions.update({key: self.__professions[key]})

        # Diseases
        keys = list(self.__diseases.keys())
        shuffle(keys)
        self.__shuffled_diseases = dict()
        for key in keys:
            self.__shuffled_diseases.update({key: self.__diseases[key]})

        # Bio
        shuffle(self.__bio_characteristics)
        self.__shuffled_bio_characteristics = self.__bio_characteristics

        # Additional info
        shuffle(self.__additional_info)
        self.__shuffled_additional_info = self.__additional_info

        # Personality traits
        shuffle(self.__personality_trains)
        self.__shuffled_personality_trains = self.__personality_trains

        # Hobbies
        keys = list(self.__hobbies.keys())
        shuffle(keys)
        self.__shuffled_hobbies = dict()
        for key in keys:
            self.__shuffled_hobbies.update({key: self.__hobbies[key]})

        # Phobias
        shuffle(self.__phobias)
        self.__shuffled_phobias = self.__phobias

        # Special info
        shuffle(self.__special_info)
        self.__shuffled_special_info = self.__special_info
    def __create_players(self):
        try:
            self.__players = []
            for i in range(self.__player_number):
                player = {}
                # prof
                key = choice(list(self.__shuffled_professions))
                player["Profession"] = {key: self.__shuffled_professions[key]}
                del self.__shuffled_professions[key]
                # disease
                key = choice(list(self.__shuffled_diseases))
                player["Disease"] = key
                del self.__shuffled_diseases[key]
                # bio
                key = choice(self.__shuffled_bio_characteristics)
                player["Bio.Characteristic"] = key
                self.__shuffled_bio_characteristics.remove(key)
                # additional info
                key = choice(self.__shuffled_additional_info)
                player["Additional information"] = key
                self.__shuffled_additional_info.remove(key)
                # personality traits
                key = choice(self.__shuffled_personality_trains)
                player["Personality trait"] = key
                self.__shuffled_personality_trains.remove(key)
                # hobbies
                key = choice(list(self.__shuffled_hobbies))
                player["Hobby"] = {key: self.__shuffled_hobbies[key]}
                del self.__shuffled_hobbies[key]
                # phobias
                key = choice(self.__shuffled_phobias)
                player["Phobia"] = key
                self.__shuffled_phobias.remove(key)
                # Special information
                key = choice(self.__shuffled_special_info)
                player["Special information"] = key
                self.__shuffled_special_info.remove(key)

                self.__players.append(player)
        except ValueError as error:
            print("Error ", error)

    def __make_players_files(self):
        for i in range(self.__player_number):
            with open(f"players/{i}.txt","w",encoding='utf-8') as file:
                for key in self.__players[i].keys():
                    if key == "Profession":
                        prof_key = list(self.__players[i][key].keys())  # prof name
                        file.write(f"Ваша профессия - {prof_key[0]}\n")
                        file.write(f"Описание вашей профессии - {self.__players[i][key][prof_key[0]]}\n")
                    if key == "Disease":
                        disease_key = self.__players[i][key]
                        file.write(f"Ваше состояние здоровья - {disease_key}\n")
                    if key == "Bio.Characteristic":
                        bio_key = list(self.__players[i][key].keys())
                        file.write(f"Ваш пол - {bio_key[0]}\n")
                        file.write(f"Ваш возраст - {self.__players[i][key][bio_key[0]]}\n")
                    if key == "Additional information":
                        file.write(f"Ваша карта с доп. информацией под номером - {self.__players[i][key]}\n")
                    if key == "Personality trait":
                        file.write(f"Ваша персональная четра - {self.__players[i][key]}\n")
                    if key == "Hobby":
                        hobby_key = list(self.__players[i][key].keys())
                        file.write(f"Ваше хобби - {self.__players[i][key][hobby_key[0]]}(Номер хобби - {hobby_key[0]})\n")
                    if key == "Phobia":
                        file.write(f"Ваша фобия - {self.__players[i][key].capitalize()}\n")
                    if key == "Special information":
                        file.write(f"Ваша карта с спец. информацией под номером - {self.__players[i][key]}\n")

if __name__ == '__main__':
    print("Number of players can not be lower than 6 or higher than 12, also can not be odd (7,9,11)\n")
    player_number = int(input("Enter number of players"))
    game = Game(player_number)