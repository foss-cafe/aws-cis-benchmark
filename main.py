import os
import sys
import argparse
from iam.checks import IamChecks

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CIS benchmarking tool', prog='main.py')
    parser.add_argument('--profile', type=str, help='AWS Profile', default='default')
    parser.add_argument('--region', type=str, help='AWS Region', default='us-west-2')
    parser.add_argument('--services', type=str, help='AWS Resource type', nargs='*', default=['iam'])
    parser.add_argument('--checks', type=str, help='CIS checks', nargs='*', default=['1'])

    args = parser.parse_args()
    print(args)
    if "iam" in args.services:
        outputs = []
        iam_check_list = IamChecks(profile="default", region="us-west-2")
        for check in args.checks:
            if check.isnumeric():
                output = iam_check_list.indirect(i=check)
                print(output)
                outputs.append(output)
            elif args.checks[0] == "all":
                pass
    else:
        pass
