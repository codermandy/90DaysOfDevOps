
# Task-01 
- Create a new branch and make some changes to it.
- Use git stash to save the changes without committing them.
- Switch to a different branch, make some changes and commit them.
- Use git stash pop to bring the changes back and apply them on top of the new commits.

# Task-02
- In version01.txt of development branch add below lines after “This is the bug fix in development branch” that you added in Day10 and reverted to this commit.
- Line2>> After bug fixing, this is the new feature with minor alteration”

  Commit this with message “ Added feature2.1 in development branch”
- Line3>> This is the advancement of previous feature

  Commit this with message “ Added feature2.2 in development branch”
- Line4>> Feature 2 is completed and ready for release

  Commit this with message “ Feature2 completed”
- All these commits messages should be reflected in Production branch too which will come out from Master branch (Hint: try rebase).


````
PS D:\90DaysOfDevOps> git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> dev

PS D:\90DaysOfDevOps> git pull origin master
From https://github.com/codermandy/90DaysOfDevOps
 * branch            master     -> FETCH_HEAD
Merge made by the 'ort' strategy.
 2023/day18/docker-compose.yaml            | 12 ++++++++++
 2023/day18/tasks.md                       | 38 +++++++++++++++++++++++++++++++
 2023/day19/sample_project_deployment.yaml | 20 ++++++++++++++++
 2023/day19/tasks.md                       | 33 +++++++++++++++++++++++++++
 2023/day20/tasks.md                       | 16 +++++++++++++
 5 files changed, 119 insertions(+)
 create mode 100644 2023/day18/docker-compose.yaml
 create mode 100644 2023/day19/sample_project_deployment.yaml
PS D:\90DaysOfDevOps> git checkout -b new_branch
fatal: a branch named 'new_branch' already exists
PS D:\90DaysOfDevOps> ls


    Directory: D:\90DaysOfDevOps


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        16-01-2023     13:22                2023
-a----        03-01-2023     21:59           5284 CONTRIBUTING.md
-a----        14-01-2023     22:52             39 dev_file
-a----        16-01-2023     13:22             39 dev_file.txt
-a----        12-01-2023     00:00            198 feat1.txt
-a----        12-01-2023     00:00             17 feature1.txt
-a----        03-01-2023     21:59          21286 LICENSE.md
-a----        04-01-2023     14:20           1247 README.md


PS D:\90DaysOfDevOps> git branch
  another_branch
* dev
  master
  new_branch
  test
PS D:\90DaysOfDevOps> git checkout new_branch
Switched to branch 'new_branch'
M       2023/day05/task02.sh
D       2023/day06/solution.txt
PS D:\90DaysOfDevOps> git add .
warning: LF will be replaced by CRLF in 2023/day05/task02.sh.
The file will have its original line endings in your working directory
PS D:\90DaysOfDevOps> git branch 
  another_branch
  dev
  master
* new_branch
  test
PS D:\90DaysOfDevOps> git stash
Saved working directory and index state WIP on new_branch: 6e16d8b Merge branch 'master' of https://github.com/codermandy/90DaysOfDevOps into branch1
PS D:\90DaysOfDevOps> git status
On branch new_branch
nothing to commit, working tree clean
PS D:\90DaysOfDevOps> git checkout master
Switched to branch 'master'
Your branch and 'origin/master' have diverged,
and have 52 and 18 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
PS D:\90DaysOfDevOps> git status
On branch master
Your branch and 'origin/master' have diverged,
and have 52 and 18 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

nothing to commit, working tree clean
PS D:\90DaysOfDevOps> git stash pop
Removing 2023/day06/solution.txt
On branch master
Your branch and 'origin/master' have diverged,
and have 52 and 18 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   2023/day04/solution.md
        new file:   2023/day05/solution.md
        new file:   2023/day05/task01.sh
        new file:   2023/day05/user_list.txt
        new file:   2023/day06/solution.md
        new file:   2023/day07/solution.md
        new file:   2023/day11/change1.txt
        new file:   2023/day11/change2.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   2023/day05/task02.sh
        deleted:    2023/day06/solution.txt

Dropped refs/stash@{0} (1be95cd4628c2e429ff47f042869f833ad04005b)
PS D:\90DaysOfDevOps> git checkout dev
Switched to branch 'dev'
A       2023/day04/solution.md
A       2023/day05/solution.md
A       2023/day05/task01.sh
M       2023/day05/task02.sh
A       2023/day05/user_list.txt
A       2023/day06/solution.md
D       2023/day06/solution.txt
A       2023/day07/solution.md
A       2023/day11/change1.txt
A       2023/day11/change2.txt
PS D:\90DaysOfDevOps> git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   2023/day04/solution.md
        new file:   2023/day05/solution.md
        new file:   2023/day05/task01.sh
        new file:   2023/day05/user_list.txt
        new file:   2023/day06/solution.md
        new file:   2023/day07/solution.md
        new file:   2023/day11/change1.txt
        new file:   2023/day11/change2.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   2023/day05/task02.sh
        deleted:    2023/day06/solution.txt
        modified:   2023/day10/Devops/Git/version01.txt

PS D:\90DaysOfDevOps> git add .
PS D:\90DaysOfDevOps> git branch
  another_branch
* dev
  master
  new_branch
  test
PS D:\90DaysOfDevOps> git commit "Added feature2.1 in development branch"
error: pathspec 'Added feature2.1 in development branch' did not match any file(s) known to git
PS D:\90DaysOfDevOps> git commit -m "Added feature2.1 in development branch"
[dev 0ac3be2] Added feature2.1 in development branch
 11 files changed, 106 insertions(+), 32 deletions(-)
 create mode 100644 2023/day04/solution.md
 create mode 100644 2023/day05/solution.md
 create mode 100644 2023/day05/task01.sh
 rewrite 2023/day05/task02.sh (88%)
 create mode 100644 2023/day05/user_list.txt
 create mode 100644 2023/day06/solution.md
 delete mode 100644 2023/day06/solution.txt
 create mode 100644 2023/day07/solution.md
 create mode 100644 2023/day11/change1.txt
 create mode 100644 2023/day11/change2.txt
PS D:\90DaysOfDevOps> git lo
0ac3be2 (HEAD -> dev) Added feature2.1 in development branch
5e18016 Merge branch 'master' of https://github.com/codermandy/90DaysOfDevOps into dev
7fc81ac (origin/master, origin/HEAD) Merge pull request #87 from RishikeshOps/patch-10
3789b5d Update tasks.md
4c4f902 Merge pull request #86 from sitchatt/patch-5
681e152 Create sample_project_deployment.yaml
7ebb548 Merge pull request #85 from sitchatt/patch-4
PS D:\90DaysOfDevOps> git lo    
0ac3be2 (HEAD -> dev) Added feature2.1 in development branch
5e18016 Merge branch 'master' of https://github.com/codermandy/90DaysOfDevOps into dev
7fc81ac (origin/master, origin/HEAD) Merge pull request #87 from RishikeshOps/patch-10
3789b5d Update tasks.md
4c4f902 Merge pull request #86 from sitchatt/patch-5
681e152 Create sample_project_deployment.yaml
7ebb548 Merge pull request #85 from sitchatt/patch-4
95e18a5 Update tasks.md
2dc360d Merge pull request #83 from Varsha-Verma/patch-6
216a60a Update tasks.md
f323ccd Merge pull request #82 from RishikeshOps/patch-9
bab412b Create docker-compose.yaml
f382ce0 Merge branch 'master' of https://github.com/codermandy/90DaysOfDevOps into dev
e33954a Merge pull request #78 from LondheShubham153/LondheShubham153-patch-1
81d8ea0 Update tasks.md
eb2904f Merge pull request #77 from RishikeshOps/patch-7
ffc8def Update tasks.md
e38e801 Merge pull request #76 from LondheShubham153/day15
8000ec6 added day 16 task
24a247c proper format edit till task 3
a12f33c Merge pull request #74 from LondheShubham153/day15
12a309e added day 15 tasks
6af4584 Merge branch 'master' of https://github.com/codermandy/90DaysOfDevOps into dev
3b9f00f Merge pull request #70 from RishikeshOps/patch-6
9924ac7 Update tasks.md
375e8da Merge pull request #69 from LondheShubham153/feat/day-14
7a41fdf added day 14 task modifications
d6781a7 Merge pull request #68 from Varsha-Verma/patch-4
23ed188 Update tasks.md
a8712a7 Merge pull request #66 from Varsha-Verma/patch-3
e19b2ae Update tasks.md
84913aa file modified
2c04c12 this is the commit message
f5cd3b1 Merge pull request #63 from Varsha-Verma/patch-2
13bfff5 Optimized the feature
5e8216d (origin/dev) Feature2 completed
fe9a297  Added feature2.2 in development branch
37ddb2a Added feature2.1 in development branch
dfdae1c Added feature2.1 in development branch
d220506 Merge branch 'dev' of https://github.com/codermandy/90DaysOfDevOps into dev
be23df9 Update tasks.md
0c9f615 added new feature
3c29ae2 Added new feature
d5a7505 Added new feature
8d64be3 changes commmited
03c2260 complete task 4
52cf8ac Added new feature
31f7d69 Update tasks.md
0aa0093 Update tasks.md
a4a66b2 Merge pull request #61 from sitchatt/patch-2
7756cdd Updated Day-11 task
079c8b3 conflict resolved
913d4dd conflict resolved
79bee8e remote-commit
c316308 this is from local
d1683c8 remote-opinion
PS D:\90DaysOfDevOps> git revert 0c9f615
Auto-merging 2023/day10/Devops/Git/version01.txt
CONFLICT (content): Merge conflict in 2023/day10/Devops/Git/version01.txt
error: could not revert 0c9f615... added new feature







[dev a0031ca] Revert "added new feature"
 1 file changed, 7 insertions(+), 1 deletion(-)
PS D:\90DaysOfDevOps> git commit -m "This is the advancement of previous feature
>> "
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   2023/day10/Devops/Git/version01.txt

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\90DaysOfDevOps> git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add
PS D:\90DaysOfDevOps> git add 
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"
PS D:\90DaysOfDevOps> git add ,
>> ^C
PS D:\90DaysOfDevOps> git add .
PS D:\90DaysOfDevOps> git commit -m "Feature 2 is completed and ready for release"
[dev f04ac3f] Feature 2 is completed and ready for release
 1 file changed, 4 insertions(+), 12 deletions(-)
 rewrite 2023/day10/Devops/Git/version01.txt (81%)
PS D:\90DaysOfDevOps> git checkout master
Switched to branch 'master'
Your branch and 'origin/master' have diverged,
and have 52 and 18 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
PS D:\90DaysOfDevOps> git rebase dev
Successfully rebased and updated refs/heads/master.
PS D:\90DaysOfDevOps> git status
On branch master
Your branch is ahead of 'origin/master' by 55 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS D:\90DaysOfDevOps> git push
Enumerating objects: 137, done.
Counting objects: 100% (113/113), done.
Delta compression using up to 8 threads
Compressing objects: 100% (70/70), done.
Writing objects: 100% (83/83), 9.77 KiB | 370.00 KiB/s, done.
Total 83 (delta 31), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (31/31), completed with 4 local objects.
To https://github.com/codermandy/90DaysOfDevOps.git
   7fc81ac..d8788ab  master -> master
PS D:\90DaysOfDevOps> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
PS D:\90DaysOfDevOps> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   2023/day04/solution.md
        modified:   2023/day05/solution.md
        modified:   2023/day05/task01.sh
        modified:   2023/day05/task02.sh
        modified:   2023/day05/user_list.txt
        modified:   2023/day06/solution.md
        modified:   2023/day07/solution.md

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\90DaysOfDevOps> git add .    
warning: LF will be replaced by CRLF in 2023/day05/task02.sh.
The file will have its original line endings in your working directory
PS D:\90DaysOfDevOps> git branch
  another_branch
  dev
* master
  new_branch
  test
PS D:\90DaysOfDevOps> git commit -m 'refactoring of tasks'
[master 63eb336] refactoring of tasks
 7 files changed, 83 insertions(+), 5 deletions(-)
PS D:\90DaysOfDevOps> git status
Writing objects: 100% (14/14), 2.81 KiB | 720.00 KiB/s, done.
Total 14 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
To https://github.com/codermandy/90DaysOfDevOps.git
   d8788ab..63eb336  master -> master
PS D:\90DaysOfDevOps> git pull
Already up to date.
PS D:\90DaysOfDevOps>
````

# Task-03
- In Production branch Cherry pick Commit “Added feature2 in development branch” and added below lines in it:
- Line to be added after Line3>> This is the advancement of previous feature
- Line4>>Added few more changes to make it more optimized.
- Commit: Optimized the feature