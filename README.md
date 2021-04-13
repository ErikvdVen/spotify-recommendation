# Spotify Recommendation ML/DL
I am building my own custom recommendation system for personal use by using Docker, Elasticsearch, Flask (Python) and a NVIDIA Jetson Nano, which will be used to build and run the recommendation models.

I use the [Music Streaming Sessions Dataset (MSSD)](https://arxiv.org/abs/1901.09851), originally published for a competition by Spotify. The dataset contains both listening session data and a lookup table for song features.

This repository contains the whole project, except for the data. I will share my model source files as well, which you can use to build your own models. If I'm allowed to share any pre-trained models as well (I have to look into the dataset license), I will do that as well.

1. [ Project description ](#project-desc)
1. [ Setup VS Code environment ](#setup-vscode)

<a name="project-desc"></a>
## Project installation
So to run the project, make sure docker-compose is installed correctly before executing the following command to build the Dockerfile, which will hold the Python app.

```Shell
docker-compose build
```
And after building, start the cluster

```Shell
docker-compose up
```

<a name="setup-vscode"></a>
## Setup VS Code for remote code execution
In case you would like to work on the project using VS Code, I would like to share some helpful configurations I came accross during development of this project.

While Microsoft might already have this built in VS Code, I couldn't find an easy way of executing my local files on a remote server using VS Code. While PyCharm already contains such functionality, it seems VS Code still wants you to connect to the remote server using SSH. This isn't always the best choice, if you are developing locally with GIT setup and everything. So thanks to [@verified.human on StackOverflow](https://stackoverflow.com/a/54789809/1843511), there is an easier way of doing this.

First add a `tasks.json` file inside the `.vscode` folder of your current workspace with below mentioned content. 

Make sure to replace `<user>@<ip_address>` with the right username and location address of the remote server. You might want to replace the `python3` command with just `python`, depending on your installation environment.

```JSON
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Synchronize Code",
            "type": "shell",
            "command": "rsync -axv --exclude-from=${workspaceFolder}/.vscode/rsync-exclude.lst --max-size=5MB \"${workspaceFolder}\" <user>@<ip_address>:dev/code-sync/",
            "problemMatcher": [],
            "isBackground": true,
            "presentation": {
                "echo": false,
                "reveal": "silent",
                "focus": false,
                "panel": "shared",
                "clear": false
            }
        },
        {
            "label": "Remote Execute",
            "type": "shell",
            "command": "ssh -n <user>@<ip_address> \"python3 ~/dev/code-sync/${workspaceFolderBasename}/${relativeFile}\"",
            "dependsOn": [
                "Synchronize Code"
            ],
            "problemMatcher": []
        }
    ]
}
```

To prevent having to enter your password everytime you would like to run this command, I would advice to set up [SSH keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804) so you can access the remote server safely and without entering any password everytime you execute this task.

### Add keybindings
It might be helpful to execute a file remotely everytime, just by hitting a keyboard shortcut. You can add one, which will execute the task you just created.

In VS Code, hit `CTRL + Shift + P` and look for `Preferences: Open Keyboard Shortcuts (JSON)`. A file called **keybindings.json** will open. It might just contain an empty array, in that case you can replace everything with the code below. Or you could just add the object. 

```JSON
[
    {
        "key": "ctrl+shift+r",
        "command": "workbench.action.tasks.runTask",
        "args": "Remote Execute"
    }
]
```

## Setup remote Jupyter Notebook server

```Shell
[Unit]
Description=Jupyter Notebook[Service]

[Service]
Environment="LD_PRELOAD=$LD_PRELOAD:/usr/lib/aarch64-linux-gnu/libgomp.so.1" # For NVIDIA Jetson Nano
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/erik/.local/bin/jupyter-notebook --config=/home/erik/.jupyter/jupyter_notebook_config.py
User=erik
Group=erik
WorkingDirectory=/home/erik/Development/notebooks
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```