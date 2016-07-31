
![Alt text](http://i.imgur.com/Fd1aRP8.png)

# Lambda

https://2016.hackerspace.govhack.org/content/taxless

This platform was designed for the GovHack hackathon hosted in Sydney in July 2016.

TaxLess uses open ATO data to optimise your next return, by comparing your deductions with people like you.

By analsying over 250 thousand tax returns, our web tool discovers where your deductions are falling short, and what can you do about them.

Using a stack that consisted of sci-kit learn and other machine learning tools, we were able to determine the amount of tax that someone should be receiving, by analyzing individals from the data set using deep learning and making links with the data provided by the user.

The information provided by the user consisted of:
- Gender
- Age Range
- Occupancy Category
- Marital Status
- Postcode
- Was a tax agent used
- Sum of salary and wages

Using your age, occupation, earnings amount, region and gender, we group you with similar taxpayers, and find out how you rank in the various deduction categories among them using a clustering algorithm. 

A significant difference likely indicates that you are either under claiming or under investing. For example, you may be self-contributing nothing to supperannuation when others are doing 10%, or you simply forgot to report expenses. 

By using the ATO's open tax return datasets, which covers 2% of taxpayers, we can also show users with no statistical background key difference and similiarities between different demographics.

#### Dataset Name: 
Taxation statistics - Individual tax return sample files
##### Publishing Organisation/Agency: 
ATO
Jurisdiction of Data: 
Australian Government
##### Dataset URL: 
http://portal.govhack.org/datasets/2016/australia/australian-taxation-office/tax...
##### How did you use this data in your entry?: 
Firstly, we use K-means clustering (by Occupation code, salary and wages amount, region, age, marital status and gender) to group users into clusters. Secondly, within the clusters we use ridge regression (aided with dummy variables for the discrete variables) to understand, in a fine grained way, how tax effective particular users are and where they get deductions. Finally, we profile the clustering by showing the distribution of variables in the different groups to study their differences among the clusters.
