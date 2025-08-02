#!/usr/bin/env python3

"""
04. Automating Experiments – Fixed

This version starts a default Controller so that OVS will learn MACs
and forward packets between h1 and h2.
"""

import time
from mininet.net   import Mininet
from mininet.topo  import Topo
from mininet.link  import TCLink
from mininet.util  import dumpNodeConnections
from mininet.node  import Controller
from mininet.log   import setLogLevel

class SimpleTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        opts = dict(bw=5, delay='10ms', loss=2, max_queue_size=50)
        self.addLink(h1, s1, cls=TCLink, **opts)
        self.addLink(s1, h2, cls=TCLink, **opts)

def run_batch(net, filename):
    print(f"\n*** Running batch from {filename}")
    with open(filename) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            print(f"*** batch> {line}")
            parts = line.split()
            cmd = parts[0].lower()
            if cmd == 'pingall':
                net.pingAll()
            elif cmd == 'iperf' and len(parts) == 3:
                h1, h2 = net.get(parts[1]), net.get(parts[2])
                print(f"*** iperf test: {parts[1]} -> {parts[2]}")
                # start iperf server on h2
                h2.cmd('iperf -s -t 5 &')
                # client on h1
                out = h1.cmd(f'iperf -c {h2.IP()} -t 5')
                print(out)
            elif cmd == 'exit':
                break
            else:
                print(f"*** Unknown batch command: {line}\n")

if __name__ == '__main__':
    setLogLevel('info')

    # 1) Create the network WITH a default (reference) controller
    net = Mininet(
        topo=SimpleTopo(),
        link=TCLink,
        controller=Controller   # <— start an OVS testcontroller
    )
    net.start()

    print("\n*** Dumping host connections")
    dumpNodeConnections(net.hosts)

    # 2) Run  “batch” commands
    run_batch(net, 'commands.txt')

    # 3) A direct host‐level iperf 
    print("\n*** Running host‐level iperf via Python API")
    h1, h2 = net.get('h1', 'h2')
    h2.cmd('iperf -s -t 5 &')
    output = h1.cmd(f'iperf -c {h2.IP()} -t 5')
    print(output)

    # 4) Tear down
    net.stop()
