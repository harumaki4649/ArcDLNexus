@echo off
cd C:\Users\msi-z\OneDrive\ドキュメント\GitHub\ArcDLNexus
pipreqs ./ArcDLNexus
python remove.py
python setup.py sdist
python setup.py bdist_wheel
pause