from datetime import date, datetime


def mpesa_time():
    now=datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    return f"{year}{month}{day}{hour}{minute}{second}"
    

    