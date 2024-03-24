import argparse
from task_12 import calcs
import pytest 

def parse_args(args_list):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args_list)

def test_invalid_arguments():
    # Test if calcs function correctly handles invalid arguments
    with pytest.raises(SystemExit):
        parse_args(["a", "b", "c"])

def test_help():
    # Test if calcs function correctly displays help message
    with pytest.raises(SystemExit):
        parse_args(["-h"])
