import dotenv
import pandas as pd
from github import Github, UnknownObjectException
from github import Auth

config = dotenv.dotenv_values('.env')
GITHUB_TOKEN = config['GITHUB_TOKEN']
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

df = pd.read_csv('docs/results.csv')
df['1'] = df['1'].astype(int)


def graduate(repo_url: str) -> int:
    score = 0
    try:
        user_repo = repo_url.split('.com/')[-1]
        repo = g.get_repo(user_repo)
        files = repo.get_contents('src')
        files = [f.name for f in files]
        pipeline_files = ['upload_to_s3.py', 'download_from_s3.py', 'preprocess_data.py']
        if set(pipeline_files).issubset(files):
            score = 2
    except (AttributeError, UnknownObjectException):
        print('No way for ', repo_url)
    return score


df['2.pipeline'] = df['git'].map(graduate)
df = df.reindex(sorted(df.columns), axis=1)
df.to_csv('tmp2.csv', index=False)

g.close()
