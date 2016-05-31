/*
You can also use this similarity metric to implement some primitive search capabilities. 
Consider a keyword query that you might type into Google: It's a bag of words, just like a document (typically a keyword query will have far fewer terms than a document, but that's ok).

So if we can compute the similarity of two documents, we can compute the similarity of a query with a document. 
You can imagine taking the union of the keywords represented as a small set of (docid, term, count) tuples with the set of all documents in the corpus, 
then recomputing the similarity matrix and returning the top 10 highest scoring documents.

(i) keyword search: Find the best matching document to the keyword query "washington taxes treasury". 
You can add this set of keywords to the document corpus with a union of scalar queries:
Then, compute the similarity matrix again, but filter for only similarities involving the "query document": docid = 'q'.
Consider creating a view of this new corpus to simplify things.

What to turn in: Create a file part_i.txt containing the maximum similarity score between the keyword query among all documents. 
Your SQL query should return a list of (docid, similarity) pairs, but you will submit only include a single number: the highest similarity score in the list.
*/

.open reuters.db


drop view frequency_and_query;
create view frequency_and_query as 
	SELECT * FROM frequency
	UNION
	SELECT 'q' as docid, 'washington' as term, 1 as count 
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count;
		
	

select highest_similarity
from (
	select query_similarity_mat.ddocid, query_similarity_mat.dtdocid, max(query_similarity_mat.similarity) as highest_similarity
	from (

		select d.docid as ddocid, dt.docid as dtdocid, sum(d.count * dt.count) as similarity
		from frequency_and_query d, frequency_and_query dt
		where d.term = dt.term and d.docid = 'q' and dt.docid <> 'q' 
		group by d.docid, dt.docid
	) query_similarity_mat
	group by query_similarity_mat.ddocid
);

