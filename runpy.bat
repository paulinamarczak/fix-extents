@echo off


rem set "PATH= %PATH%, %ProgramFiles%\ArcGIS\Pro\bin\Python\Scripts\%, C:\Users\PMARCZAK\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\, C:\Users\PMARCZAK\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\Lib, C:\Users\PMARCZAK\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\Lib\site-packages, C:\Users\PMARCZAK\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\Scripts"
rem set "PATH= %PATH%, %ProgramFiles%\ArcGIS\Pro\bin\Python\Scripts\%, C:\Users\pmarczak\AppData\Local\anaconda3\Lib, C:\Users\pmarczak\AppData\Local\anaconda3\\Lib\site-packages, C:\Users\pmarczak\AppData\Local\anaconda3\\Scripts"
rem set "PATH= %PATH%,  C:\Users\pmarczak\AppData\Local\anaconda3\Lib, C:\Users\pmarczak\AppData\Local\anaconda3\\Lib\site-packages, C:\Users\pmarczak\AppData\Local\anaconda3\\Scripts"

echo %PATH%

rem Set your python exe to your own install folder

rem python_exe= "C:\Users\PMARCZAK\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe"
rem set python_exe= "C:\Users\pmarczak\AppData\Local\anaconda3\python.exe"
set python_exe = "T:\corp\python3916\python.exe"


%python_exe% ".\fix_metadata.py"

pause