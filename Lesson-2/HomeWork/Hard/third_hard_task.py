from collections import Counter

def count_max(string: str):
    # Считаем частоты символов
    counter = Counter(string)
    # Получаем 3 самых частых символа
    return [key for key, _ in counter.most_common(3)]

s = 'aabbbcccddddeeeee'
print(count_max(s))  
