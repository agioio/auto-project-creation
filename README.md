# PREREQUISITES
* ```cd to/project/directory/```
* pip3 install -r requirements.txt
* create env:
```touch .env```
* add GITHUB_TOKEN and FILEPATH to the env (check at the bottom for a example)
* In the create file:
```change >>> acc <<< to your github username```
* Check create.py if anything is required


**If you want to make the program executable from anywhere use one of these commands:**

* **If using bash:**

```echo alias create="path/to/create/script" >> ~/.bashrc```

* **If using zsh:**

```echo alias create="path/to/create/script" >> ~/.zshrc```

# USAGE

To use the tool just use: 

```create [file name]```
For example:

```create test 1```

# EXTRA INFORMATION

* Do not make a repo you already have as it will not create it.

# ENV FILE

```
GITHUB_TOKEN="124f43fwq2t45gw45y56uw34"
FILEPATH="path/to/this/project"
```
Your github token is your personal access token.