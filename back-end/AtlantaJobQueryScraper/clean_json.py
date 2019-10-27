from make_json import json_name
import json
import re
import numpy as np

cleaned_name = "data/data_clean.json"
atlanta_zip_regex = r"30\d\d\d"
number_regex = r"[\d,]+"
month_in_year = 12
week_in_mont = 4
workday_in_week = 5
workhour_in_day = 8


def has_zipcode(string):
    return len(re.findall(atlanta_zip_regex, string)) != 0


def get_zipcode(string):
    return re.findall(atlanta_zip_regex, string)[0]


def get_annual_pay(string):
    nums = [int(string.replace(",", "")) for string in re.findall(number_regex, string)]

    if "year" in string:
        multiplier = 1
    elif "month" in string:
        multiplier = month_in_year
    elif "week" in string:
        multiplier = workday_in_week * month_in_year
    elif "day" in string:
        multiplier = workday_in_week * workday_in_week * month_in_year
    elif "hour" in string:
        multiplier = workhour_in_day * workday_in_week * workday_in_week * month_in_year
    else:
        raise Exception("Cannot interpret salary string:", string)
    nums = [num * multiplier for num in nums]
    return np.median(np.array(nums))


if __name__ == "__main__":
    with open(json_name, "r") as fh:
        data = json.load(fh)

    processed = []

    for item in data:
        if has_zipcode(item["location"]) and item["salary"] is not None:
            item["annual-pay"] = get_annual_pay(item["salary"])
            item["zipcode"] = get_zipcode(item["location"])
            processed.append(item)

    with open(cleaned_name, "w") as fh:
        json.dump(processed, fh)

    print("Done.")