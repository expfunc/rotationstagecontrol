# List of preferred commands

## General Commands
| Command ID | Command                  | Command description | Data type, value units | Additional comments |
| --- | --- | --- | --- | --- |
| 0x0100 | CONNECT                  | Establish a connection to the device |  |  |
| 0x0101 | DISCONNECT               | Disconnect from the device |  |  |

## Control Commands
| Command ID | Command                             | Command description                                               | Data type, value units | Additional comments       |
|------------|-------------------------------------|-------------------------------------------------------------------| --- |---------------------------|
| 0x0200     | MOVE ABSOLUTE {±value}              | Переместить платформу на заданный абсолютный угол                 | float, ° |                           |
| 0x0201     | MOVE RELATIVE {±value}              | Переместить платформу на заданный относительный угол              | float, ° |                           |
| 0x0202     | MOVE ABSOLUTE UNWRAPPED {±value}    | Переместить платформу на заданный абсолютный развёрнутый угол     | float, ° | Не реализовано для Standa |
| 0x0203     | SET SPEED {value}                   | Установить значение скорости платформы                            | float, °/s |                           |
| 0x0204     | SET ACCELERATION {value}            | Установить значение ускорения платформы                           | float, °/s² |                           |
| 0x0205     | SET DECELERATION {value}            | Установить значение замедления платформы                          | float, °/s² |                           |
| 0x0206     | SET CURRENT ANGLE {value}           | Принять текущее положение платформы за введённый угол             | float | Не реализовано для Standa |
| 0x0207     | SET CURRENT ANGLE UNWRAPPED {value} | Принять текущее положение платформы за введённый развёрнутый угол | float | Не реализовано для Standa                           |
| 0x0208     | SET ZERO                            | Задать текущий угол поворота платформы равным 0°                  |  |                           |
| 0x0209     | ABORT                               | Резко остановить движение платформы                               |  |                           |
| 0x0210     | STOP                                | Мягко остановить движение платформы                               |  | Не реализовано для Standa                           |

## Query Commands
| Command ID | Command                | Command description                                              | Answer format | Additional comments                 |
|------------|------------------------|------------------------------------------------------------------| --- |-------------------------------------|
| 0x0300     | GET POSITION           | Запросить текущее значение угла положения платформы              | float, ° |                                     |
| 0x0301     | GET POSITION UNWRAPPED | Запросить текущее значение развёрнутого угла положения платформы | float, ° | Не реализовано для Standa                                    |
| 0x0302     | GET MOVE SETTINGS      | Запросить текущие параметры платформы                            | {float, float, float} | {Speed, Acceleration, Deceleration} |
| 0x0303     | GET STATUS             | Запросить текущий статус                                         | {byte, string} | {status, additional data}           |
| 0x0304     | INFO                   | Запросить информацию о платформе                                 | {byte, string} | {device ID, additional data}        |