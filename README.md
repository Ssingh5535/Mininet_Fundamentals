# Mininet Fundamentals

A hands‑on collection of Mininet labs demonstrating intermediate skills:

1. **Custom Topology Programming**  
   Write Python scripts using the Mininet API (`Topo`, `addHost()`, `addSwitch()`, `addLink()`) and utilities like `dumpNodeConnections()` and `pingAll()`.

2. **Advanced Link Configuration**  
   Create links with custom bandwidth, latency, loss and queue parameters; apply traffic shaping with Linux `tc`.

3. **Controller Integration**  
   Connect your Mininet network to Ryu controllers, run multiple controllers, and experiment with failover.

4. **Automating Experiments**  
   Use batch mode (`mn --custom`), script CLI commands in Python, and integrate Mininet runs into your test suites.

---

## Prerequisites

```bash
sudo apt-get update
sudo apt-get install -y mininet git python3-pip
pip3 install ryu  # or other controller libs you plan to use
