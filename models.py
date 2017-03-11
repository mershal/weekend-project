class Flight(object):
    def __init__(self, source, destination, start_date, end_date, price, airway, flight_id):
        self.source = source
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.airway = airway
        self.flight_id = flight_id

    def to_dict(self):
        return {
            "source": self.source,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "price": self.price,
            "airway": self.airway,
            "flight_id": self.flight_id,
        }

    @classmethod
    def from_dict(cls, d):
        return Flight(
            d["source"],
            d["destination"],
            d["start_date"],
            d["end_date"],
            d["price"],
            d["airway"],
            d["flight_id"],
        )


class Hotel(object):
    def __init__(self, **kwargs):
        mandatory_fields = ["source", "destination", "start_date", "end_date", "price", "airway", "flight_id"]

        for key, val in kwargs.iteritems():
            setattr(self, key, val)

        for key in mandatory_fields:
            if not hasattr(self, key):
                raise Exception("Expected key: %s while initializing Flight instance" % key)
