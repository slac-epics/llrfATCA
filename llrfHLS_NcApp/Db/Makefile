TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this

DB_INSTALLS += $(ATCACOMMON)/db/ATCACommon.db

# ==================================================
# Support for DaqMux and Waveform Engine
# ==================================================
DB_INSTALLS += $(ATCACOMMON)/db/StreamUlong.db
DB_INSTALLS += $(ATCACOMMON)/db/StreamLong.db

DB_INSTALLS += $(ATCACOMMON)/db/StreamUshort.db
DB_INSTALLS += $(ATCACOMMON)/db/StreamShort.db

DB_INSTALLS += $(ATCACOMMON)/db/StreamType.db

DB_INSTALLS += $(RFCOMMON)/db/RFCommon.db
DB_INSTALLS += $(RFCOMMON)/db/LlrfUpConverter.db
DB_INSTALLS += $(RFCOMMON)/db/LlrfDownConverter.db
# =======================================================

DB_INSTALLS += $(LLRFHLSASYN)/db/llrfHlsAsyn_NC_XTCAV.db
DB_INSTALLS += $(INTERLOCKRTMASYN)/db/interlockRtm.db

# Add testing/checkout database for RF Interlock RTM:
# This removes the ASG = "KLYS_MAINT" in order to enable write
# access to the PVs needed to set thresholds
DB += interlockRtm_Checkout.db

# User-defined functions
#DB += waveform_stream16.template


# Install crossbar control database
DB_INSTALLS += $(ATCACOMMON)/db/crossbarCtrl.db

# =====================================================
# Install Database for tprTrigger module
# =====================================================
DB_INSTALLS += $(TPRTRIGGER)/db/tprTrig.db
DB_INSTALLS += $(TPRTRIGGER)/db/tprDeviceNamePV.db
# =====================================================

# ==============================================================
# NC Timing: Pull in Database Templates the timing pattern
# and also the BSA database templates from the event module for
# use by BsaCore 
# ==============================================================
DB_INSTALLS += $(TPRPATTERN)/db/tprPattern.db
DB_INSTALLS += $(EVENT)/db/Bsa.db
# ==============================================================

# ===============================================
# llrfAmcAsyn databases
# ===============================================
DB_INSTALLS += $(LLRFAMCASYN)/db/llrfAmcAsyn.db

# Install Common databases needed by All IOCs
# ========================================================
# Install databases from iocAdmin package
# These databases support IOC Health and Monitoring
# ========================================================
# ========================================================
# SoftIOC CPU Load, Memory Uasge, ....
# ========================================================
DB_INSTALLS += $(IOCADMIN)/db/iocAdminSoft.db

DB_INSTALLS += $(IOCADMIN)/db/iocAdminScanMon.db
DB_INSTALLS += $(IOCADMIN)/db/iocScanMonSum.db
DB_INSTALLS += $(IOCADMIN)/db/iocScanMon.db
IOCRELEASE_DB += iocRelease.db
# =========================================================

# Install Database to support reading the status of the autosave package:
DB_INSTALLS += $(AUTOSAVE)/db/save_restoreStatus.db

# =======================================================================

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

