SELECT CONVERT( DECIMAL(13, 4), 10 + (30-10)*RAND(CHECKSUM(NEWID()));CREATE TABLE public.pressure
(
    well_id integer,
    value double precision,
    "timestamp" timestamp with time zone DEFAULT current_timestamp,
    CONSTRAINT well_id FOREIGN KEY (well_id)
        REFERENCES public.well (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);