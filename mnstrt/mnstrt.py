"""CLI"""

import time
import click
import schedule

from mnstrt.database import test_connection
from mnstrt.database import create_table
from mnstrt.analysis import query_data
from mnstrt.fetch_store import fetch_store


@click.command()
@click.option("--option", "-opt")
def main(option):
    """main"""
    if option == "collect":
        fetch_store.fetch_store()
    if option == "collect_schedule":
        print("Collecting data")
        schedule.every().day.at("11:15").do(fetch_store.fetch_store)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if option == "test_connection":
        test_connection.test_connection()
    if option == "create_table":
        create_table.create_table()
    if option == "analysis":
        query_data.data_for_analysis()


if __name__ == "__main__":
    main()
