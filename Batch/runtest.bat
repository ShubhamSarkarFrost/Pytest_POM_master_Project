@echo off

rem Directory to store allure results
set RESULT_DIR=allure-results
set REPORT_DIR=allure-report

rem Run pytest and generate allure results
pytest tests/parabank_register_page.py --alluredir=%RESULT_DIR%

rem Generate the allure report
allure generate %RESULT_DIR% --clean -o %REPORT_DIR%

rem Automatically open the allure report in the default web browser
allure open %REPORT_DIR%

rem Prevent the command line from closing automatically
pause