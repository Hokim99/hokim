import random
# Ввод желаемой длины пароля
length_password = int(input("Введите длину пароля: "))
# Алфавит для будущего пароля
alphabetical = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# Генерация пароля
password = "".join(random.sample(alphabetical, length_password))
# Вывод результата
print(password)