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

# ===============================================
# Install crossbar control database for timing
# selection: routing NC/SC timing.
# ===============================================
DB_INSTALLS += $(ATCACOMMON)/db/crossbarCtrl.db


# ==================================================
# Support for DaqMux and Waveform Engine
# ==================================================
DB_INSTALLS += $(ATCACOMMON)/db/StreamUlong.db
DB_INSTALLS += $(ATCACOMMON)/db/StreamLong.db

DB_INSTALLS += $(ATCACOMMON)/db/StreamUshort.db
DB_INSTALLS += $(ATCACOMMON)/db/StreamShort.db

DB_INSTALLS += $(ATCACOMMON)/db/StreamType.db

# User-defined functions
#DB += waveform_stream16.template
# ========================================================

# =========================================================
# RFCommon databases: for common Demod/Mod DSP functions
# =========================================================
DB_INSTALLS += $(RFCOMMON)/db/RFCommon.db
DB_INSTALLS += $(RFCOMMON)/db/LlrfUpConverter.db
DB_INSTALLS += $(RFCOMMON)/db/LlrfDownConverter.db
# =======================================================

# =========================================================
# llrfAmcAsyn databases: for upconverter and downconverter
# AMC boards.
# =========================================================
DB_INSTALLS += $(LLRFAMCASYN)/db/llrfAmcAsyn.db

# =========================================================
# interlockRtmAsyn databases: for RF Interlock RTM
# =========================================================
DB_INSTALLS += $(INTERLOCKRTMASYN)/db/interlockRtm.db

# =========================================================
# llrfHlsAsyn databases: for LLRF HLS Application
# =========================================================
DB_INSTALLS += $(LLRFHLSASYN)/db/llrfHlsAsyn_SC_XTCAV.db
DB_INSTALLS += $(LLRFHLSASYN)/db/llrfHlsAsyn_SC_STCAV.db

# =====================================================
# Install Database for tprTrigger module
# =====================================================
DB_INSTALLS += $(TPRTRIGGER)/db/tprTrig.db
DB_INSTALLS += $(TPRTRIGGER)/db/tprTrig_ued.db
DB_INSTALLS += $(TPRTRIGGER)/db/tprDeviceNamePV.db
# =====================================================


# ===========================================================
# # SC Timing: Pull in Database Templates for BSA/BSSS
# # ==========================================================
DB_INSTALLS += $(BSADRIVER)/db/bsa.db
DB_INSTALLS += $(BSADRIVER)/db/bsss.db
DB_INSTALLS += $(BSADRIVER)/db/bsssCtrl.db
DB_INSTALLS += $(BSADRIVER)/db/bsas.db
DB_INSTALLS += $(BSADRIVER)/db/bsasCtrl.db
# ============================================================

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

