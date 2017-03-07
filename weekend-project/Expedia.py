from bs4 import BeautifulSoup
import requests
import json
from models import Flight



allFlightInfo =[]

def userInput(flyongFrom, flyingTo, departingDate, returningDate):
    pass

def askFromExpedia():
    expediaResponse = requests.get("https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:NYC,to:FEZ,departure:03/06/2017TANYT&leg2=from:FEZ,to:NYC,departure:03/09/2017TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search")
    # with open("./content", "w") as my_file:
    #     my_file.write(expediaResponse.content)
    soup = BeautifulSoup(expediaResponse.content,  'html.parser')
    expediaFilteredResponse = soup.find_all('script', {"id": "cachedResultsJson"})
    expediaFilteredResponse = expediaFilteredResponse[0]

    expediaFilteredResponse = expediaFilteredResponse.getText()
    expediaPrice = json.loads(expediaFilteredResponse)
    # print expediaPrice.keys()
    contentJson = json.loads(expediaPrice["content"])
    lowestPrice = float("inf")
    for results in contentJson['legs']:
        singleFlight = contentJson['legs'][results]['price']['exactPrice']
        if singleFlight < lowestPrice:
            cheapestPrice=singleFlight
            cheapestDeal = results
    return cheapestDeal, contentJson
    # print lowestPrice
    # print results

def findDestination (contentJson, results):
    timeline = contentJson['legs'][results]['timeline']
    for destinationInTimeline in timeline:
        if "arrivalAirport" in destinationInTimeline:
            return destinationInTimeline

def findAirway(contentJson, results):
    timeline = contentJson['legs'][results]['timeline']
    for airwayInTimeline in timeline:
        if "carrier" in airwayInTimeline:
            return airwayInTimeline


def mainExpedia():
    print "Gil<3"
    results, contentJson = askFromExpedia()
    destinationInTimeline = findDestination(contentJson, results)
    airwayInTimeline = findAirway(contentJson, results)
    flightIdInTimeline = findAirway(contentJson, results)
    info = {
        "source" : contentJson['legs'][results]['departureLocation']['airportCode'],
        "destination" : destinationInTimeline['arrivalAirport']['code'],
        "start_date" : contentJson['legs'][results]['departureTime']['date'],
        "end_date" : contentJson['legs'][results]['arrivalTime']['date'],
        "price" : contentJson['legs'][results]['price']['exactPrice'],
        "airway" : airwayInTimeline['carrier']['airlineName'],
        "flight_id" : flightIdInTimeline['carrier']['flightNumber']
    }
    return Flight(info["source"], info["destination"], info["start_date"], info["end_date"], info["price"], info["airway"], info["flight_id"])
