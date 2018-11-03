# _*_ coding: utf8 _*_

import requests
import csv


# offset for url
offset = [x * 50 for x in range(0, 2)]
movie_list = []

# get json data
for num in offset:
    hot_movies_url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=豆瓣高分&page_limit=50&page_start={num}'
    hot_movies_info = requests.get(hot_movies_url).json()
    for item in hot_movies_info['subjects']:
        movie_name = item['title']
        movie_rate = item['rate']
        movie_link = item['url']
        movie_list.append([movie_name, movie_rate, movie_link])

# sorted per rate
sort_movie_list = sorted(movie_list, key=lambda r: r[1], reverse=True)
print(sort_movie_list)

# save to csv file
with open('douban_hot_movies.csv', 'a', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(["名称", "评分", "链接"])
    writer.writerows(sort_movie_list)
