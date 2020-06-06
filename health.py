import json


class Health:
    __diseases = {}

    def __modify_diseases(self):
        del self.__diseases[" Головная боль у детей"]
        del self.__diseases[" Клещевой энцефалит  (болезнь Лайма)"]
        del self.__diseases[" Болезнь Крона"]
        del self.__diseases[" Целиакия"]
        del self.__diseases[" Боковой амиотрофический  склероз"]
        del self.__diseases[" Орторексия"]
        del self.__diseases[" Меланома"]
        del self.__diseases[" Мастопатия"]
        del self.__diseases[" Желчнокаменная болезнь"]
        del self.__diseases[" ВИЧ/СПИД"]
        del self.__diseases[" Аденоиды"]
        del self.__diseases[" Болезни сердца и сосудов"]
        del self.__diseases[" Аллергические заболевания"]
        del self.__diseases[" Отит"]
        del self.__diseases[" Панкреатит"]
        del self.__diseases[" Тонзиллит"]
        del self.__diseases[" Цистит"]
        self.__diseases["Депрессия"] = "description none"
        self.__diseases["Паранойя"] = "description none"
        self.__diseases["Аутизм"] = "description none"
        self.__diseases["Биполярное расстройство"] = "description none"
        self.__diseases["Воспаление миндалин"] = "description none"
        self.__diseases["Воспаление ушей"] = "description none"
        self.__diseases["Аллергия на грибы"] = "description none"
        self.__diseases["Аллергия на цитрусы"] = "description none"
        self.__diseases["Аллергия на рыбу"] = "description none"
        self.__diseases["ВИЧ"] = "description none"
        self.__diseases["СПИД"] = "description none"
        self.__diseases["Анорексия"] = "description none"
        self.__diseases["Незначительные проблемы со здоровьем(одышка)"] = "description none"
        self.__diseases["Идеально здоровый"] = "description none"
        self.__diseases["Здоровый"] = "description none"
        self.__diseases["Нету руки"] = "description none"
        self.__diseases["Нету ноги"] = "description none"
        self.__diseases["Глухонемой"] = "description none"
        self.__diseases["Глухой"] = "description none"
        self.__diseases["Слепой"] = "description none"
        self.__diseases["Немой"] = "description none"

    def __upload_diseases(self):
        with open('diseases.txt') as json_file:
            self.__diseases = json.load(json_file)

    def get_diseases(self):
        return self.__st()

    def __st(self):
        self.__upload_diseases()
        self.__modify_diseases()
        return self.__diseases

