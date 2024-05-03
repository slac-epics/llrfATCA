import get_pvname
from epics import caput

# In the UED 1080 Hz Timing Panel, this code should be the only place
# to set EPICS PV values. But there are other locations that do this.

def set_enable(get_pvname_instance, channel_number, checked):
    # Input: instance of GetPVName, string
    # Output: None
    # Received command from the UI. Send command to EPICS.
    
    ch = get_pvname_instance.get_enable_ch_pvname(channel_number)
    trg = get_pvname_instance.get_enable_trg_pvname(channel_number)

    if (checked == True):
        print('Enabling', channel_number)
        caput(ch, 1)
        caput(trg, 1)
    else:
        print('Disabling', channel_number)
        caput(ch, 0)
        caput(trg, 0)
