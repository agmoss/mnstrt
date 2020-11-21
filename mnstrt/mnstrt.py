import pandas as pd
import urllib.request
import json
import psycopg2

from mnstrt.database import database


def get_data():
    """ Fetch rental data """
    columns = [
        "latitude",
        "longitude",
        "address",
        "price",
        "bedrooms",
        "baths",
        "type",
        "city",
        "location",
        "utilities_included",
        "website",
        "intro",
    ]
    city_id = 1
    df4 = pd.DataFrame(data=None, columns=columns)
    for page in range(100):
        url = "https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity&cur_page={}&beds=&type%5B%5D=Apartment&type%5B%5D=Condo&type%5B%5D=Loft&price_range_adv%5Bfrom%5D=null&price_range_adv%5Bto%5D=null&novacancy=0&city_id=5"
        r = urllib.request.urlopen(url)
        data = json.loads(r.read().decode())
        for item in range(0, len(data["listings"])):
            df_t = pd.DataFrame([data["listings"][item]])
            df_t = df_t[columns]
            df4 = df4.append(df_t)

            # print(item)
            # print(item['latitude'],item['longitude'],item['address'],item['price'],item['bedrooms'],item['baths'],item['type'],item['city'])
            # return None
    df4["address"] = df4.address.astype("category")
    df4["company"] = df4.website.str.split("/").str.get(2)
    df4["company"] = df4.company.str.replace("www.", "")
    df4["company"] = df4.company.str.replace(".com", "")
    df4["price"] = pd.to_numeric(df4["price"])
    df4["property_no"] = df4.address.cat.codes

    print(df4.head())


def main():
    database.connect()
    # get_data()


if __name__ == "__main__":
    main()
