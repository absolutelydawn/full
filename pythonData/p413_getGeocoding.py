#!/usr/bin/env python

import json
import os.path
import folium, requests

address = '서울시 서초구 서초대로 74길 33'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

BASE_DIR = os.path.dirname(os.path.relpath("./"))
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

header = {'Authorization': 'KakaoAK ' + get_secret("kakao_apiKey")}

def getGeocoder(address):
    result = ""
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address= r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

print(getGeocoder(address))

address_latIng = getGeocoder(address)
latitude = address_latIng[0]
longitude = address_latIng[1]

print('주소지:', address)
print('위도: ', latitude)
print('경도: ', longitude)

shopinfo = '비트빌'
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker(location=[latitude, longitude], icon=myicon, popup=shopinfo).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius=300, color='blue', fill_color='red', fill=False, popup=shopinfo).add_to(foli_map)
foli_map.save('./xx_shopmap.html')
print('file saved....')
