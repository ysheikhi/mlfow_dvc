import dvc.api
repo="/Users/yousef-mac/Documents/DS_PETPROJECTS/mlflow_demo"
path="../data/winequality-red.csv"
version = "v4"


if __name__ == "__main__":
    data_url = dvc.api.get_url(path =path, repo=repo, rev=version)
    print(data_url)