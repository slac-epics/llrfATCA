from os import path
from pydm import Display
import configure_pvname
import set_pvname
import sys

class ued(Display):
    def __init__(self, parent=None, args=None, macros=None):
        # Required by pydm.
        super(ued, self).__init__(parent=parent, args=args, macros=None)

        # Get the prefix from the commandline macro.
        if macros == None or macros['prefix'] == None:
            sys.exit('Please specify the prefix in the pydm macro.')

        prefix = macros['prefix']

        self.configure_pvname_instance = configure_pvname.ConfigurePVName(prefix)

        self.configure_pvname_instance.configure_polarity(self)
        self.configure_pvname_instance.configure_width(self)
        self.configure_pvname_instance.configure_delay(self)
        self.configure_pvname_instance.configure_rate(self)
        self.configure_pvname_instance.configure_enable(self)
        self.configure_pvname_instance.configure_description(self)
        self.configure_pvname_instance.configure_current_rate(self)


    def ui_filename(self):
        # Required by pydm.
        return 'ued.ui'
