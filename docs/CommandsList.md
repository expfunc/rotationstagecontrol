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
| Command | Command description | Answer format | Additional comments |
| --- | --- | --- | --- |
| GET POSITION | Запросить текущее значение угла положения платформы | float, ° |  |
| GET MOVE SETTINGS | Запросить текущие параметры платформы | {float, float, float} | {Speed, Acceleration, Deceleration} |
| GET STATUS | Запросить текущий статус | {byte, string} | {status, additional data} |
| INFO | Запросить информацию о платформе | {byte, string} | {device ID, additional data} |