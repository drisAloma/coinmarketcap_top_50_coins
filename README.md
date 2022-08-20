## A webscrapper built with python and splash framework to retrieve top 50 coins by market capitalization on coinmarketcap website.

### Steps to launch app
Execute the following in windows CMD.</br>
N.B --> Docker version >= 17 must be installed

Step 1: Pull the splash image fron docker
- sudo docker pull scrapinghub/splash

Step 2: Set up container
- sudo docker run -it -p 8050:8050 --rm scrapinghub/splash --m-timeout=3600
The should print some lines of code and end with something like this "Server listening on https://0.0.0.0:8050".
Open your web browser and type in "https://localhost:8050"

After the above steps, run the following on python IDE in your local machine:

- git clone https://github.com/drisAloma/top_50_coins_scrapper
- cd top_50_coins_scrapper
- docker build -t top-50-coins
- docker run top-50-coins
