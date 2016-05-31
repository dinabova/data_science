/* sparse matrix multiplication
*/

.open matrix.db


select a.row_num as r, b.col_num as c, sum(a.value * b.value) as s
from a, b
where a.col_num = b.row_num 	
group by a.row_num, b.col_num;



