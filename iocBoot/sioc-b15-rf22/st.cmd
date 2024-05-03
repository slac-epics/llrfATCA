#!../../bin/linuxRT-x86_64/llrfHLS_Sc
# ====================================================================
# NC-SXR (LCLS-II Timing)
# Will be used for SC [XTCAV and LCLS LINAC Upgrades] by llrfHLS_Sc App
# ====================================================================

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables

# for IOC PV names
epicsEnvSet("IOC",          "sioc-b15-rf22")
epicsEnvSet("IOC_PRIMARY",  "SIOC")
epicsEnvSet("IOC_LOCA",     "B15")
epicsEnvSet("IOC_UNIT",     "RF22")
epicsEnvSet("IOC_INST",     "0")


# for TCAV, KLYS, TPR PV names
epicsEnvSet("TCAV_PRIMARY", "TCAV")
epicsEnvSet("KLYS_PRIMARY", "KLYS")
epicsEnvSet("TPR_PRIMARY",  "TPR")

# TCAV_LOCA macro
# DMPH : NC system
# DMPS:  SC system

epicsEnvSet("TCAV_LOCA",         "DMPS")
epicsEnvSet("TCAV_UNIT",         "360")


# LOCA and UNIT for KLYs and TPR
epicsEnvSet("LOCA", "DMP0")
epicsEnvSet("UNIT", "1")

#  INST Macro
#  0: NC system control
#  1: NC system diagnostic
#  2: SC system control
#  3: SC system diagnostic
epicsEnvSet("INST",         "3")

#  for BSSS control PV
epicsEnvSet("BSSS_GLOBAL", "BSSS:B015:1")

# IP Address for FPGA
epicsEnvSet("FPGA_IP0", "10.0.1.106")

#epicsEnvSet("FIRMWARE_HASH", "hash-ca54b72")


# ====================================================================
# Call common script for, for the NC LINAC LLRF firmware.
# -- call ../common/st.cmd_SC
# ====================================================================
< ../common/st.cmd_SC_XTCAV

# ====================================================================
# Call command script for, starting triggers
# -- call $(TOP)/iocBoot/common/st.cmd_NC_trig_init
# ====================================================================
< $(TOP)/iocBoot/common/st.cmd_SC_trig_init

< $(TOP)/iocBoot/$(IOC)/st.cmd_default_set
