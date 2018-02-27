import chardet
from collections import Counter

with open(input('Введите имя файла: '), 'rb') as file:
    text = file.read()
    decode_text = chardet.detect(text)
    res_text = text.decode(decode_text['encoding'])
    final_text = res_text

    list_word = []
    for word in final_text.split(' '):
        if len(word) > 6:
            list_word.append(word)

count_words = Counter(list_word)
sorted_words = sorted(dict(count_words).items(), key=lambda x: x[1], reverse=True)

print(sorted_words[:10])
