
---

## ✏️ 01_custom_topology/README.md

```markdown
# 01. Custom Topology Programming

**Objectives:**
- Define my own topology in Python using the `Topo` class
- Add hosts, switches, and links to a python script
- Use `mininet.util` helpers to inspect and test connectivity

**Files:**
- `custom_topo.py`: script

### Running the Example

```bash
cd 01_custom_topology
sudo python3 custom_topo.py
```

![CustomTopo](/01_custom_topology/CustomTopo.png)


# 01. Custom Topology Programming

When I execute `custom_topo.py`, Mininet performs the following steps (with corresponding console output):

```text
*** Creating network
```

* Initializes the Mininet environment: creates network namespaces, virtual Ethernet (veth) pairs, and prepares for controllers and switches.

```text
*** Adding controller
```

* Launches the default OpenFlow controller (`c0`), which will manage flow rules on the switch.

```text
*** Adding hosts:
    h1 h2
*** Adding switches:
    s1
*** Adding links:
    (h1, s1) (h2, s1)
```

* Adds two host nodes (`h1`, `h2`) and one switch node (`s1`) to the topology.
* Creates virtual links: `h1`↔`s1` and `h2`↔`s1`.

```text
*** Configuring hosts
```

* Assigns default IP addresses (e.g., `10.0.0.1/8` for `h1` and `10.0.0.2/8` for `h2`) and brings up the interfaces.

```text
*** Starting controller
c0
*** Starting 1 switches
s1 ...
```

* Starts the controller process and the Open vSwitch instance representing `s1`.

```text
Dumping host connections
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
```

* Uses `dumpNodeConnections(net.hosts)` to list each host’s interface and the switch port it’s connected to.

```text
Testing network connectivity
*** Ping: testing ping reachability
h1 -> h2 : 0% packet loss
h2 -> h1 : 0% packet loss
*** Results: 0% dropped (2/2 received)
```

* Executes `net.pingAll()` to run a simple ICMP ping between every pair of hosts and reports packet‑loss statistics.

```text
*** Stopping 1 controllers
c0
*** Stopping 2 links
*** Stopping 1 switches
s1
*** Stopping 2 hosts
h1 h2
*** Done
```

* Cleans up: stops the controller, tear downs the virtual links, switches, and hosts, and removes network namespaces.

---

## Running the Example

1. Ensure Mininet is installed and working:

   ```bash
   which mn        # should return /usr/local/bin/mn or /usr/bin/mn
   mn --version    # verify version
   ```
2. Navigate to this directory and run the script with root privileges:

   ```bash
   cd 01_custom_topology
   sudo python3 custom_topo.py
   ```

## What I’re Learning

* **Python‑based Topology Definition:** Using the `Topo` class and methods like `addHost()`, `addSwitch()`, and `addLink()` to programmatically build network laIts.
* **Mininet API Workflow:** Instantiating `Mininet()`, calling `net.start()`, inspecting with utilities (`dumpNodeConnections`, `net.pingAll()`), and cleaning up with `net.stop()`.
* **Controller & Switch Interaction:** Observing how Mininet launches an OpenFlow controller and connects it to an OVS switch for flow management.
* **Virtual Network Internals:** Understanding network namespaces, veth pairs, and how Mininet emulates L2 connectivity.
* **Debugging & Verification:** Interpreting Mininet’s console output to verify that hosts can reach each other and that the virtual topology behaves as expected.

---

*From here, I can extend the lab by adding more hosts, changing link parameters, or integrating a custom controller script.*
