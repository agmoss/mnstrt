"""Access and store rental listing in database"""

import time
from time import strftime
import pandas as pd
import requests
import tldextract

from ..database import insert_listing


def fetch_store():
    """ Fetch and store rental data """
    for page in range(100):
        url = "https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity&cur_page={page}&beds=&type%5B%5D=Apartment&type%5B%5D=Condo&type%5B%5D=Loft&price_range_adv%5Bfrom%5D=null&price_range_adv%5Bto%5D=null&novacancy=0&city_id=5"
        response = requests.get(url)
        data = response.json()
        listings = data["listings"]
        for listing in listings:
            target_listing = {}
            target_listing["retrieval_date"] = pd.to_datetime("today").strftime(
                "%m/%d/%Y"
            )
            ext = tldextract.extract(listing["website"])
            target_listing["address"] = listing["address"]
            target_listing["company"] = ext.domain
            target_listing["price"] = listing["price"]
            target_listing["latitude"] = listing["latitude"]
            target_listing["longitude"] = listing["longitude"]
            target_listing["bedrooms"] = listing["bedrooms"]
            target_listing["baths"] = listing["baths"]
            target_listing["type"] = listing["type"]
            target_listing["city"] = listing["city"]
            target_listing["location"] = listing["location"]
            target_listing["utilities_included"] = listing["utilities_included"]
            target_listing["website"] = listing["website"]
            target_listing["intro"] = listing["intro"]

            # Insert row
            insert_listing.insert_listing(target_listing)
        print("Page {} inserted".format(page := page + 1))
    print("Done")


if __name__ == "__main__":
    fetch_store()
