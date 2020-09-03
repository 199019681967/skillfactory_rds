#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[3]:


import pandas as pd
data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[4]:


data.describe()


# # Предобработка

# In[3]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[4]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '5. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"


# In[ ]:


data[data.budget == data.budget.max()]


# ВАРИАНТ 2

# In[ ]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[7]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '2. Gods and Generals (tt0279111)'


# In[ ]:


data[data.runtime == data.runtime.max()]


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[ ]:


data[data.runtime == data.runtime.min()]


# In[8]:


answers['3'] = '3. Winnie the Pooh (tt1449283)'


# # 4. Какова средняя длительность фильмов?
# 

# In[ ]:


data.runtime.mean()


# In[34]:


answers['4'] = '2. 110'


# # 5. Каково медианное значение длительности фильмов? 

# In[ ]:


data.runtime.median()


# In[10]:


answers['5'] = "1. 107"


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[6]:


# лучше код получения столбца profit вынести в Предобработку что в начале

data["profit"] = data.revenue - data.budget
data[data.profit == data.profit.max()]


# In[11]:


answers['6'] = "5. Avatar (tt0499549)"


# # 7. Какой фильм самый убыточный? 

# In[ ]:


data[data.profit == data.profit.min()]


# In[12]:


answers['7'] = "5. The Lone Ranger (tt1210819)"


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[ ]:


data[data.revenue > data.budget].count()


# In[13]:


answers['8'] = "1. 1478"


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[ ]:


year_2008 = data[data.release_year == 2008]
year_2008[year_2008.revenue == year_2008.revenue.max()]


# In[14]:


answers['9'] = "4. The Dark Knight (tt0468569)"


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[ ]:


q_10 = data[(data.release_year > 2011) & (data.release_year < 2015)]
q_10[q_10.profit == q_10.profit.min()]


# In[15]:


answers['10'] = "5. The Lone Ranger (tt1210819)"


# # 11. Какого жанра фильмов больше всего?

# In[ ]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале

data.genres.value_counts()

action = data[data.genres.str.contains("Action")]["original_title"].count()
adventure = data[data.genres.str.contains("Adventure")]["original_title"].count()
drama = data[data.genres.str.contains("Drama")]["original_title"].count()
comedy = data[data.genres.str.contains("Comedy")]["original_title"].count()
thriller = data[data.genres.str.contains("Thriller")]["original_title"].count()

action, adventure, drama, comedy, thriller


# In[16]:


answers['11'] = "3. Drama"


# ВАРИАНТ 2

# In[ ]:





# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[ ]:


profitable = data[data.profit > 0]
p_drama = profitable[profitable.genres.str.contains("Drama")]["original_title"].count()
p_comedy = profitable[profitable.genres.str.contains("Comedy")]["original_title"].count()
p_action = profitable[profitable.genres.str.contains("Action")]["original_title"].count()
p_thriller = profitable[profitable.genres.str.contains("Thriller")]["original_title"].count()
p_adventure = profitable[profitable.genres.str.contains("Adventure")]["original_title"].count()

p_drama, p_comedy, p_action, p_thriller, p_adventure


# In[17]:


answers['12'] = "1. Drama"


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[ ]:


data.groupby(["director"])["revenue"].sum().sort_values(ascending = False)


# In[18]:


answers['13'] = "5. Peter Jackson"


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[ ]:


q_14 = data[data.genres.str.contains("Action", na = False)]

director_1 = q_14[q_14.director == "Ridley Scott"]["original_title"].count()
director_2 = q_14[q_14.director == "Guy Ritchie"]["original_title"].count()
director_3 = q_14[q_14.director == "Robert Rodriguez"]["original_title"].count()
director_4 = q_14[q_14.director == "Quentin Tarantino"]["original_title"].count()
director_5 = q_14[q_14.director == "Tony Scott"]["original_title"].count()

director_1, director_2, director_3, director_4, director_5


# In[19]:


answers['14'] = "1. Ridley Scott"


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[ ]:


year_2012 = data[data.release_year == 2012]
year_2012.groupby(["cast"])["revenue"].sum().sort_values(ascending = False)


# In[20]:


answers['15'] = "3. Chris Hemsworth"


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[ ]:


high_budget = data[data.budget > data.budget.mean()]
a = high_budget[high_budget.cast.str.contains("Tom Cruise")]["original_title"].count()
b = high_budget[high_budget.cast.str.contains("Mark Wahlberg")]["original_title"].count()
c = high_budget[high_budget.cast.str.contains("Matt Damon")]["original_title"].count()
d = high_budget[high_budget.cast.str.contains("Angelina Jolie")]["original_title"].count()
e = high_budget[high_budget.cast.str.contains("Adam Sandler")]["original_title"].count()

display(a, b, c, d, e)


# In[21]:


answers['16'] = "3. Matt Damon"


# In[ ]:





# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[ ]:


nick = data[data.cast.str.contains("Nicolas Cage")]
g1 = nick[nick.genres.str.contains("Drama")]["original_title"].count()
g2 = nick[nick.genres.str.contains("Action")]["original_title"].count()
g3 = nick[nick.genres.str.contains("Thriller")]["original_title"].count()
g4 = nick[nick.genres.str.contains("Adventure")]["original_title"].count()
g5 = nick[nick.genres.str.contains("Crime")]["original_title"].count()

g1, g2, g3, g4, g5


# In[22]:


answers['17'] = "2. Action"


# # 18. Самый убыточный фильм от Paramount Pictures

# In[ ]:


paramount = data[data.production_companies.str.contains("Paramount Pictures")]
paramount[paramount.profit == paramount.profit.min()]


# In[23]:


answers['18'] = "1. K-19: The Widowmaker (tt0267626)"


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[ ]:


r_2014 = data[data.release_year == 2014]["revenue"].sum()
r_2008 = data[data.release_year == 2008]["revenue"].sum()
r_2012 = data[data.release_year == 2012]["revenue"].sum()
r_2002 = data[data.release_year == 2002]["revenue"].sum()
r_2015 = data[data.release_year == 2015]["revenue"].sum()

display(r_2014, r_2008, r_2012, r_2002, r_2015)


# In[24]:


answers['19'] = "5. 2015"


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[ ]:


Warner_Bros = data[data.production_companies.str.contains("Warner Bros")]
Warner_Bros.groupby(["release_year"])["profit"].sum().sort_values(ascending = False)


# In[25]:


answers['20'] = "1. 2014"


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[ ]:


data['release_date'] = pd.to_datetime(data['release_date'])
data.release_date.dt.month.value_counts().sort_values(ascending = False)


# In[36]:


answers['21'] = "4. Сентябрь"


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[ ]:


a = data.release_date.dt.month.value_counts()
a[6] + a[7] + a[8]


# In[26]:


answers['22'] = "2. 450"


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[ ]:


data['release_date'] = pd.to_datetime(data['release_date'])

d_1 = data[data.director == "Steven Soderbergh"]
d_1_performance = d_1.release_date.dt.month.value_counts().sort_values(ascending = False)
d_1_performance[12] + d_1_performance[1] + d_1_performance[2]

d_2 = data[data.director == "Christopher Nolan"]
d_2_performance = d_2.release_date.dt.month.value_counts().sort_values(ascending = False)

d_3 = data[data.director == "Clint Eastwood"]
d_3_performance = d_3.release_date.dt.month.value_counts().sort_values(ascending = False)
d_3_performance

d_4 = data[data.director == "Ridley Scott"]
d_4.release_date.dt.month.value_counts().sort_values(ascending = False)

d_5 = data[data.director == "Ridley Scott"]
d_5.release_date.dt.month.value_counts().sort_values(ascending = False)


# In[27]:


answers['23'] = "3. Clint Eastwood"


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[ ]:


q_24_1 = data[data.production_companies.str.contains("Universal")]
len(q_24_1.original_title.max())

q_24_2 = data[data.production_companies.str.contains("Warner Bros")]
len(q_24_2.original_title.max())

q_24_3 = data[data.production_companies.str.contains("Jim Henson Company")]
len(q_24_3.original_title.max())

q_24_4 = data[data.production_companies.str.contains("Paramount Pictures")]
len(q_24_4.original_title.max())

q_24_5 = data[data.production_companies.str.contains("Four By Two Productions")]
len(q_24_5.original_title.max())


# In[28]:


answers['24'] = "5. Four By Two Productions"


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:


data["overview_length"] = data.overview.map(lambda x: len(x))

len_1 = data[data.production_companies.str.contains ("Universal Pictures")]["overview_length"].mean()
len_2 = data[data.production_companies.str.contains ("Warner Bros")]["overview_length"].mean()
len_3 = data[data.production_companies.str.contains ("Midnight Picture Show")]["overview_length"].mean()
len_4 = data[data.production_companies.str.contains ("Paramount Pictures")]["overview_length"].mean()
len_5 = data[data.production_companies.str.contains ("Total Entertainment")]["overview_length"].mean()

len_1, len_2, len_3, len_4, len_5


# In[29]:


answers['25'] = "3. Midnight Picture Show"


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[ ]:


data.groupby(["original_title"])["vote_average"].max().sort_values(ascending = False)


# In[30]:


answers['26'] = "1. Inside Out, The Dark Knight, 12 Years a Slave"


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# ВАРИАНТ 2

# In[ ]:


option_1 = data[(data.cast.str.contains("Johnny Depp")) & (data.cast.str.contains("Helena Bonham Carter"))].count()
option_2 = data[(data.cast.str.contains("Ben Stiller")) & (data.cast.str.contains("Owen Wilson"))].count()
option_3 = data[(data.cast.str.contains("Vin Diesel")) & (data.cast.str.contains("Paul Walker"))].count()
option_4 = data[(data.cast.str.contains("Adam Sandler")) & (data.cast.str.contains("Kevin James"))].count()
option_5 = data[(data.cast.str.contains("Daniel Radcliffe")) & (data.cast.str.contains("Rupert Grint"))].count()

option_1, option_2, option_3, option_4, option_5


# In[31]:


answers['27'] = "5. Daniel Radcliffe & Rupert Grint"


# # Submission

# In[37]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[38]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




