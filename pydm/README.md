# PyDM Engineering Screens

PyDM-based engineering screens for the LLRF_HLS project.

## Prerequisites
 * pydm

## Open display:
* For controls IOCs:
```
pydm -m "DEV=KLYS:${LOCA}:${STN}1, IOC_UNIT=KY0${STN}, LOCA=${LOCA}, INST=0" \
    atcaLLRF.py
```

* For diagnostics IOCs
```
pydm -m "DEV=KLYS:${LOCA}:${STN}1, IOC_UNIT=KY${STN}1, LOCA=${LOCA}, INST=0" \
    atcaLLRF.py
```

Where:
- LOCA : Accelerator area (for example: `LI10`)
- STN : Klystron station number (for example: `2`)
