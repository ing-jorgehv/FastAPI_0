

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_string(value):
    return isinstance(value, str)
