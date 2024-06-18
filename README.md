# Computer Networks

## Analyzed TCP Traffic

**A. POX Controller Activation**

```bash
sudo ~/pox/pox.py forwarding.l2_learning openflow.spanning_tree --no-flood --hold-down log.level --DEBUG samples.pretty_log openflow.discovery host_tracker info.packet_dump
Use code with caution.
content_copy
B. Verifying Topology

Run a Mininet command like (replace paths with yours):

```bash
sudo mn --custom ~/mininet/custom/topo-2sw-2host.py --topo mytopo --mac --switch ovsk --controller remote
Use code with caution.
content_copy
Question 2: Traffic Shaping and Observation
A. Simulating Bottleneck

Bash
h1 tc qdisc add dev h1-eth0 root tbf rate 1mbit burst 1000kbit latency 10ms
Use code with caution.
content_copy
B. Measuring Bandwidth with iperf

Use iperf to measure bandwidth between specific nodes (replace with your command).

C. Packet Capture with Wireshark

Capture packets using sudo wireshark to analyze communication details.

D. Congestion Window Plot

Refer to the provided Python script for the plot between congestion window and time.
![Figure_1](https://github.com/Yogender21505/Analyzed-TCP-Traffic/assets/104339650/dc679ac7-d471-4f2a-a20a-8ec180801f21)
