# Computer Networks

## Analyzed TCP Traffic



To implement the topology described in `topo-2sw-2host.py`, we need to activate the POX controller. POX is a Python-based networking software platform used for implementing the OpenFlow protocol, which standardizes communication between switches and controllers.

Command to activate POX controller:
`
sudo ~/pox/pox.py forwarding.l2_learning openflow.spanning_tree --no-flood --hold-down log.level --DEBUG samples.pretty_log openflow.discovery host_tracker info.packet_dump
Command to create the Mininet environment:`

`sudo mn --custom ~/mininet/custom/topo-2sw-2host.py --topo mytopo --mac --switch ovsk --controller remote`

Verifying Topology:

Run a Mininet command like (replace paths with yours):

`
sudo mn --custom ~/mininet/custom/topo-2sw-2host.py --topo mytopo --mac --switch ovsk --controller remote`
## Traffic Shaping and Observation
A. Simulating Bottleneck
`
h1 tc qdisc add dev h1-eth0 root tbf rate 1mbit burst 1000kbit latency 10ms`
B. Measuring Bandwidth with iperf
Use iperf to measure bandwidth between specific nodes (replace with your command).

C. Packet Capture with Wireshark
Capture packets using sudo wireshark to analyze communication details.

D. Congestion Window Plot
Refer to the provided Python script for the plot between congestion window and time.
![Figure 1](https://github.com/Yogender21505/Analyzed-TCP-Traffic/blob/assets/104339650/dc679ac7-d471-4f2a-a20a-8ec180801f21.png)



Instructions for Use:
Copy the above Markdown content.
Create a new file named README.md in your GitHub repository.
Paste the content into the README.md file.
Ensure all referenced image files (dc679ac7-d471-4f2a-a20a-8ec180801f21.png, etc.) are placed in the correct directory (assets/104339650/ in this case) relative to README.md within your GitHub repository.
