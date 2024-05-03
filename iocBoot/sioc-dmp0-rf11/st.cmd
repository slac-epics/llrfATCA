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
epicsEnvSet("IOC",          "sioc-dmp0-rf11")
epicsEnvSet("IOC_PRIMARY",  "SIOC")
epicsEnvSet("IOC_LOCA",     "DMP0")
epicsEnvSet("IOC_UNIT",     "RF11")
epicsEnvSet("IOC_INST",     "0")


# for TCAV, KLYS, TPR PV names
epicsEnvSet("TCAV_PRIMARY", "TCAV")
epicsEnvSet("KLYS_PRIMARY", "KLYS")
epicsEnvSet("TPR_PRIMARY",  "TPR")

# TCAV_LOCA macro
# DMPH : NC system
# DMPS:  SC system

epicsEnvSet("TCAV_LOCA",         "DMPH")
epicsEnvSet("TCAV_UNIT",         "360")


# LOCA and UNIT for KLYs and TPR
epicsEnvSet("LOCA", "DMP0")
epicsEnvSet("UNIT", "1")

#  INST Macro
#  0: NC system control
#  1: NC system diagnostic
#  2: SC system control
#  3: SC system diagnostic
epicsEnvSet("INST",         "0")

# IP Address for FPGA
epicsEnvSet("FPGA_IP0", "10.0.1.102")
epicsEnvSet("FIRMWARE_HASH", "hash-ca54b72")


# ====================================================================
# Call common script for, for the NC LINAC LLRF firmware.
# -- call ../common/st.cmd_NC
# ====================================================================
< ../common/st.cmd_NC_XTCAV


# ====================================================================
# Call command script for, starting triggers
# -- call $(TOP)/iocBoot/common/st.cmd_NC_trig_init
# ====================================================================
< $(TOP)/iocBoot/common/st.cmd_NC_trig_init


< $(TOP)/iocBoot/$(IOC)/st.cmd_default_set
