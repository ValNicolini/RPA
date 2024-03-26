import schedule
from time import sleep



while True:
    schedule.run_pending()
    print('Testando...')

    sleep(10)

