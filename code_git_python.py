from git import Repo,remote


import sys
sys.path.append('/usr/local/airflow/dags')
rw_dir = 'archivo.json'
repo = Repo()

'''Enter code to commit the repository here.
After commit run the following code to push the commit to remote repo.
I am pushing to master branch here'''

git_push_automation()


origin = repo.remote(name='origin')
origin.push()
