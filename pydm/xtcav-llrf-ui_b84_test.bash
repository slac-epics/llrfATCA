#!/usr/bin/env bash

. $EPICS_SETUP/epicsenv-7.0.3.1-1.0.bash
. $TOOLS/script/use_pydm.sh

pydm --version

PYDM_STYLESHEET_INCLUDE_DEFAULT=1 pydm \
    --hide-nav-bar \
    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
    --stylesheet /afs/slac/g/controls/development/users/ktkim/sandbox/PyDM/klys/main/llrf.qss \
   /afs/slac/g/controls/development/users/ktkim/sandbox/PyDM/klys/main/test_stations.ui &

