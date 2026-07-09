## What is the Command Line
Normally we use our mouse:
```Click Folder
↓
Open Folder
↓
Open File
```

Linux lets you do everything with commands:

``` 
mkdir project  # create folder

cd project # go inside the folder

touch main.py # create file
```

## Topic 1 — Navigation
> #### pwd

**Meaning:** Print Working Directory
Shows your current location.
```bash
pwd
```

Example output:
```
/home/code/projects
```
## Real-Life Analogy

Imagine asking:
```
"Where am I?"
```
Linux replies with your current folder.

```ls```

Lists the files and folders.

```bash
ls
```

Output:
```
main.py

assistant.py

notes.txt
```
>[!CAUTION] Common Beginner Mistake

Typing:
```bash
dir
```

```dir``` works on Windows, but ```ls``` is the standard Linux command.

```cd```

Changes directories. Going inside Documents
```
cd Documents
```
Go back previous one folder:
if you are in ```/code/python```
```bash
cd ..
```
Now you are in ```/code```

Go home:
```bash
cd ~
```

### Practical Example
```
cd Projects

cd AI

pwd
```

### Output:

```
/Projects/AI
```

## Topic 2 — Creating Files & Folders
```mkdir```

Creates a directory.

```bash
mkdir AI_Project
```
Now:
```
AI_Project/
```

```touch```

Creates an empty file.
```
touch main.py
```
Now:
```
main.py
```
exists.

### Practical Example
```bash
mkdir Notes

cd Notes

touch python.txt

touch sql.txt

touch ai.txt
```

## Topic 3 — Copy Files
```cp```

Copy:
```bash
cp notes.txt backup.txt
```

Result:
```
notes.txt

backup.txt
```

## Topic 4 — Move & Rename
```mv```

Rename:
```bash
mv old.txt new.txt
```

Move:
```
mv notes.txt Documents/
```
### Practical Example
```
mv python.txt python_notes.txt
```

### Topic 5 — Delete
```rm```

Delete:
```bash
rm notes.txt
```

Delete a folder recursively:
```
rm -r Notes
```
>[!CAUTION] Be careful. Linux usually doesn't have a recycle bin for rm.

| Command         | Purpose                    |
| --------------- | -------------------------- |
| `pwd`           | Show current directory     |
| `ls`            | List files and folders     |
| `cd`            | Change directory           |
| `mkdir`         | Create directory           |
| `touch`         | Create empty file          |
| `cp`            | Copy files                 |
| `mv`            | Move or rename files       |
| `rm`            | Delete files or folders    |
| `cat`           | Display file contents      |
| `find`          | Search for files           |
| `grep`          | Search inside files        |
| `chmod`         | Change permissions         |
| `ps`            | Show running processes     |
| `kill`          | Stop a process             |
| `ping`          | Test network connectivity  |
| `curl`          | Fetch data from a URL      |
| `zip` / `unzip` | Compress and extract files |

