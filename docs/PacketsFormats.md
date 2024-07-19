### Формат основного пакета

* Packet type (1 byte): `0x01`
* Device ID length (2 byte)
* Device ID
* Command ID (2 bytes)
* Command parameters
* CRC (2 bytes): A cyclic redundancy check (CRC). It is recommended to use CRC-16 with a generator polynomial of `0x1021`.

### Запрос списка устройств

* Packet type (1 byte): `0x08`
* CRC (2 bytes): A cyclic redundancy check (CRC). It is recommended to use CRC-16 with a generator polynomial of `0x1021`.

### Error Info

* Packet type (1 byte): `0x03`
* Info about error
* CRC (2 bytes): A cyclic redundancy check (CRC). It is recommended to use CRC-16 with a generator polynomial of `0x1021`.

### Device Response

* Packet type (1 byte): `0x02`
* Device ID length (2 byte)
* Device ID
* Command ID (2 bytes)
* Response
* CRC (2 bytes): A cyclic redundancy check (CRC). It is recommended to use CRC-16 with a generator polynomial of `0x1021`.