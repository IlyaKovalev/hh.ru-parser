# hh.ru-parser
Парсер вакансий и резюме для hh.ru
## Warning
проект не является законченным

Для получения вакансий используется открытое API (https://github.com/hhru/api/blob/master/docs/general.md).
Так как вакансий ОЧЕНЬ много, то наши обращения могут быть интерпретированы как DDoS атака (насчет этого не уверен конечно но я посчитал
что кол-во запросов составит около 5-ой части месячного траффика следовательно админ может быстро кикнуть), поэтому запросы делаются через
torsocks (эта логика инкапсулирована в пакете `make_req`), в папке `constant` лежит общая конфигурация проекта и файл
с заголовками для http запросов.

Я решил добавить еще внезапности и поэтому при начале сессии запросов скрипт генерирует случайное число от 1 до 10, делает
именно такое кол-во запросов, а затем меняет выходную ноду.
Вообще по закону DDoS-ом считается более 30 запросов в минуту с одного ip адреса (на самом деле не знаю
насколько эта информаия верна просто решил перестраховаться)

Работает пока только функционал с записью справочников (запись вакансий тож работает просто я пока не решил 
в каком формате их хранить)
Парсер резюме я не начинал делать (там проблемы другого рода). Надо либо покупать доступ к бд с резюме по всей России (~21к рублей)
либо парсить открытые и уже потом обобщать на генеральную совокупность. Изначально планировалось сделать анализ рынка труда.
