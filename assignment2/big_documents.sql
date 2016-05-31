/* big documents 
Write a SQL statement to find all documents that have more than 300 different terms.
*/


.open reuters.db

select count(*) 
from (
	select docid
	from frequency
	group by docid
	having 
	count(term) > 300
);


/*
Write a SQL statement to find all documents that have more than 300 total terms.
(Hint: You can use the HAVING clause, or you can use a nested query.
Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)

select count(*) 
from (
	select docid
	from frequency
	group by docid
	having 
	sum(count) > 300
);
*/

