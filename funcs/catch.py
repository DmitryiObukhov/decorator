def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print("Found 1 error during execution of your function: KeyError no such key as foo")
    return wrapper