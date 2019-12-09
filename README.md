# Live-NBA-Scores
## Intro
<kbd>
<img src="https://i.imgur.com/0OALjxe.png"></img>
</kbd>

A single web application that presents NBA game scores from the last 24 hours and being updated live.

You can filter the results by a team's name, and press the scoreboards to open up the game's ESPN dashboard.

The app consists:
* REACT frontend to present the different matches.
* Flask REST api, that serves the frontend --> it pulls data from the DB send the updated game information to the UI.
* Scheduled scraper, that scrapes data from ESPN.com every 30 seconds and updates the DB accordingly.
* MongoDB that stores all the matches information and the teams logos (for the UI).



## Usage
Notice: Python 3.7+ is required!

Steps:
1. In the folder in which you want to deploy the service, open CMD or Terminal and enter:
```
git clone https://github.com/YotamNHL/Live-NBA-Scores.git
```

2. Now, enter the folder created, and install all required python modules:
```
cd Live-NBA-Scores
pip install -r requirements.txt
```

3. Now, the 'credentials.csv' file (sent via email) MUST be placed into the backend folder. This is crucial in order to be able to log into the MongoDB.

4. Now enter the react-frontend folder and install the packages:
```
cd ../react-frontend
npm install
```

5. After that's done, we need to build:
```
npm run-script build
```

6. Now, enter the backend folder:
```
cd backend
```

7. From there, open two CMD (or terminals) and in each on run one of the following commands:
```
python main.py
python scheduled_scraper.py
```
<kbd>
<img src="https://i.imgur.com/sxxEgTP.png"></img>
</kbd>

Now we can enter localhost:5000 in our browser and enjoy.
Notice that running scheduled_scraper for the first time will install chromium on you machine (will take a minute or 2).

## Testing
There's a simple testing file you can run to see everything checks out.
Simply enter the backend folder, and run the test_espn_scraper.py file:
```
cd backend
python test_espn_scraper.py
```
<kbd>
<img src="https://i.ibb.co/djKB6hY/test-example.png"></img>
</kbd>

_If the test went well, you should see something like this._


