import dotenv
import pandas as pd
from github import Github
from github import Auth

config = dotenv.dotenv_values('.env')
GITHUB_TOKEN = config['GITHUB_TOKEN']
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

df = pd.read_csv('../docs/results.csv')


def graduate(repo_url: str) -> int:
    score = 0
    try:
        user_repo = repo_url.split('.com/')[-1]
        repo = g.get_repo(user_repo)
        score += 2
        if repo.get_branch(branch="tmp"):
            score += 1
        if repo.get_branch(branch="master").protected:
            score += 1
    except AttributeError:
        print('No way for ', repo_url)
    return score


df['1'] = df['git'].map(graduate)
df.to_csv('tmp.csv')

g.close()
