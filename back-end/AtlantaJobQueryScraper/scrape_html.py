import requests
from parse_html import parse
from data_model import DataModel, model_name
from tqdm import tqdm
import time
import random

baseURL = "https://www.indeed.com/jobs?q=&l=Atlanta%2C+GA&filter={}start={}"
filterNumbers = list(range(0, 10))
startNumbers = list(range(0, 1000, 10))
minSleepTime = 1.00
randomRange = 1.50


if __name__ == "__main__":
    data = DataModel.load(model_name)

    compoundNumber = [(filterNumber, startNumber) for filterNumber in filterNumbers for startNumber in startNumbers]
    print("Request Count:", len(compoundNumber))

    for filterNumber, startNumber in tqdm(compoundNumber):
        url = baseURL.format(filterNumber, startNumber)
        print("Request URL: ", url)

        response = requests.get(url)

        items = parse(response.text)

        for item in items:
            data.add(item)

        randomSleep = minSleepTime + random.random() * randomRange
        print("Sleep for: ", randomSleep, "s")
        time.sleep(randomSleep)

    DataModel.save(data, model_name)
