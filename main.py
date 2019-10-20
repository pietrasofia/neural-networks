import sys

from files_reader import read_network_file, read_initial_weights_file, read_dataset_file


def main():
    print("Starting Neural Networks Algorithm...")

    # 1st parameter: network.txt
    regularization_factor, networks_layers_size = read_network_file(
        sys.argv[1])

    # 2nd parameter: initial_weights.txt
    initial_weights = read_initial_weights_file(sys.argv[2])

    # 3rd parameter: dataset.csv
    dataset = read_dataset_file(sys.argv[3])


if __name__ == "__main__":
    main()