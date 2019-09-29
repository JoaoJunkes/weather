from Data import connectdb

cur = connectdb.getCursor()
con = connectdb.getConnection()

def save(temp_max,temp_min,date_forecast,date_query,weather,id_city):
    sql = str("insert into history_weather (temp_max,temp_min,date_forecast,date_query,weather,id_city) " +
              " values (%s,%s,%s,%s,%s,%s)")
    cur.execute(sql, [temp_max,
                      temp_min,
                      date_forecast,
                      date_query,
                      weather,
                      id_city])
    con.commit()

def select():
    cur.execute('select * from history_weather')
    recset = cur.fetchall()
    for rec in recset:
        print(rec)