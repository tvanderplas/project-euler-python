@echo off
cd Tests
python -m unittest discover --pattern=*test.py
cd ..
