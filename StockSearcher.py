import yfinance as yf
import pickle

centinel = 0
centinel2 = 0
try:
    with open("favorites.pickle","rb") as f:
        favorites = pickle.load(f)
except:
    favorites = []

while centinel == 0:
    print("-------------------")
    print("1- Search company\n2- Favorite companies\n3- Download data\n4- Exit")
    print("-------------------")
    election = int(input())
    if election == 1:
        print("Ticker of company to search:")
        ticker = input()
        company = yf.Ticker(ticker)
        print(company.info)
        while centinel2 == 0:
            print("-------------------------")
            print("1- Dividends\n2- Splits\n3- Balance sheet\n4- Cashflows\n5- Earnings\n6- Financials\n7- Calendar\n8- Institutional holders\n9- History data\n10- Add to favourites\n11- Exit")
            print("-------------------------")
            e = int(input())
            if e == 1:
                print(company.dividends)
            elif e == 2:
                print(company.splits)
            elif e == 3:
                print(company.balance_sheet)
            elif e == 4:
                print(company.cashflow)
            elif e == 5:
                print(company.earnings)
            elif e == 6:
                print(company.financials)
            elif e == 7:
                print(company.calendar)
            elif e == 8:
                print(company.institutional_holders)
            elif e == 9:
                print("Do you want history from custom datetime? s/n:")
                des = input()
                if des == 's' or des == 'S':
                    print("Initial date (aaaa-mm-dd):")
                    initial = input()
                    print("End date (aaaa-mm-dd):")
                    end = input()
                    print("Do you want to put interval? s/n: ")
                    inter = input()
                    if inter == 'S' or inter == 's':
                        print("Put the interval (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo): ")
                        interval = input()
                        try:
                            print(company.history(start=initial,end=end,interval=interval))
                        except:
                            print("That interval is invaled for the periode choose")
                            print(company.history(start=initial,end=end))
                    else:
                        print(company.history(start=initial,end=end))
                else:
                    print(company.history(period="max"))
            elif e == 10:
                if favorites.append(ticker):
                    print("Add correctly")
            elif e == 11:
                centinel2 = 1
    elif election == 2:
        print("Favorite companies:")
        for e in favorites:
            print(e)
    elif election == 3:
        print("Ticker: ")
        name = input()
        print("Initial date (aaaa-mm-dd):")
        initial = input()
        print("End date (aaaa-mm-dd):")
        end = input()
        data = yf.download(name,initial,end)
    elif election == 4:
        mi_path = "favorites.pickle"
        with open(mi_path, 'wb') as f:
            pickle.dump(favorites,f)
        centinel = 1

    