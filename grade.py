total_data = 
packet_size = 
drop_rate = 
T_latency = 
line_rate = 

P_th = ceil(total_data/packet_size)
#  Medium 1Mb/s, 10 ms, 50% reorder 10% drop
P_min = 2 * P_th * (1 + drop_rate)
T_min = P_th * (1 + drop_rate) * (T_latency + packet_size/line_rate)