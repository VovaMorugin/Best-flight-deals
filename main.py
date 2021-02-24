from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.getFlightDealsData()

for price in sheet_data["prices"]:
    if price['iataCode'] == "":
        price['iataCode'] = flight_search.getIAATA(price['city'])
data_manager.putFlightDealsData(sheet_data)