import json
import requests as req

def get(url):
    try:
        req.get(url)
    except Exception as e:
        print("Wrong url please write a valid url ")
        print("\nERROR:\n", e)
    else:
        print("Requested successfully....")

def main():
    url = "https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22"
    get(url)

if __name__ == '__main__':
    main()