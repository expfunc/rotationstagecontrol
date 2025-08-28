# Standa 8MR151 – Rotation Stage Control

Backend для управления поворотным устройством [Standa 8MR151](https://www.standa.lt/products/catalog/motorised_positioners?item=9&prod=motorized_rotation_stages) через Raspberry Pi.  
Проект использует библиотеку **libximc (v2.14.30)** для управления устройством и реализует обмен данными по **UDP-протоколу** для удалённого контроля.

---
 
- [docs](docs/) — Форматы пакетов и список доступных команд для управления устройством  

---

## Требования

- Raspberry Pi с установленной **libximc 2.14.30**  
- Python 3.8+  
- Сетевое соединение (UDP)  

Установка зависимостей:
```bash
pip install libximc
