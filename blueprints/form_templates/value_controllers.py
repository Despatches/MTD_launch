def larger_than(value, controller):
    if value > controller:
        return True
    else:
        return False


def less_than(value, controller):
    if value < controller:
        return True
    else:
        return False


controllers = {"larger_than": larger_than, "less_than": less_than}
