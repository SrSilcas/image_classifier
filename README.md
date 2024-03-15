# image_classifier

## Description about the program
This program reads images into a folder and using covolutional network (resnet50) the program classifies it if it is an animal and saves the classification into a csv

## Installation and Use
How to run this program firstly you need to have Windows 11 installed on your computer secondly you need to have 
installed python 3.9.17 or newer case you don't have you can download 
[here](https://www.python.org/ftp/python/3.12.0/python-3.12.0b2-amd64.exe), after that you will need to install anaconda if you don't have you can do the download [here](https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Windows-x86_64.exe). Finally you can install the program dependencies, to do this you need to go into the program folder and then access the [**dependencies**](/dependencies/) folder after that just run the [**dependencies.bat**](dependencies\dependencies.bat) file after that you can test to see if the environment was installed successfully open cmd or comand prompt and put two command frist this below.

    conda init

Than you put that command below.

    conda activate image_classify

If the ambient can't activate you need use anaconda prompt digite **anaconda prompt** into Windows search when open you need to find the program's [dependencies](/dependencies/) folder and into this folder you use the command below.

    conda env create -f environment.yml    

And after you can install the environment variables, just activate the conda environment with the command below

    conda activate image_classify

And now you just need run the python file ```main.py```, when you ronnig this program you choose the folder that contains the images and after that you cassify the images within the folde.

## Pipeline

As the program was created in the first place, it was necessary to understand the program's requirements, after understanding them, it was necessary to understand how to classify images quickly and reliably, in view of this it was possible to choose the pre-trained ResNet-50 neural network (CNN), In choosing the neural network, Tkinter was chosen as the interaction window with the user, taking into account that Tkinter itself has a function to search and choose a folder within the computer's directory. In view of this, I formed a small simple software architecture where I divided the files into 3 directories which are the **view** where the main program window is, the **controller** where the image classification classes are and the class for writing information into csv and finally the directory **utils** where there are functions that make it possible to carry out the main functions of the program.
