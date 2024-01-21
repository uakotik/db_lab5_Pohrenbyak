select * from manufacturer;
create table manufacturercopy as select * from manufacturer; 
delete from manufacturercopy;
select * from manufacturercopy;


DO $$
 Declare
 	manufacturer_id manufacturercopy.manufacturer_id%TYPE;
	manufacturer_name manufacturercopy.manufacturer_name%TYPE;
 BEGIN
 	manufacturer_id:= 'K';
	manufacturer_name:= 'Kelloggs';
	FOR counter IN 1..20
		LOOP
			INSERT INTO manufacturercopy(manufacturer_id,manufacturer_name)
			 VALUES (case when counter % 2 = 1 then 'K' else 'G'end,case when counter % 2 = 1 then 'Kelloggs' else 'General Mills'end );
			       END LOOP;
 END;
 $$