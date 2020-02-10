import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CIS benchmarking tool', prog='main.py')
    parser.add_argument('--profile', type=str, help='AWS Profile', default='default')
    parser.add_argument('--service', type=str, help='AWS Resource type', nargs='*', default=['iam'])
    parser.add_argument('--checks', type=str, help='CIS checks', nargs='*', default=['1'])

    args = parser.parse_args()
    print(args)
