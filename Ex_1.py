import xmltodict
import re


def check_tags(check, dct_c):
    tag_shops = {}
    for ch in dct_c['osm'][check]:
        if 'tag' in ch:
            tags = ch['tag']
            if isinstance(tags, list):
                for tag in tags:
                    if tag['@v'] == 'supermarket':
                        for tagname in tags:
                            if tagname['@k'] == 'name':
                                if not tag_shops.get(tagname['@v']):
                                    tag_shops[tagname['@v']] = 1
                                else:
                                    tag_shops[tagname['@v']] += 1
    return tag_shops


file = open('C:/Python/8.osm', 'r', encoding='utf-8')
text = file.read()
file.close()

dct = xmltodict.parse(text)
dct_shops1 = check_tags('way', dct)
dct_shops2 = check_tags('node', dct)
for k, v in dct_shops1.items():
    if k in dct_shops2:
        dct_shops2[k] += v
    else:
        dct_shops2[k] = v

print(dct_shops2)
