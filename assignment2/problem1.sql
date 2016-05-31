.open reuters.db

select count(*)
from (
	select *
	from frequency f
	where
	f.docid="10398_txt_earn"
);


select term
from frequency f
where 
f.docid="10398_txt_earn" and count=1;

