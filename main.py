import appLogic

status = True

while status:
    entrance = str(input("Зареєструватися чи ввійти в наявний аккаунт? ( r - зареєструватися, e - ввійти) :"))

    print()

    if entrance == 'e':
        if appLogic.entrance() == 0:
            break
    elif entrance == 'r':
        appLogic.registration()
    else:
        print("Помилка")
        continue

    gender = str(input("Ваша стать ? (w - жінка, m - чоловік) :"))
    if (gender != 'w') and (gender != 'm'):
        print("Помилка, программа перезавантажуєтся....")
        continue

    weight = float(input("Введіть свою вагу: "))
    height = float(input("Введіть свій зріст у метрах: "))
    age = int(input("Введіть свій вік: "))

    if gender == 'w':
        brmUser = appLogic.brmWoman(weight, height, age)
    elif gender == 'm':
        brmUser = appLogic.brmMan(weight, height, age)
    else:
        print(0)

    imt = appLogic.valueImt(weight, height)
    imtStatus = appLogic.imtStatus(imt)

    print('Виберіть рівень активності: ')
    print('''
             1) Помірна активність (сидяча робота плюс легкі фізичні навантаження або заняття 1-3 разів на тиждень; домогосподарки)
             2) Середня активність (сидяча робота плюс заняття 3-5 разів на тиждень; домогосподарка з наявністю городу; робота на ногах до 12 годин без тяжкості) 
             3) Висока активність (інтенсивні навантаження, заняття 6-7 разів на тиждень; робота на ногах плюс інтенсивний спорт)
             4) Дуже висока активність (спортсмени і люди, що виконують схожі навантаження 6-7 разів на тиждень) 
        ''')

    indexAct = int(input("Виберіть рівень який описує вас: "))
    activities = appLogic.activity(indexAct)

    print('Як тий дієти вам потрібен: ')
    print('''
             1)Для схуднення.
             2)Для підтримки ваги.
             3)Для набору маси. 
          ''')

    typeOfDiet = int(input("Виберіть тип який вам потрібен: "))
    indexDiet = appLogic.indexOfDiet(typeOfDiet)

    tempValueOfCalories = appLogic.dailyNorm(brmUser, indexDiet)
    dailyNorm = appLogic.aPFC(tempValueOfCalories, activities)

    proteinsNorm = appLogic.proteins(dailyNorm)
    carbohydratesNorm = appLogic.carbohydrates(dailyNorm)
    fatsNorm = appLogic.fats(dailyNorm)

    print('Твій індес маси тіла: ', round(imt))
    print('Твій BRM: ', round(brmUser))
    print('Твій тип ваги: ', imtStatus)
    print()
    print('Твоя добова норма калорій: ', round(dailyNorm))
    print()
    print('Норма білків: ', round(proteinsNorm))
    print('Норма вуглеводів: ', round(carbohydratesNorm))
    print('Норма жирів: ', round(fatsNorm))

    print()

    appLogic.showFood()

    whileStatus = True

    dailyUsedStatus = str(input('Перейти до калькулятора спожитих калорій? (y- так, n - ні): '))
    if dailyUsedStatus == 'y':
        while whileStatus:
            caloriesUsed = int(input('Введіть кількість спожитих калорій: '))
            dailyNorm = appLogic.dailyNormRemainder(dailyNorm, caloriesUsed)

            print('Залишилось спожити ', round(dailyNorm), ' калорій')

            whil = str(input('Продовжити роботу? (y - так,n - ні) : '))

            if whil == 'n':
                whileStatus = False

    elif dailyUsedStatus == 'n':
        print('Програма завершила свою роботу')
        print('Залишилось спожити калорій: ', round(dailyNorm))

        status = False
        break
    else:
        print(0)

    status = False
    break











