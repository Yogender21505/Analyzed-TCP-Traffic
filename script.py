import pyshark
import matplotlib.pyplot as plt

def process_packets(cap):
    time_list = []
    cwnd_list = []

    for packet in cap:
        if 'TCP' in packet:
            try:
                time = float(packet.sniff_timestamp)
                cwnd = int(packet.tcp.window_size)

                time_list.append(time)
                cwnd_list.append(cwnd)
            except Exception as e:
                print(f"Error processing packet: {e}")

    return time_list, cwnd_list

def plot_congestion_window(file_path, line_color='blue'):
    try:
        cap = pyshark.FileCapture(file_path)
        time_list, cwnd_list = process_packets(cap)

        # Plotting with specified line color
        plt.plot(time_list, cwnd_list, color=line_color)
        plt.title('Congestion Window vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Congestion Window Size')
        plt.show()
    except Exception as e:
        print(f"Error plotting congestion window: {e}")

# Example usage with a different color (e.g., red)
capture_file_path = 'h1_h6_1mb.pcap'
plot_congestion_window(capture_file_path, line_color='red')

