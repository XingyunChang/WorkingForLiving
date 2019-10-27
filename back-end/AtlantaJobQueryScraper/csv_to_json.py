import pandas as pd
import json

csv_name = "data/atlantaRentals.csv"
json_name = "data/atlantaRentals.json"


if __name__ == "__main__":
    dataset = pd.read_csv(csv_name)

    objs = [{} for i in range(len(dataset))]

    for key in dataset.keys():
        for i in range(len(dataset[key])):
            objs[i][key] = str(dataset[key][i])

    with open(json_name, "w") as fh:
        json.dump(objs, fh)