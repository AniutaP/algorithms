import time


__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    time_parts = time.gmtime(seconds)
    seconds_in_one_day = 86400
    seconds_in_one_hour = 3600
    seconds_in_one_minute = 60
    if seconds >= seconds_in_one_day:
        time_parts = time.gmtime(seconds - seconds_in_one_day)
        return time.strftime('%dd%Hh%Mm%Ss', time_parts)
    if seconds >= seconds_in_one_hour:
        return time.strftime('%Hh%Mm%Ss', time_parts)
    if seconds >= seconds_in_one_minute:
        return time.strftime('%Mm%Ss', time_parts)
    return time.strftime('%Ss', time_parts)
