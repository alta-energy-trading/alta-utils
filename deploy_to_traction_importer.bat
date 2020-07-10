c:\dev\alta-utils\env\scripts\activate.bat & ^
python c:\dev\alta-utils\setup.py bdist_wheel & ^
del /q c:\dev\traction-importer\wheels\alta-utils\* & ^
cd dist & ^
robocopy . c:\dev\traction-importer\wheels\alta-utils /maxage:1 & ^
c:\dev\traction-importer\env\scripts\activate.bat & pause