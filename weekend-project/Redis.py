import redis


def get_from_db(key):
    client = redis.StrictRedis()
    flight_data = client.get(key)
    return flight_data


def add_to_db(key, value):
    client = redis.StrictRedis()
    client.set(key, value)
