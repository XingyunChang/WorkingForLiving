import pickle

model_name = "data/data_model.pkl"


class DataModel:

    def __init__(self):
        self.set = set()
        self.list = []

    def load(fileName):
        with open(fileName, "rb") as fh:
            obj = pickle.load(fh)
        return obj

    def add(self, data):
        if data["title"] not in self.set:
            self.set.add(data["title"])
            self.list.append(data)

    def save(obj, fileName):
        with open(fileName, "wb") as fh:
            pickle.dump(obj, fh, pickle.HIGHEST_PROTOCOL)


def clear_model():
    model = DataModel()
    DataModel.save(model, model_name)


def print_model():
    model = DataModel.load(model_name)
    print("set size: ", len(model.set))
    print("list size: ", len(model.list))
    print(model.list)


if __name__ == "__main__":
    # clear_model()
    print_model()