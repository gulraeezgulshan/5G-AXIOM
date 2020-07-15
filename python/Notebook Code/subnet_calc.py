#!/usr/bin/env python

import sys

def calculate_subnet(input_ip, input_subnet):
    while True:
            # Validate the IP
            octet_ip = input_ip.split(".")
            #print octet_ip
            int_octet_ip = [int(i) for i in octet_ip]

            if (len(int_octet_ip) == 4) and \
                    (int_octet_ip[0] != 127) and \
                    (int_octet_ip[0] != 169) and  \
                    (0 <= int_octet_ip[1] <= 255) and \
                    (0 <= int_octet_ip[2] <=255) and \
                    (0 <= int_octet_ip[3] <= 255):
                break
            else:
                print("Invalid IP, retry \n")
                continue

    masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]

    while True:
            # Validate the subnet mask
            octet_subnet = [int(j) for j in input_subnet.split(".")]
            # print octet_subnet
            if (len(octet_subnet) == 4) and \
                    (octet_subnet[0] == 255) and \
                    (octet_subnet[1] in masks) and \
                    (octet_subnet[2] in masks) and \
                    (octet_subnet[3] in masks) and \
                    (octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
                break
            else:
                print("Invalid subnet mask, retry\n")
                continue

    # Converting IP and subnet to binary
    ip_in_binary = []

    # Convert each IP octet to binary
    ip_in_bin_octets = [bin(i).split("b")[1] for i in int_octet_ip]

    # make each binary octet of 8 bit length by padding zeros
    for i in range(0,len(ip_in_bin_octets)):
        if len(ip_in_bin_octets[i]) < 8:
            padded_bin = ip_in_bin_octets[i].zfill(8)
            ip_in_binary.append(padded_bin)
        else:
            ip_in_binary.append(ip_in_bin_octets[i])
    
    # join the binary octets
    ip_bin_mask = "".join(ip_in_binary)

    
   # print ip_bin_mask
    sub_in_bin = []

    # convert each subnet octet to binary
    sub_bin_octet = [bin(i).split("b")[1] for i in octet_subnet]

     # make each binary octet of 8 bit length by padding zeros
    for i in sub_bin_octet:
        if len(i) < 8:
            sub_padded = i.zfill(8)
            sub_in_bin.append(sub_padded)
        else:
            sub_in_bin.append(i)

    sub_bin_mask = "".join(sub_in_bin)

    # calculating number of hosts

    no_zeros = sub_bin_mask.count("0")
    no_ones = 32 - no_zeros
    no_hosts = abs(2 ** no_zeros - 2)

    # Calculating wildcard mask
    wild_mask = []
    for i in octet_subnet:
        wild_bit = 255 - i
        wild_mask.append(wild_bit)

    wildcard = ".".join([str(i) for i in wild_mask])

    ip_bin_mask[:no_ones] + "0" * no_zeros

    # Calculating the network and broadcast address
    network_add_bin = ip_bin_mask[:no_ones] + "0" * no_zeros
    broadcast_add_bin = ip_bin_mask[:no_ones] + "1" * no_zeros

    network_add_bin_octet = []
    broadcast_binoct = []

    [network_add_bin_octet.append(i) for i in [network_add_bin[j:j+8] for j in range(0, len(network_add_bin), 8)]]
    [broadcast_binoct.append(i) for i in [broadcast_add_bin[j:j+8] for j in range(0,len(broadcast_add_bin),8)]]

    network_add_dec_final = ".".join([str(int(i,2)) for i in network_add_bin_octet])
    broadcast_add_dec_final = ".".join([str(int(i,2)) for i in broadcast_binoct])

    # Calculate the host IP range
    first_ip_host = network_add_bin_octet[0:3] + [(bin(int(network_add_bin_octet[3],2)+1).split("b")[1].zfill(8))]
    first_ip = ".".join([str(int(i,2)) for i in first_ip_host])

    last_ip_host = broadcast_binoct[0:3] + [bin(int(broadcast_binoct[3],2) - 1).split("b")[1].zfill(8)]
    last_ip = ".".join([str(int(i,2)) for i in last_ip_host])

    # print all the computed results
    print("\nThe entered ip address is: " + input_ip)
    print("The entered subnet mask is: " + input_subnet)
    print("Calculated number of hosts per subnet: {0}".format(str(no_hosts)))
    print("Calculated number of mask bits: {0}".format(str(no_ones)))
    print("Calculated wildcard mask is: {0}".format(wildcard))
    print("The Network address is: {0}".format(network_add_dec_final))
    print("The Broadcast address is: {0}".format(broadcast_add_dec_final))
    print("IP address range is: {0} - {1}".format(first_ip, last_ip))
    print("Maximum number of subnets is: " + str(2**abs(24 - no_ones)))

def main():
    calculate_subnet(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()