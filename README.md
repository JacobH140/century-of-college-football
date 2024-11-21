# century-of-college-football
A temporal network based on 100 years of Division I FBS American college football games (1924-2024), with evolving ground-truth community memberships captured in terms of conference realignment. 

# How to Use
Head over to this Colab notebook (LINK). There, the data may be filtered according to the following parameters:
- time range (in years)
- years to exclude
- ....

The script should also make it clear how to custom-filter the data if desired. 


Alternatively, the raw data queried by the Colab notebook may be found in the file `all_cfb_games_1924_2024.csv`. The script to generate the raw data is `main_csv_generation.py`. 

# Warnings
- Data from 2020 is inconsisent due to Covid-19. 
- Likewise for 1939-1945. In fact, the entire dataset pre-1970 looks like 2020 in places — expect to exercise extra care if using it. 
