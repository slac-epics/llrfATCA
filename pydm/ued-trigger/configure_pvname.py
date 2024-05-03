import get_pvname
import set_pvname
from epics import caget, caput, cainfo
import json

class ConfigurePVName:
    def __init__(self, prefix):
      	  self.get_pvname_instance = get_pvname.GetPVName(prefix)

    def configure_polarity(self, ui):        
        ui.ch0_polarity.channel = self.get_pvname_instance.get_polarity_pvname("00")
        ui.ch1_polarity.channel = self.get_pvname_instance.get_polarity_pvname("01")
        ui.ch2_polarity.channel = self.get_pvname_instance.get_polarity_pvname("02")
        ui.ch3_polarity.channel = self.get_pvname_instance.get_polarity_pvname("03")
        ui.ch4_polarity.channel = self.get_pvname_instance.get_polarity_pvname("04")
        ui.ch5_polarity.channel = self.get_pvname_instance.get_polarity_pvname("05")
        ui.ch6_polarity.channel = self.get_pvname_instance.get_polarity_pvname("06")
        ui.ch7_polarity.channel = self.get_pvname_instance.get_polarity_pvname("07")
        ui.ch8_polarity.channel = self.get_pvname_instance.get_polarity_pvname("08")
        ui.ch9_polarity.channel = self.get_pvname_instance.get_polarity_pvname("09")
        ui.ch10_polarity.channel = self.get_pvname_instance.get_polarity_pvname("10")
        ui.ch11_polarity.channel = self.get_pvname_instance.get_polarity_pvname("11")
        ui.ch12_polarity.channel = self.get_pvname_instance.get_polarity_pvname("12")
        ui.ch13_polarity.channel = self.get_pvname_instance.get_polarity_pvname("13")
        
    def configure_width(self, ui):        
        ui.ch0_width.channel = self.get_pvname_instance.get_width_pvname("00")
        ui.ch1_width.channel = self.get_pvname_instance.get_width_pvname("01")
        ui.ch2_width.channel = self.get_pvname_instance.get_width_pvname("02")
        ui.ch3_width.channel = self.get_pvname_instance.get_width_pvname("03")
        ui.ch4_width.channel = self.get_pvname_instance.get_width_pvname("04")
        ui.ch5_width.channel = self.get_pvname_instance.get_width_pvname("05")
        ui.ch6_width.channel = self.get_pvname_instance.get_width_pvname("06")
        ui.ch7_width.channel = self.get_pvname_instance.get_width_pvname("07")
        ui.ch8_width.channel = self.get_pvname_instance.get_width_pvname("08")
        ui.ch9_width.channel = self.get_pvname_instance.get_width_pvname("09")
        ui.ch10_width.channel = self.get_pvname_instance.get_width_pvname("10")
        ui.ch11_width.channel = self.get_pvname_instance.get_width_pvname("11")
        ui.ch12_width.channel = self.get_pvname_instance.get_width_pvname("12")
        ui.ch13_width.channel = self.get_pvname_instance.get_width_pvname("13")

    def configure_delay(self, ui):        
        ui.ch0_delay.channel = self.get_pvname_instance.get_delay_pvname("00")
        ui.ch1_delay.channel = self.get_pvname_instance.get_delay_pvname("01")
        ui.ch2_delay.channel = self.get_pvname_instance.get_delay_pvname("02")
        ui.ch3_delay.channel = self.get_pvname_instance.get_delay_pvname("03")
        ui.ch4_delay.channel = self.get_pvname_instance.get_delay_pvname("04")
        ui.ch5_delay.channel = self.get_pvname_instance.get_delay_pvname("05")
        ui.ch6_delay.channel = self.get_pvname_instance.get_delay_pvname("06")
        ui.ch7_delay.channel = self.get_pvname_instance.get_delay_pvname("07")
        ui.ch8_delay.channel = self.get_pvname_instance.get_delay_pvname("08")
        ui.ch9_delay.channel = self.get_pvname_instance.get_delay_pvname("09")
        ui.ch10_delay.channel = self.get_pvname_instance.get_delay_pvname("10")
        ui.ch11_delay.channel = self.get_pvname_instance.get_delay_pvname("11")
        ui.ch12_delay.channel = self.get_pvname_instance.get_delay_pvname("12")
        ui.ch13_delay.channel = self.get_pvname_instance.get_delay_pvname("13")

    def set_rate(self, chosen_rate, channel_number):
        ratemode_pvname = self.get_pvname_instance.get_ratemode_pvname(channel_number)
        ratemode = self.json['rate'][chosen_rate]['ratemode']
        caput(ratemode_pvname, ratemode)

        if self.json['rate'][chosen_rate]['ratemode'] == 'Seq':
            # The user chose one of the sequence mode rates.
            
            seqnum_pvname = self.get_pvname_instance.get_seqnum_pvname(channel_number)
            seqnum = self.json['rate'][chosen_rate]['seqnum']
            print('Sending', seqnum_pvname, seqnum)
            caput(seqnum_pvname, seqnum)
        
            seqbit_pvname = self.get_pvname_instance.get_seqbit_pvname(channel_number)
            seqbit = self.json['rate'][chosen_rate]['seqbit']
            print('Sending', seqbit_pvname, seqbit)
            caput(seqbit_pvname, seqbit)
            
        else:
            # The user chose one of the AC mode rates.
            
            acrate_pvname = self.get_pvname_instance.get_acrate_pvname(channel_number)
            acrate = self.json['rate'][chosen_rate]['acrate']
            caput(acrate_pvname, acrate)
        
            tsmask_pvname = self.get_pvname_instance.get_tsmask_pvname(channel_number)
            tsmask = self.json['rate'][chosen_rate]['tsmask']
            caput(tsmask_pvname, tsmask)
            
        # Always set the destmode to "Don't care" exactly.
        destmode_pvname = self.get_pvname_instance.get_destmode_pvname(channel_number)
        caput(destmode_pvname, "Don't care")
        
    def ch0_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "00")

    def ch1_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "01")

    def ch2_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "02")

    def ch3_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "03")

    def ch4_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "04")

    def ch5_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "05")

    def ch6_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "06")

    def ch7_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "07")

    def ch8_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "08")

    def ch9_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "09")

    def ch10_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "10")

    def ch11_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "11")

    def ch12_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "12")

    def ch13_set_rate(self, chosen_rate):
        self.set_rate(chosen_rate, "13")

    def set_initial_rate(self, which_widget, channel_number):
        # Figure out what current rate is for each channel.
        # This is very, very, imperfect, and borderline dangerous.
        # The better solution is to make one PV name that represents the rate,
        # but we currently have many PVs that represent the rate.

        keys = self.json['rate'].keys()

        ratemode_pvname = self.get_pvname_instance.get_ratemode_pvname(channel_number)
        ratemode = caget(ratemode_pvname, as_string=True)

        if ratemode == "Seq":
            # This channel is already set to Seq. Figure out which rate it is.
            seqnum_pvname = self.get_pvname_instance.get_seqnum_pvname(channel_number)
            seqnum = caget(seqnum_pvname, as_string=True)

            seqbit_pvname = self.get_pvname_instance.get_seqbit_pvname(channel_number)
            seqbit = caget(seqbit_pvname, as_string=True)

            for key in keys:
                if self.json['rate'][key]['ratemode'] == 'Seq':
                    matches_seqnum = self.json['rate'][key]['seqnum'] == seqnum
                    matches_seqbit = self.json['rate'][key]['seqbit'] == seqbit

                    if matches_seqnum and matches_seqbit:
                        print('Channel', channel_number, 'matched', key)
                        which_widget.setCurrentText(key)
            
        else:
            # This channel is already set to AC. Figure out which rate it is.
            acrate_pvname = self.get_pvname_instance.get_acrate_pvname(channel_number)
            acrate = caget(acrate_pvname, as_string=True)

            tsmask_pvname = self.get_pvname_instance.get_tsmask_pvname(channel_number)
            tsmask = caget(tsmask_pvname, as_string=True)

            for key in keys:
                if self.json['rate'][key]['ratemode'] == 'AC':
                    matches_acrate = self.json['rate'][key]['acrate'] == acrate
                    matches_tsmask = self.json['rate'][key]['tsmask'] == tsmask
                    
                    if matches_acrate and matches_tsmask:
                        print('Channel', channel_number, 'matched', key)
                        which_widget.setCurrentText(key)
            

    def configure_rate(self, ui):
        with open('get_pvname.json') as f:
            self.json = json.load(f)
            
        list_of_rates = self.json['rate'].keys()

        list_of_rates.sort()

        widgets = [ui.ch0_rate,
                   ui.ch1_rate,
                   ui.ch2_rate,
                   ui.ch3_rate,
                   ui.ch4_rate,
                   ui.ch5_rate,
                   ui.ch6_rate,
                   ui.ch7_rate,
                   ui.ch8_rate,
                   ui.ch9_rate,
                   ui.ch10_rate,
                   ui.ch11_rate,
                   ui.ch12_rate,
                   ui.ch13_rate]

        for e in widgets:
            for rate in list_of_rates:
                e.addItem(rate)

        self.set_initial_rate(ui.ch0_rate, "00")
        self.set_initial_rate(ui.ch1_rate, "01")
        self.set_initial_rate(ui.ch2_rate, "02")
        self.set_initial_rate(ui.ch3_rate, "03")
        self.set_initial_rate(ui.ch4_rate, "04")
        self.set_initial_rate(ui.ch5_rate, "05")
        self.set_initial_rate(ui.ch6_rate, "06")
        self.set_initial_rate(ui.ch7_rate, "07")
        self.set_initial_rate(ui.ch8_rate, "08")
        self.set_initial_rate(ui.ch9_rate, "09")
        self.set_initial_rate(ui.ch10_rate, "10")
        self.set_initial_rate(ui.ch11_rate, "11")
        self.set_initial_rate(ui.ch12_rate, "12")
        self.set_initial_rate(ui.ch13_rate, "13")

        ui.ch0_rate.activated[str].connect(self.ch0_set_rate)
        ui.ch1_rate.activated[str].connect(self.ch1_set_rate)
        ui.ch2_rate.activated[str].connect(self.ch2_set_rate)
        ui.ch3_rate.activated[str].connect(self.ch3_set_rate)
        ui.ch4_rate.activated[str].connect(self.ch4_set_rate)
        ui.ch5_rate.activated[str].connect(self.ch5_set_rate)
        ui.ch6_rate.activated[str].connect(self.ch6_set_rate)
        ui.ch7_rate.activated[str].connect(self.ch7_set_rate)
        ui.ch8_rate.activated[str].connect(self.ch8_set_rate)
        ui.ch9_rate.activated[str].connect(self.ch9_set_rate)
        ui.ch10_rate.activated[str].connect(self.ch10_set_rate)
        ui.ch11_rate.activated[str].connect(self.ch11_set_rate)
        ui.ch12_rate.activated[str].connect(self.ch12_set_rate)
        ui.ch13_rate.activated[str].connect(self.ch13_set_rate)

    
    def click_ch0_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "00", checked)

    def click_ch1_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "01", checked)

    def click_ch2_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "02", checked)

    def click_ch3_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "03", checked)

    def click_ch4_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "04", checked)

    def click_ch5_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "05", checked)

    def click_ch6_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "06", checked)

    def click_ch7_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "07", checked)

    def click_ch8_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "08", checked)

    def click_ch9_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "09", checked)

    def click_ch10_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "10", checked)

    def click_ch11_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "11", checked)

    def click_ch12_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "12", checked)

    def click_ch13_enable(self, checked):
        set_pvname.set_enable(self.get_pvname_instance, "13", checked)

    def configure_enable(self, ui):
        ui.ui.ch0_enable.clicked.connect(self.click_ch0_enable)
        ui.ui.ch1_enable.clicked.connect(self.click_ch1_enable)
        ui.ui.ch2_enable.clicked.connect(self.click_ch2_enable)
        ui.ui.ch3_enable.clicked.connect(self.click_ch3_enable)
        ui.ui.ch4_enable.clicked.connect(self.click_ch4_enable)
        ui.ui.ch5_enable.clicked.connect(self.click_ch5_enable)
        ui.ui.ch6_enable.clicked.connect(self.click_ch6_enable)
        ui.ui.ch7_enable.clicked.connect(self.click_ch7_enable)
        ui.ui.ch8_enable.clicked.connect(self.click_ch8_enable)
        ui.ui.ch9_enable.clicked.connect(self.click_ch9_enable)
        ui.ui.ch10_enable.clicked.connect(self.click_ch10_enable)
        ui.ui.ch11_enable.clicked.connect(self.click_ch11_enable)
        ui.ui.ch12_enable.clicked.connect(self.click_ch12_enable)
        ui.ui.ch13_enable.clicked.connect(self.click_ch13_enable)

        self.set_initial_enable(ui.ui.ch0_enable, "00")
        self.set_initial_enable(ui.ui.ch1_enable, "01")
        self.set_initial_enable(ui.ui.ch2_enable, "02")
        self.set_initial_enable(ui.ui.ch3_enable, "03")
        self.set_initial_enable(ui.ui.ch4_enable, "04")
        self.set_initial_enable(ui.ui.ch5_enable, "05")
        self.set_initial_enable(ui.ui.ch6_enable, "06")
        self.set_initial_enable(ui.ui.ch7_enable, "07")
        self.set_initial_enable(ui.ui.ch8_enable, "08")
        self.set_initial_enable(ui.ui.ch9_enable, "09")
        self.set_initial_enable(ui.ui.ch10_enable, "10")
        self.set_initial_enable(ui.ui.ch11_enable, "11")
        self.set_initial_enable(ui.ui.ch12_enable, "12")
        self.set_initial_enable(ui.ui.ch13_enable, "13")

    def set_initial_enable(self, which_widget, channel_number):
        ch_enable = caget(self.get_pvname_instance.get_enable_ch_pvname(channel_number))
        trg_enable = caget(self.get_pvname_instance.get_enable_trg_pvname(channel_number))

        if ch_enable == 0 and trg_enable == 0:
            # The channel_number channel is turned off. Set the checkbox off.
            which_widget.setChecked(False)
        elif ch_enable == 1 and trg_enable == 1:
            # The channel_number channel is turned on. Set the checkbox on.
            which_widget.setChecked(True)
        else:
            print('Should not be here. The channel and trigger are:',
                  ch_enable, trg_enable, 'which is not designed to be possible.')


    def configure_description(self, ui):
        ui.ch0_description.channel = self.get_pvname_instance.get_description_pvname("00")
        ui.ch1_description.channel = self.get_pvname_instance.get_description_pvname("01")
        ui.ch2_description.channel = self.get_pvname_instance.get_description_pvname("02")
        ui.ch3_description.channel = self.get_pvname_instance.get_description_pvname("03")
        ui.ch4_description.channel = self.get_pvname_instance.get_description_pvname("04")
        ui.ch5_description.channel = self.get_pvname_instance.get_description_pvname("05")
        ui.ch6_description.channel = self.get_pvname_instance.get_description_pvname("06")
        ui.ch7_description.channel = self.get_pvname_instance.get_description_pvname("07")
        ui.ch8_description.channel = self.get_pvname_instance.get_description_pvname("08")
        ui.ch9_description.channel = self.get_pvname_instance.get_description_pvname("09")
        ui.ch10_description.channel = self.get_pvname_instance.get_description_pvname("10")
        ui.ch11_description.channel = self.get_pvname_instance.get_description_pvname("11")
        ui.ch12_description.channel = self.get_pvname_instance.get_description_pvname("12")
        ui.ch13_description.channel = self.get_pvname_instance.get_description_pvname("13")
        
        
    def configure_current_rate(self, ui):
        ui.ch0_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("00")
        ui.ch1_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("01")
        ui.ch2_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("02")
        ui.ch3_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("03")
        ui.ch4_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("04")
        ui.ch5_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("05")
        ui.ch6_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("06")
        ui.ch7_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("07")
        ui.ch8_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("08")
        ui.ch9_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("09")
        ui.ch10_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("10")
        ui.ch11_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("11")
        ui.ch12_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("12")
        ui.ch13_current_rate.channel = self.get_pvname_instance.get_current_rate_pvname("13")
