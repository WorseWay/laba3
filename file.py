# Импорт модуля для работы с последовательным портом
import serial

# Импорт модуля для работы со временем
import time

# Импорт модуля для получения списка доступных последовательных портов
import serial.tools.list_ports

# Список скоростей передачи данных
speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']

# Получение списка последовательных портов в системе
ports = [p.device for p in serial.tools.list_ports.comports()]

# Задание имени порта (в данном случае COM6)
port_name = 'COM6'

# Определение скорости передачи данных на основе последнего элемента списка speeds
port_speed = int(speeds[-1])

# Установка таймаута для порта (в секундах)
port_timeout = 10

# Инициализация объекта Serial для работы с портом
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)

# Пауза в 1 секунду для стабилизации порта
time.sleep(1)

# Очистка буфера входных данных порта
ard.flushInput()

# Попытка чтения данных из порта
try:
    # Чтение данных из порта в бинарном виде
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())

    # Декодирование бинарных данных в строку
    msg_str_ = msg_bin.decode()

    # Вывод длины прочитанных данных
    print(len(msg_bin))

# Обработка исключения, если чтение данных вызывает ошибку
except Exception as e:
    print('Error!')

# Закрытие порта
ard.close()

# Пауза в 1 секунду
time.sleep(1)

# Вывод прочитанных строковых данных
print(msg_str_)
