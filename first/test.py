def hello():
    """ изначальная функция """
    print("hello")

def angry_func():
    """ новая функция """
    print("grrrht!")

def wrap(another_func):
    """ функция, превращающая одну в другую """
    print("Я получаю функцию и делаю ее злой")
    return angry_func

hello = wrap(hello)
hello()