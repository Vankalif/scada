FETCH_LAST = 'select well.name, "value", "timestamp" from {table} ' \
                 'left join well ON {table}.well_id = well.id ' \
                 'where well.id = %s ORDER by {table}."timestamp" DESC limit 1;'

INSERT_IN = 'insert into {table} VALUES (%s, %s);'

FETCH_WELLS = 'select * from well'
