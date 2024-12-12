import ast
import AugmentingPath as ap
import CapacityScaling as cs
import PreflowPush as pp
import time
import matplotlib.pyplot as plt
import numpy as np


def parse_network_info(file_path):
    networks = []
    with open(file_path, 'r') as file:
        content = file.read().splitlines()
        fsrep = []
        point = []
        for line in content:
            if not line.strip():
                continue
            if line.startswith("Network"):
                if fsrep and point:
                    networks.append((fsrep, point))
                fsrep = []
                point = []
            elif line.startswith("fsrep:"):
                fsrep = ast.literal_eval(line.split(":")[1].strip())
            elif line.startswith("point:"):
                point = ast.literal_eval(line.split(":")[1].strip())
        if fsrep and point:
            networks.append((fsrep, point))

    return networks


file_path = "random_networks_output.txt"
networks = parse_network_info(file_path)


def measure_runtime(networks, ap, cs, pp):
    network_sizes = []
    avg_ap_times = []
    avg_cs_times = []
    avg_pp_times = []

    for network_size in range(1, 21):
        print(f'Running networks with {10 * network_size} nodes')
        ap_times = []  # Store run times for Augmented Path for current network_size
        cs_times = []  # Store run times for Capacity Scaling for current network_size
        pp_times = []  # Store run times for Preflow Push for current network_size

        # Run 50 iterations for the current network size
        for iteration in range(50):
            print(f'Iteration: {iteration + 1}')
            index = 50 * (network_size - 1) + iteration
            fsrep, point = networks[index]
            # Measure Augmented Path runtime
            start_time = time.time()
            ap.augpath(np.array(fsrep), np.array(point), 1, 10 * network_size)
            ap_times.append(time.time() - start_time)
            # Measure Capacity Scaling runtime
            start_time = time.time()
            cs.capacityscaling(np.array(fsrep), np.array(point), 1, 10 * network_size)
            cs_times.append(time.time() - start_time)
            # Measure Preflow Push runtime
            start_time = time.time()
            pp.preflowpush(np.array(fsrep), np.array(point), 1, 10 * network_size)
            pp_times.append(time.time() - start_time)

        # Average times for the current network size
        avg_ap_times.append(sum(ap_times) / len(ap_times))
        avg_cs_times.append(sum(cs_times) / len(cs_times))
        avg_pp_times.append(sum(pp_times) / len(pp_times))

        # Store the network size
        network_sizes.append(10 * network_size)
    return network_sizes, avg_ap_times, avg_cs_times, avg_pp_times


network_sizes, avg_ap_times, avg_cs_times, avg_pp_times = measure_runtime(networks, ap, cs, pp)


plt.figure(figsize=(10, 6))
plt.plot(network_sizes, avg_ap_times, label='Augmented Path', color='r')
plt.plot(network_sizes, avg_cs_times, label='Capacity Scaling', color='g')
plt.plot(network_sizes, avg_pp_times, label='Preflow Push', color='b')
plt.xlabel('Network Size')
plt.ylabel('Average Run Time (seconds)')
plt.title('Average Run Time vs. Network Size for Different Algorithms')
plt.legend()
plt.grid(True)
plt.show()
