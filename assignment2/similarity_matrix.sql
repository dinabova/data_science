/*
The reuters dataset can be considered a term-document matrix, which is an important representation for text analytics.
frequency(docid, term, count) ~ matrix(row_num, col_num, value)
Each row of the matrix is a document vector, with one column for every term in the entire corpus. (docid is like matrix.row_num, term is like matrix.col_num and count is like matrix.value)
Naturally, some documents may not contain a given term, so this matrix is rather sparse. 
The value in each cell of the matrix is the term frequency. (You'd often want this this value to be a weighted term frequency, 
typically using "tf-idf": term frequency - inverse document frequency. But we'll stick with the raw frequency for now.)

What can you do with the term-document matrix D? One thing you can do is compute the similarity of documents. 
Just multiply the matrix with its own transpose S = D*transpose(D), and you have an (unnormalized) measure of similarity.
transpose(D) = dt(term, docid, count) 
The result is a square document-document matrix, where each cell represents the similarity.
Here, similarity is pretty simple: if two documents both contain a term, then the score goes up by the product of the two term frequencies. 
This score is equivalent to the dot product of the two document vectors.

To normalize this score to the range 0-1 and to account for relative term frequencies, the cosine similarity is perhaps more useful. 
The cosine similarity is a measure of the angle between the two document vectors, normalized by magnitude. You just divide the dot product by the magnitude of the two vectors. 
However, we would need a power function (x^2, x^(1/2)) to compute the magnitude, and sqlite has built-in support for only very basic mathematical functions. 
It is not hard to extend sqlite to add functions that you need, but we won't be doing that in this assignment.

(h) similarity matrix: Write a query to compute the similarity matrix D*transpose(D). 
(Hint: The transpose is trivial -- just join on columns to columns instead of columns to rows.) 
The query could take some time to run if you compute the entire result. 
But notice that you don't need to compute the similarity of both (doc1, doc2) and (doc2, doc1) -- they are the same, since similarity is symmetric. 
If you wish, you can avoid this wasted work by adding a condition of the form a.docid < b.docid to your query. 

What to turn in: Create a file part_h.txt containing the similarity value of the two documents '10080_txt_crude' and '17035_txt_earn'. Upload this file as your answer.

matrix_multiply.sql
select a.row_num, b.col_num, sum(a.value * b.value)
from a, b
where a.col_num = b.row_num 	
group by a.row_num, b.col_num;

*/

.open reuters.db

select similarity_mat.similarity
from (

	select d.docid as ddocid, dt.docid as dtdocid, sum(d.count * dt.count) as similarity
	from frequency d, frequency dt
	where d.term = dt.term and d.docid < dt.docid /*and d.docid = "10080_txt_crude" and dt.docid = "17035_txt_earn" */
	group by d.docid, dt.docid
) similarity_mat
where 
similarity_mat.ddocid = "10080_txt_crude" and similarity_mat.dtdocid = "17035_txt_earn";

