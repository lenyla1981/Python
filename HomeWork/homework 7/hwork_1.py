#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько 
#просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
#(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе 
#несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в 
#программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в 
#порядке
#*Пример:*
#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
 #   **Вывод:** Парам пам-пам  


letters = ['а']
text = str("пара-ра-рам рам-пам-папам па-ра-па-да").split()
good = True
let = []
for i in range(0, len(text)):
    let.append(list(filter(lambda x: x in letters, text[i])))
    if i > 0 and len(let[i]) != len(let[0]): 
        good = False

if good: print('Парам пам-пам')
else: print('Пам парам')