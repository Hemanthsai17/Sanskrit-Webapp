# Sanskrit-Webapp

Hey!
This repository has the final functional not really good looking application, which I have used to enter data.
So, the story is I have hand-labeled sanskrit slokas of the Raghuvamsa Mahakavyas (one of the major mahakavyas i.e. 5).
From my research of various categorization of sentiments and like 9 (Navarasas), 33 (vyabichari bhavas) and while reading I found some have sentiments that do not belong to either.
So, I have created by adding few of those commonly repeating sentiments. Now to get the data digitally to sent it to the model for obtaining embeddings and doing the classification, I chose the on-hot method.
Each sloka is hot with 1, where the sentiment is present in that particular sloka (please refer the data folder for more clarity).
So, the objective of this webapp is to enter the data, after selecting the file, reading the sloka, select the sentiments, save to enter the data into the excel sheet.
You can refer my other repository's readme file named "sanskrit-website-trails" to understand the flow in a decent looking version.

The data folder (only Raghuvamsa) holds the data that I have labeld using this. One more folder named olddata (45) is removed as I have uploaded them in my previously mentioned repository named "sanskrit-website-trails".
index.html -> to select file
label.html -> to label the slokas and save
