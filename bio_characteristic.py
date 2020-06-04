from random import randint


def random_genders():
    return [randint(0, 1) for i in range(0, 10)]


def random_ages():
    ages = []
    for i in range(0,5):
        current_age = randint(18,80)
        ages.append(current_age)
        if current_age >= 50:
            next_age = randint(18,50)
            ages.append(next_age)
            continue
        if current_age <= 50:
            next_age = randint(50,80)
            ages.append(next_age)
            continue
    return ages


def flow():
    genders = random_genders()
    ages = random_ages()
    merge = {}
    for i in range(0,10):
        if genders[i] == 0:
            print("Male -", ages[i])
        else:
            print("Female -", ages[i])

flow()