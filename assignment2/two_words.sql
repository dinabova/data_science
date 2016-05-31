/*
two words: 
Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. 
(Hint: Find the docs that contain one word and the docs that contain the other word separately, then find the intersection.)
*/


.open reuters.db

select count(*) 
from (
	select distinct f1.docid
	from frequency f1, frequency f2
	where 
	(f1.docid = f2.docid) and 
	((f1.term="transactions" and f2.term="world") or (f1.term="world" and f2.term="transactions"))
);