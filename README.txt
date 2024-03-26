Since the Git extension is mid, heres some of the commands we'll use that you can copy/paste.

## Update ALL Branches (do this as often as possible. If working on a commit -> git stash push -m "Your descriptive message")
./fetch.sh

## To merge latest changes from MAIN branch to your REMOTE branch
1. git checkout your_branch_name (or navigate to your branch)
2. git pull origin your_branch_name
3. git fetch origin main
4. git merge origin/main
5. git push origin your_branch_name

These need tweaking I think:

## Pushing commits to dev branch (Pull request with testing) 
1. git checkout dev
2. git pull origin dev
3. git push -u origin your_branch_name
4. git push origin dev
5. Create pull request for review in github
6. Revise based on feedback

## Push from dev to main *CHECK WITH ALL TEAM MEMBERS*
1. git checkout dev
2. git pull origin dev
3. git checkout main
4. git pull origin main
5. git merge dev
6. git push origin main
