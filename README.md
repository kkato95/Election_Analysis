# Election_Analysis
## Overview of Election Audit:
The purpose of the PyPoll Challenge election audit analysis is to observe the vote totals, to tally the number of votes and their percetnages across the three counties, and to list the vote distribution across the candidates. We are able to use the raw data collected from the polling station and use various looping methods to build lists and dictionaries for the election audit tally.

## Election-Audit Results:
Using the data to run analysis we we able to calculates the various topics.
1. Using a for loop and 2 nested if-statements to build the lists of candidates and their vote count and county and their vote count: Total Votes - 369,711  
![image](https://user-images.githubusercontent.com/99375741/158099491-ec2740ae-9a48-4b7d-910b-ff26800be9a4.png)  
![image](https://user-images.githubusercontent.com/99375741/158099306-0e96fd00-5896-4e2a-bf86-bb5dc93436c2.png)  

2. Breakdown of number of votes and percent for each county:  
![image](https://user-images.githubusercontent.com/99375741/158099611-3df0694a-ecbd-4e2e-8d04-0edc029ee416.png)  
![image](https://user-images.githubusercontent.com/99375741/158099725-30701415-2fba-4363-baa8-428937aca1e4.png)  

3. Denver has the largest number of votes.  
![image](https://user-images.githubusercontent.com/99375741/158099830-c218a7c9-8c1b-44d3-93b2-c0d8092c735b.png)  
![image](https://user-images.githubusercontent.com/99375741/158099910-84f87844-0fcc-4a71-a557-f99e59f9149e.png)  

4. Diana DeGette received 73.8% (85,213), Charles Casp Stockham recieved 23.0%, and Raymnd Anthony Doane recieved 3.1% (11,606).  
![image](https://user-images.githubusercontent.com/99375741/158100036-9de755bd-d3ab-4192-a8c8-54ca9c8cf184.png)  

5. Diana DeGette won the election with a total of 272,892 and winning percentage of 73.8%  
![image](https://user-images.githubusercontent.com/99375741/158100063-360f67f5-f717-472f-a210-c7334c2dd2b8.png)  

## Election Audit Summary:  
The script created can be used in other elections to preform the same election audit. There are 2 things that must be changed for this code to work in other instances.  
1. The first peice of code that would have to be changed is the file from which Python is reading. We would have to update the path 'file_to_laod' to read the new data.  
![image](https://user-images.githubusercontent.com/99375741/158100641-d16b4542-4297-403d-aee2-94109b036712.png)  
2.The second peice of code that must be updated is the location Python is writing to. We would change the path to the new write_to file.  
![image](https://user-images.githubusercontent.com/99375741/158100862-5e835179-8dcd-43e9-ac64-beedf98cd2d4.png)  
