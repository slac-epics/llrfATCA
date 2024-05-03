#!/usr/bin/env bash

. $EPICS_SETUP/epicsenv-7.0.3.1-1.0.bash
. $TOOLS/script/use_pydm.sh

pydm --version

PYDM_STYLESHEET_INCLUDE_DEFAULT=1 pydm \
    --hide-nav-bar \
    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
    --stylesheet $PYDM/klys/llrf.qss \
    $PYDM/klys/xtcav_stations.ui &

