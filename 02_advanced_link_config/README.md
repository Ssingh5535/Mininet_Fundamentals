---

## 02_advanced_link_config

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
*** Adding links: (h1, s1) (s1, h2)
```
* Adds two hosts and one switch, then connects h1↔s1 and s1↔h2 with custom link parameters (`bw=10`, `delay=5ms`, `loss=1%`, `max_queue_size=100`).

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
*** Testing default ping with configured link parameters
h1 -> h2 : 0% packet loss
h2 -> h1 : 0% packet loss
```
* Executes `net.pingAll()` under link constraints.

```text
*** Testing bandwidth with iperf
h1 -> h2 : 9.22 Mbits/sec
h2 -> h1 : 9.18 Mbits/sec
```
* Runs `iperf` to measure throughput, verifying the 10 Mbps limit.

```text
*** Stopping network
```
* Cleans up the network and namespaces.

---

## Running the Example

1. Ensure Mininet is installed and working:

   ```bash
   which mn        # should return /usr/local/bin/mn or /usr/bin/mn
   mn --version    # verify version
   ```

2. Navigate here and run:

   ```bash
   cd 02_advanced_link_config
   sudo python3 link_config.py
   ```

## What I'm Learning

* **Emulated Link Properties:** Using `TCLink` parameters (`bw`, `delay`, `loss`, `max_queue_size`) to simulate real-world link characteristics.  
* **Traffic Shaping with `tc`:** Applying Linux `tc` commands (TBF, RED) to host interfaces for rate-limiting and queue management.  
* **Performance Measurement:** Interpreting `pingAll()` and `iperf` results under constrained link conditions.  
* **Experimentation & Debugging:** Tweaking link configurations and observing effects on latency, packet loss, and throughput.

---
```
