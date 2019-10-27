import json
import numpy as np
from clean_json import month_in_year


def query(job_database, house_database, infos):
    try:
        infos = json.loads(infos)
    except:
        return json.dumps([])

    keys = infos.keys()

    if 'title' not in keys or 'zipcode' not in keys or 'hometype' not in keys or 'index' not in keys:
        return json.dumps([])

    title = str(infos['title'])
    zipcode = str(infos['zipcode'])
    hometype = str(infos['hometype'])
    try:
        index = int(infos["index"])
    except:
        return json.dumps([])

    job_database = sort_by_title(job_database, title)
    job_database = filter_by(job_database, "zipcode", zipcode)
    house_database = filter_by(house_database, "zipcode", zipcode)
    house_database = filter_by(house_database, "type", hometype)

    print(len(job_database))
    print(len(house_database))

    pairs = []
    for job in job_database:
        for house in house_database:
            if float(job["annual-pay"]) >= float(house["price"]) * month_in_year:
                pairs.append((job, house))
            print(float(job["annual-pay"]), float(house["price"]) * month_in_year)

    losts = [lost(job, house, title) for job, house in pairs]
    pairs = [pairs[idx] for idx in np.argsort(losts)]

    if 0 <= index < len(pairs):
        return json.dumps(pairs[index])
    else:
        return json.dumps([])


def lost(job, house, title):
    x = float(job["annual-pay"]) / (float(house["price"]) * month_in_year)
    if x < 1.5:
        money_lost = (1.5 - x) * 2
    else:
        money_lost = min(1.0, (x - 1.5) * 0.25)

    title_lost = levenshtein(title, job["title"])

    # print(money_lost, title, "----", job["title"], title_lost)
    return money_lost * 0.2 + title_lost * 0.8


def sort_by_title(job_database, title):
    job_titles = [job["title"] for job in job_database]
    dists = np.array([levenshtein(title, curr_job) for curr_job in job_titles])
    first_indices = np.argsort(dists)
    return [job_database[i] for i in first_indices]


def filter_by(database, key, value):
    values = [job[key] for job in database]
    indices = np.nonzero(np.array(values, dtype="str") == str(value))[0]
    return [database[int(i)] for i in indices]


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]/float(len(s1))
