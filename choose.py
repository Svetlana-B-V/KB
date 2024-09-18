def correct():
    while True:
        try:
            entry = float(input("Введите число: "))
            return entry
        except ValueError:
            print("Ошибка, введите корректное значение!")


while True:
    exit = input("Введите 'стоп' для прекращения работы программы или другое значение для работы: ")
    if exit == 'стоп':
            break
    else:
        action = input("Введите номер желаемой программы в диапазоне 1-3: ")

        if action == "1":
            #Первая задача
       
            a = correct()
      
            a2 = a * a
            a3 = a2 * a
            a5 = a3 * a2
            a2 = a5 * a5

            print("При исходном а =", a)
            print("'a' в 3 степени = ", a3)
            print("'а' в 10 степени = ", a2)
        
    
        elif action == "2":
            #Вторая задача
            import  math

            x = correct()

            if x <= 0:
                y = 0
            else:
                if x <= 1:
                    y = x*x - x
                else:
                    y = x*x - math.sin(3.14 * x*x)
            print("Число Y, при исходном X = ", x, ", равно ", round(y,2))
    
        elif action == "3":
            #Третья задача
            import math

            S = 0
            i = 1

            for i in range(1, 131, 1):
                S = 1 / ((2*i)**2) + S
            print("Конечная сумма = ", round(S,2))

        else:
            print("Неверный код, такой программы не существует, попробуйте ещё раз")  



    


