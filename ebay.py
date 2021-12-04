import os
import datetime as datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
import pandas as pd

api_key = 'API_KEY'

df = pd.DataFrame(columns=['Date', 'Customer Id', 'Item Code', 'Item Name', 'Price',], index=None)
print(df)

class Ebay(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch(self):
        try:
            api = Connection(appid=self.api_key, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': 'Tools'})
            print(response.reply)

            assert (response.reply.ack == 'Success')
            assert (type(response.reply.timestamp) == datetime.datetime)
            assert (type(response.reply.searchResult.item) == list)

            item = response.reply.searchResult.item[0]
            assert (type(item.listingInfo.endTime) == datetime.datetime)
            assert (type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())


    def parse(self):
        pass

# Main Driver

if __name__ == '__main__':
    e = Ebay(api_key)
    e.fetch()
    e.parse()
