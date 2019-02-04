data = {}


def search():
    return data, 200


def get(key):
    if key in data:
        return data[key], 200
    else:
        return 'Not Found', 404


def put(key, value):
    data[key] = value
    return data[key], 200
