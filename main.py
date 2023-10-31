from functions import inputs
import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('indir', type=str, help='')
parser.add_argument(
    '--directory_name',
    type=str,
    default='',
    help=''
)
args = parser.parse_args()
inputs(args.indir, args.directory_name)