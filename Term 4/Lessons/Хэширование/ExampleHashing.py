import hashlib

# Доступные алгоритмы хеширования
# print(hashlib.algorithms_available)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()

new_password = input('Установите пароль: ')
hashed_password = hash_password(new_password)
del new_password

password = input('Введите ваш пароль: ')

if check_password(hashed_password, password):
    print("Вы залогинились!")
else:
    print("Пароли не совпали")




