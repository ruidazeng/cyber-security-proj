import json
with open('part_result.json') as json_file:
    data = json.load(json_file)
    for p in data:
        try:
            print('Geographic coordinate for device at ip is ({0}, {1})\n:'.format(p['ip_str']), p['location']['longtitude'], p['location']['latitude'])
            print()
        except:
            print('No known geographic coordinate system for device at ip {0}'.format(p['ip_str']))
