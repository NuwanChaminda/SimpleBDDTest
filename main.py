from behave.__main__ import main as behave_main
import allure_behave
import os

if __name__ == '__main__':
    # to execute selenium UI tests
    behave_main("-f allure_behave.formatter:AllureFormatter -o reports/allure/results features --logging-level DEBUG")
    os.system('cmd /c "allure generate reports/allure/results --clean -o reports/allure/reports"')
    os.system('cmd /c "allure serve reports/allure/results"')
