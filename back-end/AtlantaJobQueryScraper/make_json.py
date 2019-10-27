from data_model import model_name, DataModel
import json

json_name = "data/data_model.json"


if __name__ == "__main__":
    data = DataModel.load(model_name)

    with open(json_name, "w") as fh:
        json.dump(data.list, fh)
