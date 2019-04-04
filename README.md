# MarblesGame_ImageMaker
A python script for creating images for the Marbles Game

This Repo holds all the files you will need to create images similar to this: 

Here is how you can get started:
1) You will need to clone or download the entire repository. 
2) Then install [Blender](https://www.blender.org/)
3) Open the AutomateBuild.blend file located in this repository.
4) Run the python script from inside the built-in python shell in Blender.

How it works:
The python script reads the variables in the trialInfo.csv file in order to get the number of green and purple marbles for each side of the image (left/right). It then randomly positions each marble on the screen and prevents marbels form overlapping. For each image it renders the file and saves a .jpg to the main directory.

To Do list:
1) I plan to update this to allow different size marbles
2) I also need to improve the shell script to run blender in the background and pipe the input directly in.
