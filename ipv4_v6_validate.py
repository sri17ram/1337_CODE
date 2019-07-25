import re

def ip_data_validate(getip):
    print (getip)
    if re.search('\\.', getip):
        print ("I am here")
        ips = getip
        ips = ips.split('.')
        status = "IPv4"
        for octets in ips:
            # octets = "0"
            # print (len(octets))
            if re.search("^0[0-9]", octets) \
                or len(octets) > 3 \
                or int(octets) >= 255 \
                or int(octets) < 0 \
                or len(ips) > 4:
                status = "Neither"
        return status
    elif re.search(':', getip):
        ips = getip
        ips = ips.split(':')
        print (ips)
        status = "IPv6"
        for octets in ips:
            octets = "2001"
            if
            either it can be a hexa 0-9 A-Z - 4 digits
            :: valid
            :0: valid

            small
            print(octets)
            exit()
ip_data_validate(getip="2001:db8:85a3:0000:0000:8a2e:0370:7334")

## 0101


