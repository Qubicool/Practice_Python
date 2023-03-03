import pandas as pd
# Создаем словарь с данными о животных
animals_data = {
'Name': ['Lion', 'Tiger', 'Elephant', 'Giraffe'],
'Species': ['Carnivore', 'Carnivore', 'Herbivore', 'Herbivore'],
'Weight': [190, 160, 600, 1000],
'Count': [5, 4, 8, 15]
}
columns = ['Name', 'Species', 'Weight', 'Count']
# Создаем DataFrame с данными о животных
df = pd.DataFrame(animals_data, columns=columns)
# Выводим DataFrame на экран
print(df, "\n")
# Сохраняем DataFrame в файл CSV
df.to_csv('animals.csv', index=False)
# Выбираем последние N строк из DataFrame и выводим на экран
N = 2
print(df.tail(N), "\n")
# Выбираем первые N строк из DataFrame и выводим на экран
print(df.head(N), "\n")
# Выводим описание статистики по числовым столбцам DataFrame
print(df.describe(), "\n")
# Выбираем столбец 'Species' из DataFrame и выводим на экран
print(df['Species'], "\n")
# Выбираем строки с индексами от 2 до 4 (не включая 4) и выводим на экран
print(df[2:4], "\n")
# Группируем строки в DataFrame по значениям в столбце 'Species' и выводим средний вес для каждой группы
print(df.groupby('Species').agg({'Weight': 'mean'}), "\n")
# Создаем переменную value со значением 200
value = 200
# Заполняем все пропущенные значения в DataFrame значением переменной value
print(df.fillna(value), "\n")
# Удаляем все строки с пропущенными значениями в DataFrame
print(df.dropna(), "\n")
# Сортируем строки в DataFrame по убыванию веса животных
print(df.sort_values(by='Weight', ascending=False), "\n")
# Выбираем строки, у которых вес больше значения переменной value, и выводим на экран
print(df[df['Weight'] > value], "\n")
# Переименовываем столбец 'Name' в DataFrame на 'Full Name'
print(df.rename(columns={'Name': 'Full Name'}), "\n")