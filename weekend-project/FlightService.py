import json
from Expedia import mainExpedia
import Redis
from models import Flight


def get_cheapest_flight(source, destination, start_date, end_date):
    key = "%s:%s:%s:%s" % (source, destination, start_date, end_date)

    cached_cheapest_flight = Redis.get_from_db(key)
    if cached_cheapest_flight is None:
        cheapest_flight = mainExpedia()
        value = json.dumps(cheapest_flight.to_dict())
        Redis.add_to_db(key, value)
        print "from expedia"
        return cheapest_flight
    else:
        print "from redis"
        return Flight.from_dict(json.loads(cached_cheapest_flight))
