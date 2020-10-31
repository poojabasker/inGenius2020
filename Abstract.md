Abstract of CricBOT
Posted by :BOT Fury
Pooja Basker
Shreeja Shukla 
Shreya Singh
Srikanth Shankar

Project Name : CricBOT
Upload Date : 31-10-2020
Platform : Discord, Jupyter 
Programming Language : Python
Project Type : Discord ChatBot

DISCORD BOT: 
A discord bot coded in python that listens for the commands typed by the user (predefined 4 commands in the code as of now). 
The commands understood by the bot are-
-awaken
-help
-livescore
-commentary (aliases: -comm, -comment)
All the commands must be preceded by an hyphen ‘-’
This bot is connected to the CricBuzz API library and uses it to find the livescore and commentary of the current ongoing match.
The user can view these by using commands -livescore and -commentary.
To know about the command documentation, the user can use the -help command.

Further Implementation: Connect the prediction code written in Jupyter Notebook to the discord bot.

PREDICTION JUPYTER NOTEBOOK
Initially, the categorical data are converted into numerical data for easy implementation of the model and use them. Later, the IPL teams are encoded to initial and then to team IDs.
Comparative models of toss winner and match winner v/s toss winner and match losers and analysed. The venue attribute is also taken into consideration.
Generic models used:
logistic Regression
Gaussian NAive bayes algorithm
Applying KNN algorithm
SVM classification
Gradient boost algorithm
Decision tree algorithm
Random forest classifier
From the generic models, it is seen that SVM, Decision Tree algorithm, and Random Forest Classifiers have an accuracy of 87%. 

