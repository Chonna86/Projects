from datetime import datetime


def get_str_date(date):
    print(date)
    date_time_obj = datetime.fromisoformat(date)
    print(date_time_obj)
    norm_date = date_time_obj.strftime('%A %d %B %Y')
    print(norm_date)
    return norm_date
iso_date = "2021-05-27 17:08:34.149Z"
get_str_date(iso_date)  