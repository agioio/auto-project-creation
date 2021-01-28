import argparse, os
from dotenv import load_dotenv
from github import Github

load_dotenv()

path = os.getenv("FILEPATH")
token = os.getenv("GITHUB_TOKEN")

user = Github(token).get_user()

my_arg = argparse.ArgumentParser()
my_arg.add_argument('input',action='store',nargs='+')

args = my_arg.parse_args()

os.makedirs(path + "/" + "-".join(args.input))
user.create_repo("-".join(args.input),auto_init=True)