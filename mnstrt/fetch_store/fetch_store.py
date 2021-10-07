"""Access and store rental listing in database"""

import time
from time import strftime
import pandas as pd
import requests
import re

from ..database import insert_listing


def fetch_store():
    """ Fetch and store rental data """
    for city in [1,2,3,4,5,72,73]:
        print(city)
        for page in range(1, 100):
            url = "https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity&beds=&type%5B%5D=Apartment&type%5B%5D=Condo&type%5B%5D=Loft&price_range_adv%5Bfrom%5D=null&price_range_adv%5Bto%5D=null&furnishing=Unfurnished&novacancy=0&type%5B%5D=Townhouse&city_id={}&cur_page={}".format(
                city, page
            )
            response = requests.get(url)
            data = response.json()
            listings = data["listings"]
            for listing in listings:
                try:
                    target_listing = {}

                    sq_feet = re.sub(
                                "[^0-9]", "", listing['sq_feet'])

                    sq_feet = float(sq_feet) if sq_feet.isdigit() else None

                    target_listing["retrieval_date"] = pd.to_datetime("today").strftime(
                        "%m/%d/%Y"
                    )
                    target_listing["userId"] = listing["userId"]
                    target_listing["city"] = listing["city"]
                    target_listing["address"] = listing["address"]
                    try: 
                        target_listing["price"] = float(listing["price"])
                    except:
                        target_listing["price"] = float(listing["price"].split('-')[0])
                    target_listing["latitude"] = listing["latitude"]
                    target_listing["longitude"] = listing["longitude"]
                    target_listing["bedrooms"] = listing["bedrooms"]
                    target_listing["baths"] = listing["baths"]
                    target_listing["type"] = listing["type"]
                    target_listing["city"] = listing["city"]
                    target_listing["location"] = listing["location"]
                    target_listing["utilities_included"] = str(
                        listing["utilities_included"]
                    )
                    target_listing["title"] = str(listing["title"])
                    target_listing["sq_feet"] = sq_feet
                    target_listing["community"] = listing["community"]
                    target_listing["garage_size"] = listing["garage_size"]

                    # Insert row
                    insert_listing.insert_listing(target_listing)
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
                    pass
        print("Page {} inserted".format(page))

    print("Done")


if __name__ == "__main__":
    fetch_store()
