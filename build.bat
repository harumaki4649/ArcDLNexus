@echo off
set TRD=C:\Users\msi-z\OneDrive\ƒhƒLƒ…ƒƒ“ƒg\GitHub\ArcDLNexus
cd %TRD%
pipreqs ./ArcDLNexus
python remove.py
python setup.py sdist
python setup.py bdist_wheel
cd C:\Users\msi-z\AppData\Roaming\Python\Python39\site-packages\twine
echo;
__main__.py upload --repository pypi %TRD%\dist\* --verbose
pause
