text = input("Введіть текст: ")

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouyAEIOUY"
secret_code = ""

for char in text:
    if char.isalpha():
        if char in vowels:
            secret_code += "0"
        else:
            secret_code += "1"
    else:
        secret_code += char  # залишаємо пробіли, знаки пунктуації тощо

print("Секретний код:", secret_code)