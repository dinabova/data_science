.open reuters.db

select count(*)
from (
	select distinct term
	from frequency f
	where 
	(f.docid="10398_txt_earn" or f.docid="925_txt_trade") and (f.count=1)
);