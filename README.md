# ONTI-FinTech

# Решение финальной задачи олимпиады ОНТИ по профилю "Программная инженерия финансовых технологии" 2019 года.

Создание платформы на примере сети ethereum с поддержкой распознавания и идентификации по лицу.

Проект представляет собой платформу с помощью которой можно получать доступ к своему ethereum кошельку посредством идентификации по лицу и четырёхзначного пин-кода.
После идентификации пользователь может совершить следующие действия:
- просмотр баланса.
- установка соответствия между ethereum кошельком и номером телефона.
- удаление соответствия между ethereum кошельком и номером телефона.
- перевод средств с одного кошелька на другой.

Работа платформы осуществляется посредством смарт-контракта написанного на языке solidity и скриптов написанных на языке python, которые взаимодействуют с контрактом.

setup.py - скрипт отвечающий за первоначальную настройку. Отправка смарт-контракта в сеть.
faceid.py - скрипт отвечающий за взаимодействие пользователя со своим кошельком
kyc.py - скрипт необходимый администратору (владельцу) платформы для осуществления действий не доступных простому пользователю.
face-management.py - скрипт отвечающий за распознавание и идентификацию

actions.json, faceapi.json, person.json, registrar.json необходимы для хранения информации и обмена информации между скриптами.

Смарт-контракт находится в KYC_Registrar.sol
