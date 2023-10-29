def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type', None)
        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError("Permission denied")
    return wrapper