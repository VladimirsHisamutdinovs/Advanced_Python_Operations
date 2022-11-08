def turn_off(func):
    return lambda *args, **kwargs: None

print("Hello")
print = turn_off(print)
print("Hush")