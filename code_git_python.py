!pip install GitPython


from git import Repo,remote
import git
import os
import pandas as pd
username = "username_for_github"
password = "password"

repo = git.Repo.clone_from(f'https://{username}:{password}@github.com/_git/NAMEOF THE REPOSITORY',
                           os.path.join('name_how_you_want_to_save_it_localy'))

print('completo')

# agregar archivos al repositorio
texto = pd.read_csv('reporte1.csv')
texto.to_csv('/content/name_how_you_want_to_save_it_localy/folder1/folder2/prueba_Python.json')


repo.git.add("/content/name_how_you_want_to_save_it_localy/folder1/folder2/")
repo.index.commit("Some commit message")
origin = repo.remote(name="origin")
origin.push()
# origin.pull()

