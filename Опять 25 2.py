def generate_ideas():
    ideas = []
    print("Генератор ідей. Вводь усе, що приходить в голову! (введи 'стоп' для завершення)")

    while True:
        idea = input("Введи ідею: ")
        if idea.lower() == 'стоп':
            break
        ideas.append(idea)

    print("\n Згенеровані ідеї:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")

    return ideas


def improve_ideas(ideas):
    print("\n✍ Об'єднання або вдосконалення ідей (введи номерів через кому):")
    print("Приклад: 1,3 — об'єднати ідеї 1 і 3")

    indexes = input("Введи номери ідей для об'єднання: ")
    try:
        parts = [ideas[int(i.strip()) - 1] for i in indexes.split(',')]
        combined = " + ".join(parts)
        ideas.append(" Об'єднано: " + combined)
        print(" Ідея додана як нова: ", combined)
    except:
        print(" Неправильне введення.")

    return ideas



all_ideas = generate_ideas()


while True:
    choice = input("\nХочеш об'єднати/вдосконалити ідеї? (так/ні): ")
    if choice.lower() == 'так':
        all_ideas = improve_ideas(all_ideas)
    else:
        break


print("\n Остаточний список ідей:")
for i, idea in enumerate(all_ideas, 1):
    print(f"{i}. {idea}")