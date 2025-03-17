import psutil

buttry = psutil.sensors_battery()

if buttry is not None:
    print("Battery status: ", buttry.percent)
    print("Power plugged in: ", buttry.power_plugged)

else:
    print("Battery status: Not available")