import click
import pandas as pd
import schedule
import time
from time import strftime
import requests
import tldextract

from mnstrt.database import test_connection
from mnstrt.database import insert_listing
from mnstrt.database import create_table

from mnstrt.analysis import query_data


def mnstrt():
    """ Fetch and store rental data """
    for page in range(2):
        url = "https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity&cur_page={}&beds=&type%5B%5D=Apartment&type%5B%5D=Condo&type%5B%5D=Loft&price_range_adv%5Bfrom%5D=null&price_range_adv%5Bto%5D=null&novacancy=0&city_id=5"
        response = requests.get(url)
        data = response.json()
        listings = data['listings']
        for listing in listings:
            target_listing = {}
            target_listing['retrieval_date'] = pd.to_datetime('today').strftime("%m/%d/%Y")
            ext = tldextract.extract(listing['website'])
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
        print('Page {} inserted'.format(page :=page+1))
    print("Done")

@click.command()
@click.option('--option', '-opt')
def main(option):
    if(option == 'collect'):
        mnstrt()
    if(option == 'schedule_collect'):
        print('Collecting data')
        schedule.every().day.at("02:00").do(mnstrt)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if(option == 'test_connection'):
        test_connection.connect()
    if(option == 'create_table'):
        create_table.create_table()
    if(option == 'analysis'):
        query_data.data_for_analysis()


if __name__ == "__main__":
    main()
