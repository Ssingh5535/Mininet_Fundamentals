#!/usr/bin/env python3

from mininet.topo import Topo
from mininet.net  import Mininet
from mininet.util import dumpNodeConnections
from mininet.log  import setLogLevel

class CustomTopo(Topo):
    def build(self):
        # Create 2 hosts and 1 switch
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        # Link hosts to switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = CustomTopo()
    net  = Mininet(topo=topo)
    net.start()

    print("Dumping host connections")
    dumpNodeConnections(net.hosts)

    print("Testing network connectivity")
    net.pingAll()

    net.stop()
