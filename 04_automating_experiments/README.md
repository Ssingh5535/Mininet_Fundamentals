# 04. Automating Experiments

**Objectives:**
- Automate Mininet experiments non-interactively using a batch file and Python scripting.
- Demonstrate link shaping with `TCLink` and validate connectivity with `pingAll` and `iperf`.
- Integrate Mininet runs into shell or Python workflows for repeatable testing.

**Files:**
- `automated_experiments.py`: Python script that builds a shaped-link topology, runs a custom batch of Mininet commands, and performs an `iperf` test via the Python API.
- `commands.txt`: List of CLI commands (`pingall`, `iperf h1 h2`, `exit`) used by the script.
- `run_experiments.sh`: (Optional) Shell wrapper demonstrating Mininet’s built-in `--batch` mode.
- `AutomatedExperiments.png`: Screenshot of the experiment’s console output.

---

## Running the Example

1. **Ensure Mininet is installed** (and you have root privileges):
   ```bash
   which mn
   mn --version
   ```
2. **Run the automated script**:
   ```bash
   cd 04_automating_experiments
   sudo python3 automated_experiments.py
   ```
   This will:
   - Create a two-host, one-switch topology with 5 Mbps bandwidth, 10 ms delay, 2% loss.
   - Dump host connections.
   - Execute `pingall` and `iperf h1 h2` by reading `commands.txt`.
   - Start an `iperf` server on `h2` and a client on `h1` via the Python API.

3. **Observe the result**:

   ![AutomatedExperiments](AutomatedExperiments.png)

   In this run you can see:
   - **0% Packet Loss** on the `pingall` test.
   - Measured **~2.07 Mbits/sec** bandwidth for the `iperf` test (reflecting the 5 Mbps link with some overhead).

---

## What I’m Learning

- **Batch Automation:** How to drive Mininet’s CLI commands from a file for repeatable tests.  
- **Python API Scripting:** Using `mininet.net.Mininet` and host-level `cmd()` to automate experiments.  
- **Link Shaping:** Modeling network characteristics (bandwidth, delay, loss) with `TCLink`.  
- **Performance Validation:** Combining `pingAll` and `iperf` to verify that emulated constraints are in effect.

---

*End of 04. Automating Experiments README*
