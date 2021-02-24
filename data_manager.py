import os

import requests


class DataManager:
    SHEETY_BEARER = os.environ["SHEETY_BEARER"]
    SHEETY_FILE_NAME = os.environ["SHEETY_FILE_NAME"]

    SHEETY_END_POINT = f"https://api.sheety.co/{SHEETY_FILE_NAME}/flightDeals/prices"

    sheety_headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_BEARER
    }

    def getFlightDealsData(self):
        sheet_response = requests.get(url=self.SHEETY_END_POINT, headers=self.sheety_headers)
        sheet_response.raise_for_status()
        return sheet_response.json()

    def putFlightDealsData(self, data):
        for city in data['prices']:
            sheet_inputs = {
                "price": {
                    "city": city["city"],
                    "iataCode": city["iataCode"],
                    "lower price": city["lowestPrice"]
                }
            }
            row_url = f"{self.SHEETY_END_POINT}/{city['id']}"
            sheet_response = requests.put(url=row_url, json=sheet_inputs, headers=self.sheety_headers)
            sheet_response.raise_for_status()
            print(sheet_response.json())
