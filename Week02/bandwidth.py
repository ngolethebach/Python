# Bandwidth

max_network=1000
user=200
app_a=200000
app_b=100000
new_app=350000
max_network_bps=max_network*1000000
current_use=(app_a+app_b)*user
current_available=max_network_bps-((app_a*user)+(app_b*user))
print("The network capacity is: {} bps".format(max_network*100000))
print("The current usage of the network is: {} bps".format(current_use))
print("The current available is: {} bps".format(current_available))
print("The new app will use: {} bps".format(new_app*user))
print("The remaining bandwidth with the new application installed is: {} mbps".format((current_available - (new_app * user))/1000000)) 



























