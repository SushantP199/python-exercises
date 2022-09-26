import json
import requests as req
import datetime

def get_data(url):
    try:
        return req.get(url).text
    except Exception as e:
        print("UNmable to load url......")

def load_json(data):
    if not data is None:
        j = json.loads(data)
        title = j["results"][0]["name"]["title"]
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        # email = j["results"][0]["email"]
        dob = j["results"][0]["dob"]["date"]
        age = j["results"][0]["dob"]["age"]
        return title, fname, lname, dob, age

def main():
    url = "https://randomuser.me/api"
    val = load_json(get_data(url))
    if not val is None:
        d = datetime.timezone
        print(f"NAME OF PERSON : {val[0]}.{val[1]} {val[2]}")
        print(f"DOB : {val[3]} and AGE : {val[4]}")
        # print("Last name  :", val[1])
        # print("Email ID   :", val[2])

if __name__ == '__main__':
    main()