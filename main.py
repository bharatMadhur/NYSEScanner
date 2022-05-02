import requests
import json


#########################################
# documentation of this file

#########################################

def api_calls():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    api_data = json.dumps(x)

    return api_data


def allFuctions(task):
    # checkValidTicker
    # reqResConnection
    # endOfTheDay
    return 0


def checkValidTicker(ticker):
    # Check if the value of the ticker is valid
    #
    return 1


def reqResConnection():
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get("https://api.tiingo.com/api/test?token=2f7e85db1869a38072f3348bdae03512c8438e30",
                                   headers=headers)

    response_message = requestResponse.json()
    if response_message['message'] == 'You successfully sent a request':
        return True
    else:
        return False


# END OF DAY PRICES FOR A TICKER
def endOfTheDay(ticker, startDate):
    if reqResConnection == False:
        return "Unable to establish Connection"
    else:
        # if check

        headers = {
            'Content-Type': 'application/json'
        }
        requestResponse = requests.get(
            "https://api.tiingo.com/tiingo/daily/"+ticker+"/prices?startDate="+str(startDate)+"&token=2f7e85db1869a38072f3348bdae03512c8438e30",
            headers=headers)
        #print(requestResponse.json())
        return requestResponse.json()


# META ENDPOINT ABOUT THE COMPANY
def aboutTheCompany(ticker):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/tiingo/daily/" + ticker + "?token=2f7e85db1869a38072f3348bdae03512c8438e30",
        headers=headers)
    print(requestResponse.json())
    pass


# NEWS API CONNECTION
def newsOfTheStock():
    import requests
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get("https://api.tiingo.com/tiingo/news?token=2f7e85db1869a38072f3348bdae03512c8438e30",
                                   headers=headers)
    print(requestResponse.json())


def print_hi(name):
    import requests
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/tiingo/utilities/search?query=sp&token=2f7e85db1869a38072f3348bdae03512c8438e30",
        headers=headers)
    print(requestResponse.json())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def forex(currencypair):
    import requests
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/tiingo/fx/top?tickers=audusd,eurusd&token=2f7e85db1869a38072f3348bdae03512c8438e30",
        headers=headers)
    print(requestResponse.json())


def currentPrice():
    import requests
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/iex/?tickers=aapl,spy&token=2f7e85db1869a38072f3348bdae03512c8438e30", headers=headers)
    print(requestResponse.json())


# MOST IMPORTANT FUNCTION FOR MY DATA ANALYSIS
def intradayChartingPrices(startDate, ticker, freq):
    startDate = "2022-04-26"
    freq = "1hour"
    ticker = "aapl,spy"
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/iex/" + ticker + "/prices?startDate=" + startDate + "&resampleFreq=" + freq + "&columns=open,high,low,close,volume&token=2f7e85db1869a38072f3348bdae03512c8438e30",
        headers=headers)
    # print(requestResponse.json())
    return requestResponse.json()


def fundamentalsDow30():
    ticker = "msft"
    try:
        headers = {
            'Content-Type': 'application/json'
        }

        requestResponse = requests.get(
            "https://api.tiingo.com/tiingo/fundamentals/" + ticker + "/statements?startDate=2022-03-25&token"
                                                                     "=2f7e85db1869a38072f3348bdae03512c8438e30",
            headers=headers)
        return requestResponse.json()
    except:
        return False


def fundamentalDow30():
    ticker = "msft"
    try:
        headers = {
            'Content-Type': 'application/json'
        }

        requestResponse = requests.get(
            "https://api.tiingo.com/tiingo/fundamentals/aapl/daily?startDate=2022-04-29&token"
            "=2f7e85db1869a38072f3348bdae03512c8438e30",
            headers=headers)
        return requestResponse.json()
    except:
        return False

    # Revenue per share ‘rps’
    # Return on asset ‘roa’
    # ‘assetTurnover’
    # ‘bookVal’
    # ‘bvps’ — > Book Value per each share
    # 'revenue'
    # 'netinc''Revenue QoQ Growth''Debt to Equity Ratio''roe'

    # headers = {
    #    'Content-Type': 'application/json'
    # }
    # requestResponse = requests.get(
    #    "https://api.tiingo.com/tiingo/fundamentals/definitions?token=2f7e85db1869a38072f3348bdae03512c8438e30",
    #    headers=headers)
    # print(requestResponse.json())

# intradayChartingPrices(1, 2, 3)
# newsOfTheStock()
# aboutTheCompany('goog')
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
