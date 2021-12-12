import pickle
#
#
def entrance():
    handle = open("loginBase.txt")
    userLogin = input('Введіть логін: ')
    inputLog = userLogin
    userLogin += ":"
    userLogin += input('Введіть пароль: ')
    userLogin += "\n"
    for line in handle:
        if line == userLogin or line+"\n" == userLogin:
            handle.close()
            return inputLog
    handle.close()
    return entrance()


def registration():
    print("Реєстрація користувача")

    userLogin = str(input("Введіьть логін: "))
    userPassword = str(input("Введіть пароль: "))

    print()

    fBase = open("loginBase.txt", "a", encoding='utf-8')
    fBase.write(userLogin + ':' + userPassword + "\n")

    fBase.close()

    entrance()


def addFood():
    foodF = open('foodBase.txt', 'a', encoding='utf-8')
    food = str(input('Назва страви: '))
    calories = str(input('Калорійність на 100 грам: '))
    proteins = str(input('Введіть кількість білків в 100 грамах: '))
    carbohydrates = str(input('Введіть кількість вуглеводів в 100 грамах: '))
    fats = str(input('Введіть кількість жирів в 100 грамах: '))


    foodF.write(food + " : " + calories + " | " + proteins + " : " + carbohydrates + " : " + fats + "\n")
    foodF.close()

    status = str(input('Продовжити ? (y - так, n - ні): '))
    if status == 'y':
        addFood()
    elif status == 'n':
        showFood()
    else:
        print(0)


def showFood():
    print("Таблиця продуктів")
    print("Страва : калорійність | білків : жирів : вуглеводів")

    foodF = open('foodBase.txt', 'r', encoding='utf-8')
    contentFoodF = foodF.read()
    foodF.close()

    print(contentFoodF)

    status = str(input('Додати нові продукти? (y - так,n - ні): '))

    if status == 'y':
        addFood()


def brmWoman (weight, height, age):
    bmr = 447.593 + (9.247 * weight) + (3.097 * height) + (4.33 * age)
    return bmr


def brmMan (weight, height, age):
    brm = 88.362 + (13.397 * weight) + (4.799 * height) + (5.677 * age)
    return brm


#amount of proteins, fats and carbohydrates
def aPFC(brm, activity):
    return brm * activity


def valueImt (weight, height):
    return weight / height**2


def imtStatus (imt):
    if(imt < 18.5):
        imtStatus = "Нижче нормальної ваги"
        return imtStatus
    elif(imt >= 18.5 and imt < 25):
        imtStatus = "Нормальна вага"
        return imtStatus
    elif(imt >= 25 and imt < 30):
        imtStatus = "Надмірна вага"
        return imtStatus
    elif(imt >= 30 and imt < 35):
        imtStatus = "Ожиріння I ступеня"
        return imtStatus
    elif(imt >= 35 and imt < 40):
        imtStatus = "Ожиріння II ступеня"
        return imtStatus
    elif(imt >= 40):
        imtStatus = "Ожиріння III ступеня"
        return imtStatus


def activity(indexAct):
    if indexAct == 1:
        return 1.375
    elif indexAct == 2:
        return 1.55
    elif indexAct == 3:
        return 1.725
    elif indexAct == 4:
        return 1.9


def indexOfDiet(typeOfDiet):
    if typeOfDiet == 1:
        return 0.8
    elif typeOfDiet == 2:
        return 1
    elif typeOfDiet == 3:
        return 1.2


def dailyNorm(brm, idexOfDiet):
    return brm * idexOfDiet


def proteins(dailyNorm):
    return dailyNorm * 0.15

def fats(dailyNorm):
    return dailyNorm * 0.25

def carbohydrates(dailyNorm):
    return dailyNorm * 0.6


def dailyNormRemainder (dailyNorm, usedCallories):
    return dailyNorm - usedCallories

