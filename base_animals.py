import sqlite3


def run_sql(sql):
    with sqlite3.connect("animal.db") as con:
        cur = con.cursor()
        results = cur.execute(sql).fetchall()
        cur.close()
    return results


def base_animal(itemid):
    """По запросу itemid функция возвращает информацию об одном объекте"""

    sql = f"SELECT age_upon_outcome, animal_id, type_animals.name_type, name, breed_animals.name_breed, date_of_birth " \
          f"FROM animals_final " \
          f"LEFT JOIN breed_animals on animals_final.breed_id = breed_animals.Id " \
          f"LEFT JOIN type_animals on animals_final.type_id = type_animals.Id " \
          f"WHERE animals_final.id = {itemid}"
    results = run_sql(sql)
    animal_dic = {
        "age_upon_outcome": results[0][0], "animal_id": results[0][1], "type_animals": results[0][2],
        "name_animal": results[0][3], "breed": results[0][4], "date_of_birth": results[0][5]
    }
    return animal_dic


def sql():
    sql_1 = '''CREATE TABLE type_animals(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_type VARCHAR(20)
        )'''
    sql_2 = '''INSERT INTO type_animals(name_type) SELECT DISTINCT animal_type FROM animals'''

    sql_3 = '''CREATE TABLE breed_animals(
         Id INTEGER PRIMARY KEY AUTOINCREMENT,
         name_breed VARCHAR(20)
         )'''
    sql_4 = '''INSERT INTO breed_animals(name_breed) SELECT DISTINCT breed FROM animals'''

    sql_5 = '''CREATE TABLE color(
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
              name_color VARCHAR(10)
            )'''
    sql_6 = '''INSERT INTO color(name_color) SELECT color1 FROM animals'''

    sql_7 = '''CREATE TABLE animal_color(
                animal_id INTEGER,
                color_id INTEGER)'''
    sql_8 = '''INSERT INTO animal_color SELECT animals."index", color.Id FROM animals
        JOIN color on color1 = color.name_color'''
    sql_9 = '''INSERT INTO animal_color SELECT animals."index", color.Id FROM animals
            JOIN color on color2 = color.name_color'''

    sql_10 = '''CREATE TABLE outcome(
             outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
             outcome_subtype VARCHAR(10),
             outcome_type VARCHAR(10),
             outcome_month INTEGER,
             outcome_year INTEGER)'''
    sql_11 = '''INSERT INTO outcome(outcome_subtype, outcome_type, outcome_month, outcome_year) 
       SELECT outcome_subtype, outcome_type,outcome_month, outcome_year FROM animals group by outcome_subtype, 
       outcome_type, outcome_month, outcome_year'''

    sql_12 = '''CREATE TABLE animals_final (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              age_upon_outcome VARCHAR(20),
              animal_id INTEGER,
              type_id INTEGER,
              name varchar(50),
              breed_id varchar(50),
              date_of_birth DATE,
              outcome_id)'''
    sql_13 = '''INSERT INTO animals_final SELECT
              "index",
              age_upon_outcome,
              animal_id,
              type_animals.Id,
              animals.name,
              breed_animals.id,
              date_of_birth,
              outcome.outcome_id
              FROM animals LEFT JOIN type_animals on animals.animal_type = type_animals.name_type
              LEFT JOIN breed_animals on animals.breed = breed_animals.name_breed
              LEFT JOIN outcome on animals.outcome_subtype = outcome.outcome_subtype
              AND animals.outcome_type = outcome.outcome_type
              AND animals.outcome_month = outcome.outcome_month
              AND animals.outcome_year = outcome.outcome_year
              '''