.open reuters.db

select count(*)
from ( 
	select *
	from frequency f
	where 
	f.docid="10398_txt_earn"
);