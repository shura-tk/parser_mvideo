from time import sleep

from pythonping import ping


def wait_ping():

    ex = False
    while not ex:
        try:
            ex = ping('ya.ru').success()
            sleep(0.5)
        except:
            pass


if __name__ == '__main__':
    main()

