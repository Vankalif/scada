INSERT_IN = 'insert into {table} VALUES (%s, %s);'

FETCH_WELLS = 'SELECT well."name", well.id, deposit."name" FROM well ' \
              'LEFT JOIN deposit ON deposit.id = well.deposit_id;'

FETCH_LAST = 'with ' \
           't_1 as (select well_id, max("timestamp") as record_tstmp from temperature group by well_id)' \
           ',t_2 as (select well_id, max("timestamp") as record_tstmp from pressure group by well_id)' \
           ',t_3 as (select well_id, max("timestamp") as record_tstmp from "level" group by well_id)' \
           'select w.*, deposit."name", temperature.value as temperature, temperature."timestamp",' \
           'pressure.value as pressure, pressure."timestamp",' \
           '"level".value as "level", "level"."timestamp"' \
           'from  well as w ' \
           'left join deposit ON deposit.id = w.deposit_id ' \
           'left join temperature on temperature.well_id=w.id ' \
           'left join t_1 on t_1.well_id=temperature.well_id ' \
           'left join pressure on pressure.well_id=w.id ' \
           'left join t_2 on t_2.well_id=pressure.well_id ' \
           'left join "level" on "level".well_id=w.id ' \
           'left join t_3 on t_3.well_id="level".well_id ' \
           'where temperature."timestamp"=t_1.record_tstmp and pressure."timestamp"=t_2.record_tstmp and "level"."timestamp"=t_3.record_tstmp order by w.id;'

CHART_DATA = "select value, timestamp from {table} where {table}.timestamp >= %s and {table}.timestamp <= %s and well_id=%s order by timestamp asc;"

SERVER_ROOM_TEMP = "select sensor_data, timestamp from server_room_temp where" \
                   " server_room_temp.timestamp >= %s and" \
                   " server_room_temp.timestamp <= %s order by timestamp asc;"


INSERT_IN_SERVER_ROOM_TEMP = "insert into server_room_temp(sensor_data) VALUES (%s)"