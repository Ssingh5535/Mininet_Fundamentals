# Mininet Fundamentals

A hands‑on collection of Mininet labs demonstrating intermediate skills and concepts in software‑defined networking (SDN). Each lab builds on the previous, showcasing:

1. **Custom Topology Programming**  
   Write Python scripts using the Mininet API (`Topo`, `addHost()`, `addSwitch()`, `addLink()`) and utilities like `dumpNodeConnections()` and `pingAll()`.

2. **Advanced Link Configuration**  
   Create links with custom bandwidth, latency, loss, and queue parameters; apply traffic shaping with Linux `tc`.

3. **Controller Integration**  
   Connect your Mininet network to remote OpenFlow controllers (e.g., Ryu), assign primary/backup controllers, and experiment with failover.

4. **Automating Experiments**  
   Use `mn` CLI batch mode, script CLI commands in Python (`CLI.doBatch()`), and integrate Mininet runs into shell or Python test suites.

---

## Repository Structure

```
.
├── 01_custom_topology
│   ├── custom_topo.py
│   └── README.md
├── 02_advanced_link_config
│   ├── link_config.py
│   └── README.md
├── 03_controller_integration
│   ├── controller_integration.py
│   └── README.md
├── 04_automating_experiments
│   ├── automated_experiments.py
│   ├── commands.txt
│   └── README.md
└── README.md        # <- you are here
```

---

## Prerequisites

- **Operating System:** Ubuntu 20.04+ (or any Debian‑based Linux)  
- **Python:** 3.9 (recommended)  
- **Mininet:** network emulator  
- **Open vSwitch:** for software switching  
- **Ryu:** OpenFlow controller framework  

### Install System Dependencies

```bash
sudo apt-get update
sudo apt-get install -y \
    python3.9 python3.9-venv python3.9-distutils python3.9-dev \
    mininet openvswitch-switch \
    git
```

---

## Python Environment Setup

Create and activate a virtual environment to isolate dependencies:

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install ryu
```

---

## Running the Labs

Each lab directory contains its own `README.md` with detailed instructions. To get started:

1. **Custom Topology Programming**

   ```bash
   cd 01_custom_topology
   sudo python3 custom_topo.py
   ```

2. **Advanced Link Configuration**

   ```bash
   cd ../02_advanced_link_config
   sudo python3 link_config.py
   ```

3. **Controller Integration**

   - Start two Ryu controllers in separate terminals:

     ```bash
     source ../venv/bin/activate
     ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13 &
     ryu-manager --ofp-tcp-listen-port 6634 ryu.app.simple_switch_13 &
     ```

   - Run the integration script:

     ```bash
     cd ../03_controller_integration
     sudo python3 controller_integration.py
     ```

4. **Automating Experiments**

   ```bash
   cd ../04_automating_experiments
   sudo python3 automated_experiments.py
   ```

---
