---
## ✏️ 03_controller_integration/README.md

```markdown
# 03. Controller Integration

**Objectives:**
- Connect Mininet switches to two remote OpenFlow controllers (Ryu simple_switch_13 instances).  
- Assign primary and backup controllers to different switches for failover.  
- Demonstrate controller failover with no interruption to host-to-host connectivity.

**Files:**
- `controller_integration.py`: script

### Running the Example

```bash
cd 03_controller_integration
sudo python3 controller_integration.py
```

![ControllerIntegration](/03_controller_integration/ControllerIntegration.png)

# 03. Controller Integration

When I execute `controller_integration.py`, Mininet performs the following steps (with corresponding console output):

```text
*** Creating network
*** Adding hosts:
    h1 h2 h3 h4
*** Adding switches:
    s1 s2
*** Adding links:
    (h1, s1) (h2, s1) (h3, s2) (h4, s2) (s1, s2)
*** Configuring hosts
    h1 h2 h3 h4
```
* Instantiates four hosts and two OVS switches, linking each host to its switch and bridging the two switches.

```text
*** Starting controllers
  c0 -> 127.0.0.1:6633
  c1 -> 127.0.0.1:6634
```
* Connects to two running Ryu controllers (OF 1.3 simple_switch_13) as `c0` (primary) and `c1` (backup).

```text
*** Starting switches
s1 s2 ...
```
* Starts each switch, passing them the controller list.  
* `s1` uses `[c0, c1]` (primary c0, backup c1).  
* `s2` uses `[c1, c0]` (primary c1, backup c0).

```text
*** Dumping host connections
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s2-eth1
h4 h4-eth0:s2-eth2
```
* Uses `dumpNodeConnections(net.hosts)` to list each host’s interface and its connected switch port.

```text
*** Testing network connectivity (pingAll)
*** Ping: testing ping reachability
h1 -> h2 h3 h4
h2 -> h1 h3 h4
h3 -> h1 h2 h4
h4 -> h1 h2 h3
*** Results: 0% dropped (12/12 received)
```
* Verifies end-to-end connectivity across the two-switch topology under the primary controllers.

```text
*** Simulating failover: stopping primary controller c0
```
* Stops `c0`, forcing both switches to reconnect to `c1`.

```text
*** Testing connectivity after failover (pingAll)
*** Ping: testing ping reachability
h1 -> h2 h3 h4
h2 -> h1 h3 h4
h3 -> h1 h2 h4
h4 -> h1 h2 h3
*** Results: 0% dropped (12/12 received)
```
* Confirms that switching over to the backup controller causes no packet loss.

```text
*** Stopping network
```
* Cleans up controllers, switches, links, and namespaces.

---

## Running the Example

1. **Ensure Ryu controllers are running** on ports 6633 and 6634:
   ```bash
   source ~/mininet-ryu-env/bin/activate
   ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13 &
   ryu-manager --ofp-tcp-listen-port 6634 ryu.app.simple_switch_13 &
   ```
2. **Run the integration script**:
   ```bash
   cd 03_controller_integration
   sudo python3 controller_integration.py
   ```

## What I’m Learning

* **Multi-Controller Topologies:** How to assign different controllers (primary/backup) to switches.  
* **OpenFlow Versioning:** Ensuring both OVS and Ryu use OF 1.3 for compatibility.  
* **Failover Mechanics:** Observing seamless switch reconnection when the primary controller stops.  
* **Debugging & Verification:** Using `dumpNodeConnections` and `pingAll()` to validate network and failover behavior.

---
