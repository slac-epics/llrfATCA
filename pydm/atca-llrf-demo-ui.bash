#!/usr/bin/env bash

. $EPICS_SETUP/epicsenv-7.0.3.1-1.0.bash
. $TOOLS/script/use_pydm.sh

pydm --version

PYDM_STYLESHEET_INCLUDE_DEFAULT=1 pydm -m "LOCA=B084,UNIT=RF70,INST=0,TCAV_LOCA=B084,TCAV_UNIT=RF70,IOC_UNIT=RF70, DESC=NC,SIOC=SIOC:B084:RF70,DEV=TCAV:B084:RF70:0" \
    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
    --stylesheet $PYDM/klys/llrf.qss \
    /afs/slac/g/controls/development/users/ktkim/sandbox/llrfATCA/pydm/xtcav_atcaLLRF_pau.py &
