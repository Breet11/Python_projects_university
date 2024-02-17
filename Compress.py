def compress (text: list[str]) -> int:
    #Проверка на пустоту листа
    if not text:
        return 0

    char_counter=1
    write_index=0

    #Начиная с первого элемента, смотрим если он равен предыдущему и наращием ему счетчик
    for x in range(1,len(text)):
        if text[x] == text [x-1]:
            char_counter += 1
        #Как только он не равен предыдущему, начинаем переписывать
        else:
            text[write_index] = text[x-1]
            write_index += 1
            #Пишем после буквы количество повторений этой буквы и увеличиваем индекс записи.
            #После чего обнуляем счетчик повторяющихся символов.
            #Цикл нужен для записи счетчиков которые >9 (больше чем однозначные)
            if char_counter > 1:
                for digit in str(char_counter):
                    text[write_index] = digit
                    write_index += 1
            char_counter = 1

    #Выйдя из цикла, записываем последний считаемый символ, делаем последнюю проверку для повторяющихся символов
    text[write_index] = text[len(text)-1]
    write_index += 1
    if char_counter > 1:
        #Такой же цикл, как и выше
        for digit in str(char_counter):
            text[write_index] = digit
            write_index += 1
    return write_index

text = list('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
new_len = compress(text)

assert new_len == 20
assert text[:new_len] == list('A4B3C2XYZD4E3F3A6B28')

text = list('AAAA')
new_len = compress(text)

assert new_len == 2
assert text[:new_len] == list('A4')

text = list('AAAABBB')
new_len = compress(text)

assert new_len == 4
assert text[:new_len] == list('A4B3')

text = list('')
new_len = compress(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list('A')
new_len = compress(text)

assert new_len == 1
assert text[:new_len] == list('A')

text = list('A4B3C2XYZD4E3F3A6B28')
new_len = compress(text)

assert new_len == 20
assert text[:new_len] == list('A4B3C2XYZD4E3F3A6B28')

text = list('ABBBB')
new_len = compress(text)

assert new_len == 3
assert text[:new_len] == list('AB4')

text = list('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB')
new_len = compress(text)

assert new_len == 5
assert text[:new_len] == list('A33B4')

