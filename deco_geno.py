def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        func_obj = func(*args, **kwargs)
        print(f"Created generator from {func.__name__}")
        return func_obj
    return wrapper


@log_activity
def number_generator(limit):
    print(" --> Generator is now running.")
    for i in range(limit):
        print(f" --> Yielding {i} ")
        yield i # Pauses here and retruns 'i'
    print(" --> Generator has finished.")



my_gen = number_generator(5)

value = next(my_gen)
print(value)

value = next(my_gen)
print(value)

value = next(my_gen)
print(value)

value = next(my_gen)
print(value)