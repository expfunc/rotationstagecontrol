# List of preferred commands for the positioner

## Platform Control Commands

| Command | Command Description |       Value Units      | Additional Comments |
| --- | --- | :-----------: | --- |
| MOVE ABSOLUTE {±value} | Переместить платформу на заданный абсолютный угол | °         |  |
| MOVE RELATIVE {±value} | Переместить платформу на заданный относительный угол | °         |  |
| MOVE HOME             | Переместить платформу в угол 0°            |           |  |
| SET DIRECTION {CW/CCW} | Выбрать направление движения платформы      |           | CW – clockwise, CCW – counter-clockwise |
| SET SPEED {value}      | Установить значение скорости платформы      |           | Нужно определиться, в каких величинах необходимо задавать данный параметр |
| SET ACCELERATION {value} | Установить значение ускорения платформы    |           | Нужно определиться, в каких величинах необходимо задавать данный параметр |
| SET DECELERATION {value} | Установить значение замедления платформы  |           | Нужно определиться, в каких величинах необходимо задавать данный параметр |
| SET ZERO              | Задать текущий угол поворота платформы равным 0° |           |  |
| ABORT                | Остановить движение платформы            |           |  |
| INIT SCAN {start angle} {stop angle} {step size} | Задать программу движения платформы      | °         |  |
| INIT ROUTE {angles list} | Задать программу движения платформы в соответствии с набором углов | °         | Не приоритетная команда, но было бы неплохо иметь в финальной реализации. |

## Platform Query Commands

| Command | Command Description |      Answer Format     | Additional Comments |
| --- | --- | :-----------: | --- |
| GET POSITION          | Запросить текущее значение угла положения платформы | Angle, °   | Было бы неплохо иметь возможность получения значения угла в реальном времени при движении платформы |
| GET SETTINGS          | Запросить текущие параметры платформы      | Speed, Acceleration, Deceleration |  |
| GET STATUS            | Запросить текущий статус            | Moving/Idle/Error |  |
| INFO                  | Запросить информацию о платформе      |             | Модель микроконтроллера и другие необходимые параметры |
