import os


from config import config
from utils import create_database, get_youtube_data, save_data_to_database


def main():
    api_key = 'AIzaSyDKAGZhxHZfroBisPVbCpnHdcQNXnI7Ri0'
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        'UCwHL6WHUarjGfUM_586me8w',  # highload
    ]
    data = get_youtube_data(api_key, channel_ids)

    params = config()
    create_database('youtube', params)
    print(f"БД youtube успешно создана")

    save_data_to_database(data, 'youtube', params)
    #
    # conn = None
    #
    # params.update({'dbname': db_name})
    # try:
    #     with psycopg2.connect(**params) as conn:
    #         with conn.cursor() as cur:
    #             execute_sql_script(cur, script_file)
    #             print(f"БД {db_name} успешно заполнена")
    #
    #             create_suppliers_table(cur)
    #             print("Таблица suppliers успешно создана")
    #
    #             suppliers = get_suppliers_data(json_file)
    #             insert_suppliers_data(cur, suppliers)
    #             print("Данные в suppliers успешно добавлены")
    #
    #             add_foreign_keys(cur, json_file)
    #             print(f"FOREIGN KEY успешно добавлены")
    #
    # except(Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()


if __name__ == '__main__':
    main()
