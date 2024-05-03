from pydm import Display
import re
import logging
from numbers import Number
import epics
from qtpy.QtGui import QDoubleValidator
from qtpy.QtWidgets import QMessageBox


logger = logging.getLogger(__name__)

class ComplexWindow(Display):
    def __init__(self, parent=None, args=None, macros=None, ui_filename=None):
        super(ComplexWindow, self).__init__(parent=parent, args=args, macros=macros)

        self._macros = macros

        try:
            # Get the macro values
            self._device = self._macros['DEV']
            self._record = self._macros['R']
            self._index = self._macros['N']
        except:
            QMessageBox.critical(self,
                "Error",
                "Something went wrong with the macro??..."
                )
            logger.error(
                "You need to define a DEV macro (-m 'DEV=KLYS:${LOCA}:${STN}1')")

        # List of labels for the input channel selection menu
        self._input_labels = [
            "DnwCon:RF_IN_2",
            "DnwCon:RF_IN_1",
            "DnwCon:RF_IN_4",
            "DnwCon:RF_IN_3",
            "DnwCon:RF_IN_6",
            "DnwCon:RF_IN_5",
            "UpCon:RF_IN_2",
            "UpCon:RF_IN_1",
            "UpCon:RF_IN_3",
            "UpCon:RF_OUT_MON",
        ]

        # Read the ADC frequency (normally this is 357 Mhz)
        self._adc_freq = epics.caget('{}:XWF_ASUB.A'.format(self._device))

        # Read the waveform size. We just need to read the size from one 
        # waveform, so here were are reading it from the amplitude one.
        self._size = int(epics.caget('{}:A{}{}.NELM'.format(self._device, self._record, self._index)))

        # Setup all elements in the UI
        self.ui_setup()

    def add_pv_labels(self):
        """
        Adds the respective label PV to the input channel menu label, if defined.
        """
        for i in range(0,10):
            label_pv = epics.caget("{}:DMOD_LABEL{}".format(self._device, i))
            if label_pv:
                self._input_labels[i] += " - {}".format(label_pv)

    def ui_setup(self):
        """
        Setup all elements in the UI.
        """
        self.input_selection_setup()
        self.time_interval_setup()
        self.value_setup()
        self.write_pv_setup()

    def time_interval_setup(self):
        """
        Setup the time interval line edit
        """
        # Set valiator for the time line edits
        self.ui.amplitude_start.setValidator(
            QDoubleValidator(self.ui.amplitude_start))
        self.ui.amplitude_end.setValidator(
            QDoubleValidator(self.ui.amplitude_end))
        self.ui.phase_start.setValidator(
            QDoubleValidator(self.ui.phase_start))
        self.ui.phase_end.setValidator(
            QDoubleValidator(self.ui.phase_end))

    def value_setup(self):
        """
        Setup the value line edit
        """
        # Set valiator for the time line edits
        self.ui.amplitude_value.setValidator(
            QDoubleValidator(self.ui.amplitude_value))
        self.ui.phase_value.setValidator(
            QDoubleValidator(self.ui.phase_value))

        # Set the amplitude value to 1 by defualt
        self.ui.amplitude_value.setText("1")

    def write_pv_setup(self):
        """
        Setup the write PV buttons
        """
        self.ui.write_amplitude.clicked.connect(self.write_amplitude_pv)
        self.ui.write_phase.clicked.connect(self.write_phase_pv)

    def input_selection_setup(self):
        """
        Setup the input_select menu.
        """
        # Add PV labels to the input channel menu labels 
        self.add_pv_labels()

        # Add the generated list of labels to the input channel menu
        self.ui.input_selection.clear()
        self.ui.input_selection.addItems(self._input_labels)

        # Call self.input_selection_changed when the user choose an item
        self.ui.input_selection.activated.connect(
            self.input_selection_changed)

    def input_selection_changed(self, index):
        """
        Process changes in the input selection menu
        """
        # Get the current list of amplitude curves
        curves = self.amplitude_plot.getCurves()

        # The measurement signal is the second in the list.
        # It PV name is ${DEV}:AWF${INDEX}
        # Change it to point to the selected index
        curves[1] = re.sub("{}:AWF\d".format(self._device),
                           "{}:AWF{}".format(self._device, index),
                           curves[1])

        # Send back the modified list
        self.amplitude_plot.setCurves(curves)

        # Get the current list of phase curves
        curves = self.phase_plot.getCurves()

        # The measurement signal is the second in the list.
        # It PV name is ${DEV}:PWF${INDEX}
        # Change it to point to the selected index
        curves[1] = re.sub("{}:PWF\d".format(self._device),
                           "{}:PWF{}".format(self._device,  index),
                           curves[1])

        # Send back the modified list
        self.phase_plot.setCurves(curves)

    def get_amplitude_start(self):
        """
        Read the amplitude start time
        """
        return self.get_line_edit_float(self.ui.amplitude_start)
        #start = None
        #str_value = str(self.ui.amplitude_start.text())
        #if str_value:
        #    try:
        #        start = float(str_value)
        #    except ValueError:
        #        logger.error('Could not convert to float')
        #return start

    def get_amplitude_end(self):
        """
        Read the amplitude end time
        """
        return self.get_line_edit_float(self.ui.amplitude_end)
        #end = None
        #str_value = str(self.ui.amplitude_end.text())
        #if str_value:
        #    try:
        #        end = float(str_value)
        #    except ValueError:
        #        logger.error('Could not convert to float')
        #return end

    def get_phase_start(self):
        """
        Read the phase start time
        """
        return self.get_line_edit_float(self.ui.phase_start)
        #start = None
        #str_value = str(self.ui.phase_start.text())
        #if str_value:
        #    try:
        #        start = float(str_value)
        #    except ValueError:
        #        logger.error('Could not convert to float')
        #return start

    def get_phase_end(self):
        """
        Read the phase end time
        """
        return self.get_line_edit_float(self.ui.phase_end)
        #end = None
        #str_value = str(self.ui.phase_end.text())
        #if str_value:
        #    try:
        #        end = float(str_value)
        #    except ValueError:
        #        logger.error('Could not convert to float')
        #return end

    def get_amplitude_value(self):
        """
        Read the amplitude value
        """
        return self.get_line_edit_float(self.ui.amplitude_value)

    def get_phase_value(self):
        """
        Read the amplitude value
        """
        return self.get_line_edit_float(self.ui.phase_value)

    def get_line_edit_float(self, line_edit):
        """
        Get the value from a line edit widget, as a float
        """
        value = None
        str_value = str(line_edit.text())
        if str_value:
            try:
                value = float(str_value)
            except ValueError:
                logger.error('Could not convert to float')
        return value

    def generate_waveform(self, start, end, value=1.0):
        """
        Generate a rectangual waveform, using the start and end times.
        """
        is_valid = False
        is_zeros = False

        if start == 0 and end == 0:
            is_zeros = True

        if (isinstance(start, Number) and
                isinstance(end, Number) and self._size):
            is_valid = True

        logger.debug('Start: {}, end: {}'.format(start, end))

        if not is_valid:
            QMessageBox.critical(self,
                "Invalid Window Dimensions",
                "You must define start & end values"
                )
            return False, 0

        # Convert the the time to indexes
        start_index = int(start * self._adc_freq)
        end_index = int(end * self._adc_freq)

        if (start_index >= end_index and not is_zeros) or (end_index >= self._size):
            QMessageBox.critical(self,
                "Invalid Window Dimensions",
                "Not a valid I window size. Please make sure"
                " the start < end, and end < pv_size, or both zeros"
                )
            return False, 0

        # Generate and return the waveform
        return True, ([0]*start_index + [value]*(end_index - start_index) + [0]*(self._size - end_index))

    def write_amplitude_pv(self):
        """
        Process the command to write the amplitude PV
        """

        # Get the amplitude value
        amplitude = self.get_amplitude_value()

        # Verify that the amplitude is a positive number
        if not amplitude > 0:
            QMessageBox.critical(self,
                "Invalid Amplitude Value",
                "The amplitude must be a positive number"
                )
            return

        # Generate the waveform data
        valid, win = self.generate_waveform(
            start = self.get_amplitude_start(), 
            end = self.get_amplitude_end(), 
            value = amplitude)

        # If the waveform data was genearetd, write it to the amplitude PV
        if valid:
            epics.caput('{}:A{}{}'.format(self._device, self._record, self._index), win)

    def write_phase_pv(self):
        """
        Process the command to write the phase PV
        """

        # Get the phase value
        phase = self.get_phase_value()

        # Verify that the phase is between -180 and 180 deg
        if not (phase >= -180 and phase <= 180):
            QMessageBox.critical(self,
                "Invalid Phase Value",
                "The phase value must be between -180 and 180 deg"
                )
            return

        # Generate the waveform data
        valid, win = self.generate_waveform(
            start = self.get_phase_start(), 
            end = self.get_phase_end(), 
            value = phase)

        # If the waveform data was genearetd, write it to the amplitude PV
        if valid:
            epics.caput('{}:P{}{}'.format(self._device, self._record, self._index), win)

    def ui_filename(self):
        """
        Return the UI file name
        """
        return 'hls_complex_window.ui'
