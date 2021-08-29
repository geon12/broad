#!/bin/bash
sudo apt-get update
sudo apt-get -y install python-pip
sudo apt-get install python-numpy python-scipy python-matplotlib python-pandas
sudo pip install -U scikit-learn
python -m py_compile cmapregression.py

echo "Done"
