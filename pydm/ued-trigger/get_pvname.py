import json

# Given the config file, get the EPICS PV names.

class GetPVName:
    def __init__(self, prefix):
        with open('get_pvname.json') as f:
            self.json = json.load(f)

        self.prefix = prefix

    def get_polarity_pvname(self, channel_number):
        return self.prefix + ":TRG" + channel_number + "_TPOL"
    
    def get_delay_pvname(self, channel_number):
        return self.prefix + ":TRG" + channel_number + "_SYS2_TDES"

    def get_width_pvname(self, channel_number):
        return self.prefix + ":TRG" + channel_number + "_SYS2_TWID"

    def get_ratemode_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_RATEMODE"

    def get_seqnum_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_SEQNUM"

    def get_seqbit_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_SEQBIT"
    
    def get_acrate_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_ACRATE"

    def get_tsmask_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_TSMASK"

    def get_enable_ch_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_SYS2_TCTL"
    
    def get_enable_trg_pvname(self, channel_number):
        return self.prefix + ":TRG" + channel_number + "_SYS2_TCTL"

    def get_description_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_SYS2_TCTL.DESC"
    
    def get_current_rate_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_CNT"
    
    def get_destmode_pvname(self, channel_number):
        return self.prefix + ":CH" + channel_number + "_DESTMODE"
