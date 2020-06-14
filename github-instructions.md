# GitHub First Timer Instructions
## Signing Up on GitHub
Go to https://www.github.com  
As seen below in the figure attached, click sign up on the right corner.

![GitHub signup screen](./images/intro-github/github-1.jpg)

Follow the steps required by GitHub to complete your registration and verify your email for full access to GitHub.

## Setting Up GitHub
After you have signed up for GitHub, go to the link below and install Git on your local machine.  
In order to be able to use Git commands, you will need to have Git installed on your machine.  
[Click here to download Git](https://git-scm.com/downloads)  

![](./images/intro-github/github-2.jpg)

Once you are on the website shown in the figure above, you can either click on the "Download x.xx.x for (Your Operating System)" or choose your download manually under the Downloads section.  
After the download finishes, install it with pre-configured options or you can manually choose it if you know what you are doing.

## Operating Command Prompt/Terminal
Before going into how to use git, I would like to show you how to operate command prompt (Windows) and terminal (MacOS) first. However, the pictures shown will be on Windows OS as that is the only one I own.

In order to access command prompt, you have to go to your start menu on the lower left of the screen and type "command prompt" on the search bar. Click on it to open up the program. You will get something similar to the figure below.  

![](./images/intro-github/github-3.jpg)

In this application, you will be able to use a multitude of commands to access and control your computer. But in this document, I will only teach you how to access files and use basic git commands for learning.

* C:, D:, E: - choose whatever drive you would like to be in  
* dir (directory) - list out files and folders in the current directory (ls for MacOS)  
* cd (change directory) - change your current directory to the folder that you would like to access, you can do this with the folder's name, or with . for current directory, .. for parent directory, and ~ for root (uppermost) directory  

![](./images/intro-github/github-4.jpg)

In both figures above and below indicate the actual usage of commands on my computer. First, I accessed my drive D because all of my files related to this project are in drive D. Then, I typed "dir" to see what files and folders are in my current directory and I used "cd" to change my path to the next folder closer to my project folder. I then repeated the process of using "dir" and "cd" until I reached my Python working directory.  

![](./images/intro-github/github-5.jpg)

## Generating an SSH Key
After you have installed git from git-scm, you will also receive an application called, "Git Bash". For this part of the document, you will be opening "Git Bash" from your start menu again. Once you open application, you will see a screen like below.

![](./images/intro-github/github-6.jpg)

The objective of this section of the document is to grant you access to pushing and pulling from GitHub. You will first type on your Git Bash, 'ssh-keygen -t rsa -b 4096 -C "{your email}"'. Once you type that in, it will start the process of generating an ssh key for your access to git. You will find the screen below showing up asking for what you'd like your file's name to be. Hit enter to use the default name. You'll then be asked to type the password to the file (Please remember the password because you will need it for pushing and pulling files from repositories). Also, while typing your password, don't worry if you don't see your password on the screen, they are actually already typed, keep typing.  

![](./images/intro-github/github-7.jpg)

After you have input your file's name and password, you will receive a screen resembling the screen below.

![](./images/intro-github/github-8.jpg)

## Adding Public SSH Key
After you have successfully created an ssh key, you will need to add your public key to your GitHub account to help identify your contributions. In order to do that, you will need to go back to your GitHub website, and click on your profile picture on the upper right as you see in the figure below.  

![](./images/intro-github/github-9.jpg)

You will see the option "Settings", click on it and it will lead you to the figure below. Once you are here, you then go to "SSH and GPG keys" section.

![](./images/intro-github/github-10.jpg)

In this section, you will see SSH keys and GPG keys that you can add. This is where you add your generated SSH key. Click on "New SSH key" on the upper right.

![](./images/intro-github/github-11.jpg)

You will be led to the figure below and you can see that you can give a name to your SSH key that you are adding and a section to input your public key.

![](./images/intro-github/github-12.jpg)

You will then go back to your Git Bash in order to copy the public key for GitHub. Before you copy the key, type "ls -al ~/.ssh" to check what ssh keys you have on your computer. If you use the default name, you should see "id_rsa" and "id_rsa.pub". You will want to copy the public key from "id_rsa.pub". Follow the command below "clip < ~/.ssh/id_rsa.pub" to copy your public ssh key.

![](./images/intro-github/github-13.jpg)

Once you have your key copied, you will go back to the SSH key addition page you were on on GitHub. You will paste the key you have copied onto the "Key" section of the page. Then, you click "Add SSH key" to finish adding the key.

![](./images/intro-github/github-14.jpg)

This should show you that you now have a new key in your SSH keys list.

## Cloning Repositories to Your Local Computer
![](./images/intro-github/github-15.jpg)
![](./images/intro-github/github-16.jpg)

## Branching Git For Your Own Implementation
![](./images/intro-github/github-17.jpg)
![](./images/intro-github/github-18.jpg)
![](./images/intro-github/github-19.jpg)

## Pushing Your Files Back to Repositories
![](./images/intro-github/github-20.jpg)
![](./images/intro-github/github-21.jpg)
![](./images/intro-github/github-22.jpg)
![](./images/intro-github/github-23.jpg)
![](./images/intro-github/github-24.jpg)

## Pulling Your Files From Repositories
![](./images/intro-github/github-25.jpg)
![](./images/intro-github/github-26.jpg)

## More commands teaching later :P
