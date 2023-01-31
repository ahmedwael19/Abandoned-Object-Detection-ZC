import psycopg2
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(
    host="localhost",
    database="action_activity",
    user="postgres",
    password=" ")

cur = conn.cursor()


cur.execute("INSERT INTO full_outputs (uid , frame_id , cam_id , lab_id , object_id , action_type , class      , bb_left , bb_top , bb_width , bb_height, pred_conf , time_stamp) \
            VALUES                    (1   , 1        , 1      ,  32    , 24        , 'abandon'   , 'backpack' , 100     , 12     , 22       , 222      , 0.34      ,  '2015-01-11 00:51:14')");
conn.commit()
cur.close()
conn.close()
