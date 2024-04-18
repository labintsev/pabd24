## Git essential  

```git clone <https://user_name/repo_name>``` - клон репозитория на локальную машину.  
```git branch <branch-name> ``` - создать новую ветку.  
```git branch --delete <branchname>``` - удалить ветку.  
```git checkout <name-of-your-branch> ``` - переключиться на ветку.  
```git status ``` - текущее состояние репозитория.  
```git add <file> ``` - добавить файл в систему контроля версий.  
```git commit -m "commit message" ``` - внести изменения в файлы.  
```git push -u <remote> <branch-name> ``` - отправить изменения на удаленный сервер.  
```git fetch ``` - получить обновления с удаленного сервера.  
```git merge <branch-name>``` - внести изменения в текущую ветку из ветки `branch-name`.  
```git pull <remote> ``` - fetch + merge.  
```git revert <hash> ``` - отменить изменения.  