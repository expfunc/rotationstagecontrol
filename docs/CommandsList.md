# List of preferred commands

## General Commands
| Command ID | Command                  | Command description | Data type, value units | Additional comments |
| --- | --- | --- | --- | --- |
| 0x0100 | CONNECT                  | Establish a connection to the device |  |  |
| 0x0101 | DISCONNECT               | Disconnect from the device |  |  |

## Control Commands
| Command ID | Command                  | Command description | Data type, value units | Additional comments |
| --- | --- | --- | --- | --- |
| 0x0200 | MOVE ABSOLUTE {±value}   | Переместить платформу на заданный абсолютный угол | float, ° |  |
| 0x0201 | MOVE RELATIVE {±value}           | Переместить платформу на заданный относительный угол | float, ° |  |
| 0x0202 | SET SPEED {value}        | Установить значение скорости платформы | float, °/s |  |
| 0x0203 | SET ACCELERATION {value} | Установить значение ускорения платформы | float, °/s² |  |
| 0x0204 | SET DECELERATION {value} | Установить значение замедления платформы | float, °/s² |  |
| 0x0205 | SET ZERO                 | Задать текущий угол поворота платформы равным 0° |  |  |
| 0x0206 | ABORT                    | Остановить движение платформы |  |  |

## Query Commands
| Command ID | Command | Command description | Answer format | Additional comments |
| --- | --- | --- | --- | --- |
| 0x0300 | GET POSITION | Запросить текущее значение угла положения платформы | float, ° |  |
| 0x0301 | GET MOVE SETTINGS | Запросить текущие параметры платформы | {float, float, float} | {Speed, Acceleration, Deceleration} |
| 0x0302 | GET STATUS | Запросить текущий статус | {byte, string} | {status, additional data} |
| 0x0303 | INFO | Запросить информацию о платформе | {byte, string} | {device ID, additional data} |