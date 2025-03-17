def my_decorator(func):
    def baghali(*args, **kwargs):
        print("Befor function Run!!!!!!!!!!! ")
        resulte = func(*args, **kwargs)
        print("After function Run!!!!!!!!!!! ")
        return resulte
    return baghali

@my_decorator
def say_name(name):
    print(f'$$$$$$$$$$$$$$$$$$$  hi {name} $$$$$$$$$$$$$$$$$$$')

say_name("ali")