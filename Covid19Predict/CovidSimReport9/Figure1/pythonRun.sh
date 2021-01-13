#!/bin/bash
python3 -m virtualenv myvenv
source myvenv/bin/activate
pip3 install numpy matplotlib
python3 RelativeContactAfterClosure.py
