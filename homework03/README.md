# Water Turbidity Analysis

### Overview
Directory 'Homework03' contains one python script that calculates the average turbidity of water from the 5 most recent data points. Another python script is included in the directory that tests the functionality of the functions utilized in the previous script. It is relevant to analyze the turbidity of water to determine if the water is safe to use or if the place from where the water was obtained from has to be put under a water boil notice.

## Data Set Download
In order to utilize the python script 'analyze_water.py', it is required to download a list of directories. The data required can be found in the following link:
https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
It is reccomended to create a new file named turbidity_data.json and paste the contents from the link into the file. Once the data is acquired, the scripts can be run.

# analyze_water.py Description
This script takes in a list of directories that contains the water quality data set. From this information, this script calculates the average of the most recent five data points, checks if the turbidity is below a safe threshold, and calculates the minimum time required for turbidity to fall below the safe threshold.

# How to Run
To run the code, first you must download the list of directories as explained in the 'Data Set Download' section. Once such data is acquired, the code can be run by using 'python3 analyze_water.py'. After running the code, three lines of output will be print out. And example of such output is:
Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours   
