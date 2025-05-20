#!/usr/bin/python3
def log(function):
    def decorator(*args, **kwargs):
        print(f"Begining of the function calling: {function.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = function(*args, **kwargs)
        print(f"Call result: {result}")
        return result
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == "__main__":
    print(soma(5, 7))
    print(sub(5, y=7))
