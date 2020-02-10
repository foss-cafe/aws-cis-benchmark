# aws-cis-benchmark

### Tools needed

- Assuming aws CLI is already configured with profiles
- Python 3.x

### Installation

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
python main.py -h
usage: main.py [-h] [--profile PROFILE] [--region REGION]
               [--services [SERVICES [SERVICES ...]]]
               [--checks [CHECKS [CHECKS ...]]]

CIS benchmarking tool

optional arguments:
  -h, --help            show this help message and exit
  --profile PROFILE     AWS Profile
  --region REGION       AWS Region
  --services [SERVICES [SERVICES ...]]
                        AWS Resource type
  --checks [CHECKS [CHECKS ...]]
                        CIS checks
```

#### Ex

```bash
python main.py --service iam --checks 1
```
