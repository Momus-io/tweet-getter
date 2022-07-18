import schedule
import time
import worker

schedule.every().day.at("21:58").do(worker.main)

while True:
    schedule.run_pending()
    time.sleep(1)
