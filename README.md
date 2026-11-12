# LoL SoloQ Tracker
Tracks professional League of Legends players' solo queue matches using the Riot Games API.

##Overview
A Python-based application designed to collect, track, and analyze match data from professional League of Legends players.
Currently, the project focuses on retrieving ranked solo queue match data, extracting player statistics, and storing results in JSON format.

###Tech Stack
Python
Riot Games API
Jenkins
Git / GitHub
JSON

###Features
Retrieve recent ranked solo queue matches.
Extract champion, KDA, and match results.
Store match data in JSON.
Prevent duplicate records.
Automate Python execution and dependency installation through Jenkins.
Securely manage API credentials using Jenkins Credentials.

###Pipeline
<img width="1899" height="671" alt="image" src="https://github.com/user-attachments/assets/4be9a05b-6821-40e1-8ece-593a4b0c3a62" />
GitHub → Jenkins → Checkout → Install Dependencies → Run Python Script → Riot Games API → JSON

###Future Development
Track multiple professional players.
Add competitive match data.
Implement performance statistics and data analysis.
Add automated testing and cloud deployment.
