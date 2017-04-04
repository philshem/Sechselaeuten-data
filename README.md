###OpenData for Zürich's Sechseläuten

Wikipedia: [en](https://en.wikipedia.org/wiki/Sechsel%C3%A4uten) | [de](https://de.wikipedia.org/wiki/Sechsel%C3%A4uten) | [fr](https://fr.wikipedia.org/wiki/Sechsel%C3%A4uten) 

[Zürich Tourism](https://www.zuerich.com/en/visit/sechselaeuten)

***

#### Böögg burning times - [boeoegg_burn_duration.csv](https://github.com/philshem/Sechselaeuten-data/blob/master/boeoegg_burn_duration.csv)

+ Böögg burn duration data from [Sechselaeuten.ch](http://www.sechselaeuten.ch/) 

- To add a new duration (in seconds) to the burn file, visit the [Statistik page](http://www.sechselaeuten.ch/sechselaeuten/statistik.asp) and find the newest year. Also available from [NZZ](https://www.nzz.ch/zuerich/sechselaeuten-animierte-grafik-bringen-sie-boeoegg-zur-explosion-ld.12809).

***

#### Zürich weather - [zuri_historical_weather.csv](https://github.com/philshem/Sechselaeuten-data/blob/master/zuri_historical_weather.csv)

+ Historical weather data for Zürich from [MeteoSchweiz](http://www.meteoswiss.admin.ch)
- To update historical weather file, run the Python 2.7 code [get_zuri_weather.py](https://github.com/philshem/Sechselaeuten/blob/master/get_zuri_weather.py), which downloads and parses [this text file](http://www.meteoswiss.admin.ch/product/output/climate-data/homogenous-monthly-data-processing/data/homog_mo_SMA.txt) and prints a CSV file.
