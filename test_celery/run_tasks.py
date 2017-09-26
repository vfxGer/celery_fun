from .tasks import longtime_add
from time import sleep


def main():
    i = 0
    while True:
        print("Running:%s" % i)
        result = longtime_add.delay(i)
        print('Task result:', result.result)
        i += 1
        if i%10 == 0:
            print("Sleeping for 60 seconds")
            sleep(60)


main()