#!/bin/bash

# get local path
pwd

# test different condition
echo "hello" | python3 main.py
echo "USA" | python3 main.py
echo "Paris" | python3 main.py
echo "alala" | python3 main.py

# go to pandas folder
cd ..
cd learn_pandas
python3 main.py
