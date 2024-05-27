from os import error
import string


class Net_addr:
    
    def __init__(self, ip_addr, mask):
        net_addr = self.translate(ip_addr, mask)
        self.netaddr = net_addr
    
    def translate(self, ipad, mask):
        ## consider that both the ip_address and mask are uint_8 array
        net_address = []
        for ia, m in zip(ipad, mask):
            if ia > 255 or m > 255 : 
                return None
            res = ia & m 
            net_address.append(res)
        
        return net_address
    
    def __eq__(self, other):
        if isinstance(other, Net_addr):
            return self.netaddr == other.netaddr
        return False

    def __hash__(self):
        return hash(tuple(self.netaddr))
        
"""
The routing table contains the map of 
    <network_address> : <ropute_string>
"""
class RoutingTable:
    
    #initialise the Routing table
    def __init__(self):
        self.map = {}
    
    # add to routing table
    def add_route(self, net_addr: Net_addr, route: string):
        # update the value in map
        self.map[net_addr] = route
            
        
    def get_route(self, net_addr):
        #if not in map return error
        #else return route
        if net_addr not in self.map.keys():
            return (-1, "not in table")
        else: 
            return (0, "Send packets to :" + self.map[net_addr])
    
    def print_routing_table(self):
        print(self.map)


def main():
    
    # initialise a hash routing table 
    rt = RoutingTable()

    # add network address and route info to the routing table
    ip_address = [10,10,1,1]
    mask = [255, 255, 255, 0]
    net_addr = Net_addr(ip_address, mask)
    rt.add_route(net_addr, "eno1")
    ip_address = [10,10,3,2]
    mask = [255, 255, 255, 0]
    net_addr = Net_addr(ip_address, mask)
    rt.add_route(net_addr, "en1")
    ip_address = [192,12,3,23]
    mask = [255, 255, 12, 0]
    net_addr = Net_addr(ip_address, mask)
    rt.add_route(net_addr, "eno4")

    # when provided the network address get the relevant route for the network address 
    ip_address = [10,10,1,1]
    mask = [255, 255, 255, 0]
    net_addr = Net_addr(ip_address, mask)
    
    ret_val, ret = rt.get_route(net_addr)
    if ret_val >= 0:
        print(ret)
    else:
        print(ret)

    
if __name__ == "__main__":
    main()



