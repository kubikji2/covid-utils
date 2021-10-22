import urllib.request
import json

# based on:
# https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
def download_dummy_data():
    with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
        data = json.loads(url.read().decode())
        return data

def download_test_data():
    with urllib.request.urlopen("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json") as url:
        data = json.loads(url.read().decode())
        return data

def download_json(url_str):
    with urllib.request.urlopen(url_str) as url:
        data = json.loads(url.read().decode())
        return data