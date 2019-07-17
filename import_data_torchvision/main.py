import argparse
import ruamel.yaml
import os

from torchvision import datasets


def get_args():
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument("--dataset_name",
                        type=str,
                        required=True,
                        help="The name of the dataset in torchvision.datasets")

    parser.add_argument("--output_folder",
                        type=str,
                        required=True,
                        help="The folder to store the images")
    return parser.parse_args()


def write_meta(dataset_name, yaml_path):
    data = {'type': 'torch-dataset', 'dataset-name': dataset_name}
    with open(yaml_path, 'w') as fout:
        ruamel.yaml.round_trip_dump(data, fout)


DATASET_NAMES = {
        'CIFAR10', 'CIFAR100', 'Caltech101', 'Caltech256', 'CelebA', 'Cityscapes', 'CocoCaptions', 'CocoDetection',
        'DatasetFolder', 'EMNIST', 'FakeData', 'FashionMNIST', 'Flickr30k', 'Flickr8k', 'ImageFolder', 'ImageNet',
        'KMNIST', 'LSUN', 'LSUNClass', 'MNIST', 'Omniglot', 'PhotoTour',
        'SBDataset', 'SBU', 'SEMEION', 'STL10', 'SVHN',
        'VOCDetection', 'VOCSegmentation', 'VisionDataset',
    }
if __name__ == '__main__':
    args = get_args()
    print(args)
    if args.dataset_name not in DATASET_NAMES:
        raise Exception(f"Not a valid dataset name: {args.dataset_name}")
    load_data_method = getattr(datasets, args.dataset_name)
    load_data_method(args.output_folder, download=True)
    write_meta(args.dataset_name, os.path.join(args.output_folder, '_meta.yaml'))
