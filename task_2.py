s = 'bfgshbkis'
# срез в python работает по принципу: list[start:stop:step]
# для получения строки 'ibs' из строки 'bfgshbkis' устанавливаем начальным значением -2 (индекс символа 'i' в изначальной строке), конечным значением 1 или 2 (индексы символов 'f' и 'g') и устанавливаем шаг со значением -2
print(s[-2:2:-2])