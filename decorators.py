from datetime import datetime

def  logger(some_funktion):

    def wrapper(*args, **kwargs):
        my_file = open('new_file.txt', 'w', encoding='utf8')
        my_file.write(f"Дата и время вызова функции: {datetime.now()} \n")
        my_file.write(f"имя функции: {some_funktion.__name__} \n")
        my_file.write(f"Аргументы функции: {args, kwargs} \n")
        res = some_funktion(*args, **kwargs)
        my_file.write(f"результат работы функции: {res}")
        my_file.close()

    return wrapper


@logger
def uppercase(text):
    return text.upper()

# @logger
# def islower(text):
#     return text.lower()

uppercase('aaaa')