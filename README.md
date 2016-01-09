# Sechselaeuten
OpenData for Zürich's Sechseläuten - Böögg burning time and historical weather

----
+ Böögg burn duration data from [Sechselaeuten.ch](http://www.sechselaeuten.ch/)
- To add a new duration (in seconds) to the burn file, visit the [Statistik page](http://www.sechselaeuten.ch/sechselaeuten/statistik.asp) and find the newest year.

----

+ Historical weather data for Zürich from [MeteoSchweiz](http://www.meteoswiss.admin.ch)
- To update historical weather file, run the Python 2.7 code [get_zuri_weather.py](https://github.com/philshem/Sechselaeuten/blob/master/get_zuri_weather.py), which downloads and parses [this text file](http://www.meteoswiss.admin.ch/product/output/climate-data/homogenous-monthly-data-processing/data/homog_mo_SMA.txt) and prints a CSV file.
