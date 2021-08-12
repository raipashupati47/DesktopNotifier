import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message="Getting enough water is important for your health. Drinking water can prevent dehydration.",
            app_icon="C:\\Users\\PASHUPATI RAI\\PycharmProjects\\Notifier\\ig.ico",
            # displaying time
            timeout=2
            )
        # waiting time
        time.sleep(7)
