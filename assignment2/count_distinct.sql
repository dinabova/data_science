/*
Write a SQL statement to count the number of unique documents containing the word "law" or containing the word "legal" 
(If a document contains both law and legal, it should only be counted once
*/
.open reuters.db

select count(*)
from (
	select distinct docid
	from frequency f
	where 
	f.term="law" or f.term="legal"
);