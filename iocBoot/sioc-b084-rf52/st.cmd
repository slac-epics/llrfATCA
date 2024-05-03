#!../../bin/linuxRT-x86_64/llrfHLS_Nc
# ====================================================================
# NC-HXR (LCLS-I Timing)
# Will be used for NC [XTCAV and LCLS LINAC Upgrades] by llrfHLS_NCApp
# ====================================================================

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables

# for IOC PV names
epicsEnvSet("IOC",      "sioc-b084-rf52")
epicsEnvSet("IOC_PRIMARY",  "SIOC")
epicsEnvSet("IOC_LOCA",     "B084")
epicsEnvSet("IOC_UNIT",     "RF52")
epicsEnvSet("IOC_INST",     "0")

# for TCAV, KLYS, TPR PV names
epicsEnvSet("TCAV_PRIMARY", "TCAV")
epicsEnvSet("KLYS_PRIMARY", "KLYS")
epicsEnvSet("TPR_PRIMARY",  "TPR")

# TCAV_LOCA macro
# DMPH : NC system
# DMPS:  SC system
epicsEnvSet("TCAV_LOCA",         "B084")
epicsEnvSet("TCAV_UNIT",         "RF52")

# LOCA and UNIT for KLYs and TPR
epicsEnvSet("LOCA", "B084")
epicsEnvSet("UNIT", "RF52")

#  INST Macro
#  0: NC system control
#  1: NC system diagnostic
#  2: SC system control
#  3: SC system diagnostic
epicsEnvSet("INST",         "0")

# IP Address for FPGA
epicsEnvSet("FPGA_IP0", "10.0.1.104")
#epicsEnvSet("FIRMWARE_HASH", "hash-f12f67f")
epicsEnvSet("FIRMWARE_HASH", "hash-ca54b72")

# ====================================================================
# Call common script for, for the NC LINAC LLRF firmware.
# -- call ../common/st.cmd_NC
# ===================================================
< ../common/st.cmd_NC

