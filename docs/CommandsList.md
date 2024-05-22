# List of preferred commands

## Control Commands
| Command                  | Command description | Data type, value units | Additional comments |
|--------------------------| --- | --- | --- |
| MOVE ABSOLUTE {±value}   | Переместить платформу на заданный абсолютный угол | float, ° |  |
| MOVE RELATIVE {±value}           | Переместить платформу на заданный относительный угол | float, ° |  |
| SET SPEED {value}        | Установить значение скорости платформы | float, °/s |  |
| SET ACCELERATION {value} | Установить значение ускорения платформы | float, °/s² |  |
| SET DECELERATION {value} | Установить значение замедления платформы | float, °/s² |  |
| SET ZERO                 | Задать текущий угол поворота платформы равным 0° |  |  |
| ABORT                    | Остановить движение платформы |  |  |
## Query Commands
| Command description | Command | Answer format | Additional comments |
| --- | --- | --- | --- |
| Запросить текущее значение угла положения платформы | GET POSITION | float, ° |  |
| Запросить текущие параметры платформы | GET MOVE SETTINGS | {float, float, float} | {Speed, Acceleration, Deceleration} |
| Запросить текущий статус | GET STATUS | {byte, string} | {status, additional data} |
| Запросить информацию о платформе | INFO | {byte, string} | {device ID, additional data} |