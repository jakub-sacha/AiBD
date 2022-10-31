import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int) and category > 0:
        return pd.read_sql("SELECT f.title, l.name AS languge , c.name AS category "
                           "FROM film f "
                           "JOIN language l USING(language_id) "
                           "JOIN film_category fc USING(film_id) "
                           "JOIN category c USING(category_id) "
                           f"WHERE c.category_id = {category} "
                           "ORDER BY f.title, l.name", con=connection)
    elif isinstance(category, str):
        return pd.read_sql("SELECT f.title, l.name AS languge , c.name AS category "
                           "FROM film f "
                           "JOIN language l USING(language_id) "
                           "JOIN film_category fc USING(film_id) "
                           "JOIN category c USING(category_id) "
                           f"WHERE c.name = '{category}' "
                           f"ORDER BY f.title, l.name", con=connection)
    else:
        return None
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int) and category > 0:
        return pd.read_sql("SELECT f.title, l.name AS languge , c.name AS category "
                           "FROM film f "
                           "JOIN language l USING(language_id) "
                           "JOIN film_category fc USING(film_id) "
                           "JOIN category c USING(category_id) "
                           f"WHERE c.category_id = {category} "
                           "ORDER BY f.title, l.name", con=connection)
    elif isinstance(category, str):
        return pd.read_sql("SELECT f.title, l.name AS languge , c.name AS category "
                           "FROM film f "
                           "JOIN language l USING(language_id) "
                           "JOIN film_category fc USING(film_id) "
                           "JOIN category c USING(category_id) "
                           f"WHERE c.name ~* '{category}' "
                           f"ORDER BY f.title, l.name", con=connection)
    else:
        return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(title, str):
        return None
    return pd.read_sql("SELECT a.first_name, a.last_name "
                       "FROM film f "
                       "JOIN film_actor fa USING(film_id) "
                       "JOIN actor a USING(actor_id) "
                       f"WHERE f.title = '{title}' "
                       f"ORDER BY a.last_name, a.first_name", con=connection)


def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(words, list) or any([not isinstance(word, str) for word in words]):
        return None

    where_statements = " OR ".join([f"f.title ~* '^{word} ' OR f.title ~* ' {word}$'" for word in words])

    return pd.read_sql("SELECT DISTINCT f.title "
                       "FROM film f "
                       "JOIN film_actor fa USING(film_id) "
                       "JOIN actor a USING(actor_id) "
                       f"WHERE {where_statements}", con=connection)


