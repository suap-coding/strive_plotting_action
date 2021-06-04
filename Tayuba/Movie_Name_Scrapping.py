from bs4 import BeautifulSoup
import requests
import pandas as pd



website = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
# website = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(website)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
name_of_movies = soup.find_all(name="h3")
data = []
for movies in name_of_movies:
    All_name = movies.getText()
    # All_name.replace(" ", "")

    print(All_name)

types_of_movies = soup.find_all(name="span", class_="genre")
# for type_of_movie in types_of_movies:
#     print(type_of_movie.getText())

# df = pd.DataFrame(data)
# print(df)
# csv_file = open("data.csv", mode="w+")
# csv_file.writelines(df)

# df_csv =df.to_csv("data.csv")