from plyer import notification
import time
def water_reminder():
    while True:
        notification.notify(title='Water Reminder', message='Time to drink some water Hitanshi!', timeout=10)
        time.sleep(3600)  # Wait for an hour
water_reminder()
