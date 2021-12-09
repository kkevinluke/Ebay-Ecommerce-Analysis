import os
import datetime as datetime

from ebaysdk import response
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
import pandas as pd

API_KEY = 'APIKEY'

#df = pd.DataFrame(columns=['Date', 'Customer Id', 'Item Code', 'Item Name', 'Price',], index=None)
#print(df)

class Ebay(object):
    def __init__(self,API_KEY):
        self.api_key = API_KEY

    def fetch(self):
        try:
            api = Connection(domain ='svcs.sandbox.ebay.com', appid=self.api_key, siteid="EBAY-GB", config_file='ebay.yaml')
            #api = Connection(domain='http://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=drone&limit=3', appid=self.api_key, debug=True, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': 'car'})
            #print(response.reply.searchResult.item)
            for item in response.reply.searchResult.item:
                #print(item)
                print(f"Title: {item.title}")
                print(f"Category Name: {item.primaryCategory.categoryName}")
                print(f"Location: {item.location}")
                print(f"Shipping Type: {item.shippingInfo.shippingType}")
                print(f"Shipping Cost: {item.shippingInfo.shippingServiceCost.value}GBP")
                print(f"Price: {item.sellingStatus.currentPrice.value}GBP")
                print(f"Selling Status: {item.sellingStatus.sellingState}")
                print(f"Condition: {item.condition.conditionDisplayName}\n")

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
    e = Ebay(API_KEY)
    e.fetch()
    e.parse()




