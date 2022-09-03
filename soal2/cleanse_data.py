import json
import re
from collections import OrderedDict

filename = '/Users/tiara/Documents/personal/soal-2.json'
with open(filename) as fp:
  data = json.load(fp)

dest = {}
for i in data:
  for r in (("nila merah dan hitam", "nila merah,nila hitam"),
            ("ikan ", ""), 
            ("dan ", ","),
            ("tngkol",""),
            (" ", ","),
            ("parin","patin"),
            ("majaer","mujaer"),
            ("gurami","gurame"),
            ("jaer ", "mujaer"),
            ("cumi ","cumi-cumi"),
            ("mujair","mujaer")
            ):
    #replace set of string above
    i['komoditas'] = i['komoditas'].replace(*r)
    
    #replace first comma char
    i['komoditas'] = re.sub(r'^,','',i['komoditas'])
    #replace doubble comma
    i['komoditas'] = i['komoditas'].replace(',,',',')
    #convert str to list
    list_komoditas = list(i['komoditas'].split(","))

  #get all integer 
  i['berat'] = re.findall(r'\d+', i['berat'])

  #convert all items in list to integer
  berat_int = [eval(i) for i in i['berat']]
  # print(i['berat'])

  #map between list komoditas & list berat
  #
  dict_komoditas_berat = dict(zip(list_komoditas, berat_int))
  # print(dict_komoditas_berat)

  dest = {
    key: dest.get(key, 0) + dict_komoditas_berat.get(key, 0) for key in set(dest) | set(dict_komoditas_berat)
  }
# print(dest)  

#sort dictionary dest descending
dest = dict(sorted(dest.items(), key=lambda item: item[1], reverse=True))

#add description kg and exclude komoditi "null"
for k,v in dest.items():
  if k != '':
    print(k,":",v,"kg")


