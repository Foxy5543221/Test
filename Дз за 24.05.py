slovnik = {
"привіт": "hello",
"пока": "bye",
"собака": "dog",
"кіт": "cat",
"дім": "house",
"сонце": "sun",
"місяць": "moon",
"вода": "water",
"вогонь": "fire",
"земля": "earth",
"повітря": "air",
"друзі": "friends"
}
slova = input("Введіть слово українською мовою для перекладу: ").lower()

if slova in slovnik:
    print(f"Переклад слова '{slova}': {slovnik[slova]}")
else:
    print(f"Слово '{slova}' не знайдено в словнику.")