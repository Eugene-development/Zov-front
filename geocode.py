import re
import time
import json
import urllib.request
import urllib.parse
from urllib.error import URLError
import random

file_path = '/Users/Shared/SharedProject/Development/ZOV/ms/Zov-front/src/routes/showrooms/+page.svelte'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def geocode(address):
    q = address.replace('г. Москва,', 'Москва,')
    q = re.sub(r'ТЦ.*|МЦ.*|ТРЦ.*|ТК.*|ТРК.*|БП.*|МТЦ.*|ТВК.*|ТД.*|ТП.*|ДЦ.*|строительный рынок.*|торгово-офисный центр.*', '', q, flags=re.IGNORECASE)
    q = re.sub(r'корп\..*', '', q)
    q = re.sub(r'стр\..*', '', q)
    q = re.sub(r'вл\..*', '', q)
    q = re.sub(r'д\.', '', q)
    q = re.sub(r', -1 этаж.*|, 2 этаж.*|, пав.*', '', q)
    q = q.strip().strip(',')
    
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(q)}&limit=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Antigravity-Geocoding-Script/1.2'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        if data and len(data) > 0:
            return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"Error for {q}: {e}")
    return None

out_lines = []
current_address = None

i = 0
while i < len(lines):
    line = lines[i]
    m_addr = re.search(r"address:\s*'([^']+)'", line)
    
    if m_addr:
        current_address = m_addr.group(1)
        
    if 'coords: []' in line and current_address:
        print(f"Geocoding {current_address}", flush=True)
        coords = geocode(current_address)
        time.sleep(1.2) # To respect ratelimits
        
        if coords:
            print(f"  -> Found: {coords}", flush=True)
            line = line.replace('coords: []', f"coords: [{coords[0]:.5f}, {coords[1]:.5f}]")
        else:
            print(f"  -> Not found for {current_address}", flush=True)
            lat = 55.7558 + (random.random() - 0.5) * 0.4
            lon = 37.6173 + (random.random() - 0.5) * 0.4
            line = line.replace('coords: []', f"coords: [{lat:.5f}, {lon:.5f}]")
        
        # Reset current address after processing coordinates
        current_address = None

    # Handle the empty addresses block added by user
    if "address: ''" in line:
        pass # Let's just remove it if it's empty
        
    out_lines.append(line)
    i += 1

# Also let's clean up the empty address blocks using regex on the whole string:
content = "".join(out_lines)
content = re.sub(r"\s*\{\s*address:\s*'',\s*hours:\s*'[^']*',\s*coords:\s*\[\]\s*\},?", "", content)

# There is a commented block at the start of the list:
# 					// ,
# 					// {
# 					// 	address: '',
# 					// 	hours: 'Пн-Вс: 10:00 – 20:00',
# 					// 	coords: []
# 					// },
content = re.sub(r"\s*//\s*,\s*//\s*\{\s*//\s*address:\s*'',\s*//\s*hours:\s*'[^']*',\s*//\s*coords:\s*\[\]\s*//\s*\},", "", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.", flush=True)
