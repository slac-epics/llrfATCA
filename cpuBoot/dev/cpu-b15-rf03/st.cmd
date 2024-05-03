#==============================================================
#
#  Abs:  Startup Script for cpu-b15-rf03 (stn 10-4,10-5)
#
#  Name: st.cmd
#
#  Desc: The processor is an Advantech 1U server,
#        SKY-8100 S industrial pc/server.
#
#  Facility:  EED Klystron Controls
#
#  Auth: 11-Jun-2020, Kristi Luchini  (LUCHINI)
#  Rev:  dd-mmm-yyyy, Reviewer's Name (USERNAME)
#--------------------------------------------------------------
#  Mod:
#        18-Aug-2020, Ernest Williams (ERNESTO)
#         chg eth0 and eth1 to eth5 and eth6
#         raise priority of eth5 and eth6
#         increase receiver buffer size
#
#=============================================================

# Turn on local IPMI Client support
echo "Load IPMI..."
sleep 10
modprobe ipmi_devintf
ipmitool lan print

# Ethernet configuraiton
# Self Manager Crate ID:0001, Branch=0, ID=1, eth5
ifconfig eth5 10.0.1.1 netmask 255.255.255.0 up

# Self Manager Crate ID:0101, Branch=1, ID=1, eth6
ifconfig eth6 10.1.1.1 netmask 255.255.255.0 up

# ==================================================================
# escalating RT priority for network kernel threads (SCHED_FIFO, 84)
# =================================================================
for PID in  $(ps -elF | grep eth5 | grep -v grep | awk '{print $4}'); do chrt -f -p 84 $PID ; done
for PID in  $(ps -elF | grep eth6 | grep -v grep | awk '{print $4}'); do chrt -f -p 84 $PID ; done

# ======================================
# increasing receive buffer size to 10MB
# ======================================
sysctl -w net.core.rmem_default=10485760

# wait a bit to device become visible
sleep 2

# End of script'


