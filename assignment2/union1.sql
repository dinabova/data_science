.open reuters.db

select count(*)
from (
	select term
	from frequency f
	where 
	f.docid="10398_txt_earn" and f.count=1
	
	union
	
	select term
	from frequency f
	where 
	f.docid="925_txt_trade" and f.count=1
);