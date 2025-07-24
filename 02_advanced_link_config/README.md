
## ✏️ 02_advanced_link_config/README.md

```markdown
# 02. Advanced Link Configuration

**Objectives:**
- Specify custom bandwidth, latency, packet loss, and queue size using the `TCLink` class.
- Perform traffic shaping and policing with Linux `tc` (Hierarchical Token Bucket, RED, etc.) on Mininet interfaces.

**Files:**
- `link_config.py`: script

### Running the Example

```bash
cd 02_advanced_link_config
sudo python3 link_config.py
```

![LinkConfig](/02_advanced_link_config/LinkConfig.png)

# 02. Advanced Link Configuration

When I execute `link_config.py`, Mininet performs the following steps (with corresponding console output):

```text
*** Creating network
```
* Initializes the Mininet environment, setting up namespaces and veth pairs.

```text
*** Adding controller
```
* Launches the default OpenFlow controller (`c0`).

```text
*** Adding hosts: h1 h2
*** Adding switches: s1
*** Adding links: (10.00Mbit 5ms delay 1.00000% loss) (10.00Mbit 5ms delay 1.00000% loss) (h1, s1) (10.00Mbit 5ms delay 1.00000% loss) (10.00Mbit 5ms delay 1.00000% loss) (s1, h2)
```
* Adds two hosts and one switch, then connects `h1↔s1` and `s1↔h2` with exactly one `TCLink` qdisc per link configured for 10 Mbps, 5 ms delay, 1% loss, 100‑packet queue.

```text
*** Configuring hosts
```
* Assigns IPs (e.g., `10.0.0.1/8` and `10.0.0.2/8`) and brings up interfaces.

```text
*** Starting controller
c0
*** Starting 1 switches
s1 ...
```
* Starts the controller and the switch.

```text
*** Dumping host connections
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
```
* Uses `dumpNodeConnections(net.hosts)` to list each host’s interface and its switch port.

```text
*** Testing network connectivity (pingAll)
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
```
* Executes `net.pingAll()` under the configured link constraints.

```text
*** Iperf: testing TCP bandwidth h1 → h2
```
* Runs a single-direction `iperf` (h1→h2) to measure throughput.

```text
*** Results: 5.2 Mbits/sec
*** Results: 5.1 Mbits/sec
```
* Verifies that the measured bandwidth is close to the 10 Mbps limit.

```text
*** Stopping network
```
* Cleans up the network and namespaces.

---

## Running the Example

1. Ensure Mininet (with `iperf`) is installed and working:

   ```bash
   which mn        # should return /usr/local/bin/mn or /usr/bin/mn
   mn --version    # verify version
   which iperf     # ensure the legacy iperf is present
   ```

2. Navigate here and run:

   ```bash
   cd 02_advanced_link_config
   sudo python3 link_config.py
   ```

## What I'm Learning

* **Emulated Link Properties:** Using a single `TCLink` per link (`bw`, `delay`, `loss`, `max_queue_size`) to model real‑world characteristics.  
* **Traffic Shaping with `tc`:** Applying Linux `tc` commands (TBF, RED) for fine‑grained rate control and queue management.  
* **Performance Measurement:** Running `net.pingAll()` and a unidirectional `iperf` to validate latency, packet loss, and throughput under constrained conditions.  
* **Experimentation & Debugging:** Controlling exactly where and how many qdiscs are applied, and parsing iperf output reliably with regex-based numeric extraction.

---
