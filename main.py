import argparse
from app.controller.controller import Controller

def main(data_dir=None):
    app = Controller(data_dir)
    app.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs the Boat Food Inventory Manager.')
    parser.add_argument('--data-directory', type=str, default=None, help='Path to the data directory')

    args = parser.parse_args()

    main(args.data_directory)
