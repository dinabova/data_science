.open reuters.db

select count(*)
from (
	select term
	from frequency f
	where 
	f.docid="10398_txt_earn" and f.count=1
);