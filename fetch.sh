#!/bin/bash

# Fetch all branches from the remote
git fetch --all

# Loop through all remote branches
for branch in $(git branch -r | grep -v '\->'); do
    # Trim the "origin/" part of the branch name
    local_branch=${branch#origin/}
    
    # Check out the local branch (creates it if it doesn't exist)
    git checkout -B "$local_branch" "$branch"
done

# Switch back to the main branch (or any branch of your choice)
git checkout main
