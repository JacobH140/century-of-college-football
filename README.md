# century-of-college-football
A network based on 100 years of Division I FBS American college football games (1924-2024), with evolving ground-truth community memberships captured in terms of conference realignment. The idea of benchmarking (static) community detection using college football comes from [1]. 

# How to Use
Head over to [this Colab notebook](https://colab.research.google.com/drive/1V8QjLjaZGW33G-bqT1MNQ_VvXWd3E5sf?usp=sharing)
 and make a copy. There, the data may be filtered according to start/end year, snapshot aggregation length, etc. The notebook will output a tailored dataset accordingly, together with network statistics, a time-varying adjacency matrix, and a readme. The notebook should also make it clear how to custom-filter the data if desired. 

Alternatively, the raw data queried by the Colab notebook may be found in the file `all_cfb_games_1924_2024.csv`. The script that was used to generate the raw data via the [collegefootballdata.com](https://collegefootballdata.com/) API is `main_csv_generation.py`.  

# Warnings
- Data from 2020 is inconsisent due to Covid-19. 
- Likewise for 1939-1945 due to WWII. Indeed, expect to exercise general care when handling data pre-1970.


# Citing
```
@inproceedings{humeSpectral2024,
  author    = {Hume, Jacob and Balzano, Laura},
  title     = {A Spectral Framework for Tracking Communities in Evolving Networks},
  booktitle = {Proceedings of the Third Learning on Graphs Conference},
  year      = {2024},
  organization = {PLMR},
}
```

# References
[1] Michelle Girvan and Mark EJ Newman. Community structure in social and biological networks.
Proceedings of the national academy of sciences, 99(12):7821–7826, 2002.
