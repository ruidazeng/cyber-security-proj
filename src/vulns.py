import json
with open('part_result.json') as json_file:
    data = json.load(json_file)
    for p in data:
        try:
            print('Vulnerabilities for device at ip {0}\n:'.format(p['ip_str']), p['vulns'])
            print()
        except:
            print('No known vulnerabilities for device at ip {0}'.format(p['ip_str']))
