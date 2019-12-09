import shodan
import time

SHODAN_API_KEY = "K42zXXtUyHPCdX94Auz9m4xRX5zr5DaU"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
for i in range(256):
    for j in range(256):
        time.sleep(1) # Slow down API call, 1 request per second
        ip_adresss = '129.59.{0}.{1}'.format(i, j)
        print("Looking up ip address {0}".format(ip_adresss))
        try:
                # Lookup the host
                host = api.host(ip_adresss)

                # Print general info
                print("""
                        IP: {}
                        Organization: {}
                        Operating System: {}
                """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

                # Print all banners
                for item in host['data']:
                        print("""
                                Port: {}
                                Banner: {}
                        """.format(item['port'], item['data']))
        except shodan.APIError as e:
                print('Error: {}'.format(e))

print('Scanning completed...')
