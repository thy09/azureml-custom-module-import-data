import os
import pickle

import fire
import ruamel.yaml
from torchvision import datasets


def write_meta(dataset_name, pickle_file_name, yaml_path):
    data = {'type': 'torch-dataset', 'dataset-name': dataset_name, 'pickle-file': pickle_file_name}
    with open(yaml_path, 'w') as fout:
        ruamel.yaml.round_trip_dump(data, fout)


DATASET_NAMES = {
    'CIFAR10', 'CIFAR100', 'Caltech101', 'Caltech256', 'CelebA', 'FashionMNIST',
    'ImageNet', 'KMNIST', 'MNIST', 'Omniglot', 'PhotoTour',
    'SBDataset', 'SBU', 'SEMEION', 'STL10', 'SVHN', 'VOCDetection', 'VOCSegmentation',
}


def download_dataset(dataset_name, output_folder):
    if dataset_name not in DATASET_NAMES:
        raise Exception(f"Not a valid dataset name: {dataset_name}")
    load_data_method = getattr(datasets, dataset_name)
    ds = load_data_method(output_folder, download=True)
    pickle_file_name = 'dataset.pickle'
    with open(pickle_file_name, 'wb') as fout:
        pickle.dump(ds, fout)
    write_meta(dataset_name, pickle_file_name, os.path.join(output_folder, '_meta.yaml'))


if __name__ == '__main__':
    fire.Fire(download_dataset)
