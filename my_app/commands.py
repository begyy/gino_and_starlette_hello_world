import argparse

parser = argparse.ArgumentParser(description='Migrations')
parser.add_argument('command', type=str)
args = parser.parse_args()
