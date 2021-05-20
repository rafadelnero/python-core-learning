

def time_conversion(time_am_pm):
    result = ""
    extracted_time = time_am_pm.split(":")

    if "PM" in time_am_pm:
        military_time = "12" if int(extracted_time[0]) == 12 else int(extracted_time[0]) + 12
        result += str(military_time) + ":" + extracted_time[1]+":"+extracted_time[2].strip("PM")
    else:
        extracted_time[0] = "00" if extracted_time[0] == "12" else extracted_time[0]
        result += extracted_time[0] + ":" + extracted_time[1] + ":" + extracted_time[2].strip("AM")

    print(result)


def time_conversion_user_solution(time):
    h, m, s = map(int, time[:-2].split(':'))
    p = time[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    print(('%02d:%02d:%02d') % (h, m, s))


if __name__ == '__main__':
    time_conversion("12:45:54PM")
    time_conversion_user_solution("07:05:45PM")
