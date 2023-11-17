pytest --alluredir=tests\allure_results .\tests\elements_test.py::TestElements::
allure serve .\tests\allure_results
pip freeze > requirements.txt
pip install -r requirements.txt

-x позволяет завершить сессию автотестов при первом неудачном результате
-x включает детализацию, отображаему в терминале
-s позволяет отобразить в терминале результат методов print()
-m позволяет запустить тесты с определеным маркером


