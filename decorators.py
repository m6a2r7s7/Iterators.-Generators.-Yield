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
        return res

    return wrapper


@logger
def uppercase(text):
    print(text.upper())

@logger
def islower(text):
    return text.lower()

uppercase('aaaa')

@logger
def summator(x, y):
   return x + y

three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

print('result: ', result)
print('result type: ', type(result))

def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwargs):
            my_file = open(f"{parameter}new_file.txt", 'w', encoding='utf8')
            my_file.write(f"Дата и время вызова функции: {datetime.now()} \n")
            my_file.write(f"имя функции: {foo.__name__} \n")
            my_file.write(f"Аргументы функции: {args, kwargs} \n")
            result = foo(*args, **kwargs)
            my_file.write(f"результат работы функции: {result}")
            my_file.close()
            return result
        return new_foo
    return decor

path = "Lib/site-packages/"
@parametrized_decor(parameter=path)
def foo(text):
    print(text.upper())

foo('aaa')