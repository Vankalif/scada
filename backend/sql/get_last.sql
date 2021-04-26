
select * from "level" order by "timestamp" desc limit 1;


select well.name, "value", "timestamp" from temperature
	join well ON temperature.well_id = well.id ORDER by temperature."timestamp" DESC limit 1;

select well.name, "value", "timestamp" from "level" left join well ON "level".well_id = well.id where well.id = 2 ORDER by "level"."timestamp" DESC limit 1;