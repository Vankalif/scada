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
           'where temperature."timestamp"=t_1.record_tstmp and pressure."timestamp"=t_2.record_tstmp and "level"."timestamp"=t_3.record_tstmp;'
