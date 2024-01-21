import psycopg2
import matplotlib.pyplot as plt

username = 'student01'
password = '1'
database = 'lab5'
host = 'localhost'
port = '5432'

query_1 = '''
select m.manufacturer_name,c.sugar
from cereal c
join manufacturer m on m.manufacturer_id=c.manufacturer_id
'''
query_2 = '''select c.name,c.protein
from cereal c
'''

query_3 = '''select r.rating_score,c.sugar 
from rating r 
join cereal c on r.cereal_id=c.cereal_id
join manufacturer m on m.manufacturer_id=c.manufacturer_id
order by rating_score
'''

view_1 = ''' create or replace view NameSugar as
    select m.manufacturer_name,c.sugar
    from cereal c
    join manufacturer m on m.manufacturer_id=c.manufacturer_id
'''
view_2 = ''' create or replace view NameProtein as
    select c.name,c.protein
    from cereal c
'''
view_3= ''' create or replace view RateSugar as
    select r.rating_score,c.sugar 
    from rating r 
    join cereal c on r.cereal_id=c.cereal_id
    join manufacturer m on m.manufacturer_id=c.manufacturer_id
    order by rating_score
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    cur = conn.cursor()

    cur.execute(view_1)
    cur.execute(view_2)
    cur.execute(view_3)

    cur.execute(query_1)
    manufacturer = []
    calories = []

    for row in cur:
        manufacturer.append(row[0])
        calories.append(row[1])
    
    x_range = range(len(manufacturer))
    
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    
    bar_ax.bar(x_range, calories, label='calories')
    bar_ax.set_title('Вміст цукру у сніданках кожгого виробника')
    bar_ax.set_xlabel('Виробники')
    bar_ax.set_ylabel('Цукор')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(manufacturer)

    cur.execute(query_2)
    name = []
    protein = []


    for row in cur:
        name.append(row[0])
        protein.append(row[1])


    pie_ax.pie(protein, labels=name, autopct='%1.1f%%')
    pie_ax.set_title('Частка протеїну у кожному сніданках')


    cur.execute(query_3)
    rating = []
    sugar = []
    
    
    for row in cur:
        rating.append(row[0])
        sugar.append(row[1])

    graph_ax.plot(rating, sugar, marker='o')
    graph_ax.set_xlabel('Рейтинг')
    graph_ax.set_ylabel('Кількість цукру')
    graph_ax.set_title('Графік залежності рейтингу від кількості цукру')

    for qnt, price in zip(rating, sugar):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')  

    mng = plt.get_current_fig_manager()
    mng.resize(1400, 600)
    plt.show()