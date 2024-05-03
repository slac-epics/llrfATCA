#!/usr/bin/env bash

. $EPICS_SETUP/epicsenv-7.0.3.1-1.0.bash
. $TOOLS/script/use_pydm.sh

pydm --version

PYDM_STYLESHEET_INCLUDE_DEFAULT=1 pydm -m "LOCA=DIAG0,UNIT=11,INST=1,TCAV_LOCA=DIAG0,TCAV_UNIT=11,IOC_UNIT=11, DESC=SC,SIOC=SIOC:DIAG0:KY02,DEV=TCAV:DIAG0:11" \
    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
    --stylesheet $PYDM/klys/llrf.qss \
    $PYDM/klys/stcav_atcaLLRF.py &
