# Write your MySQL query statement below
with cte1 as(
    select *, row_number() over(partition by email) rn
    from Person
)
select distinct email Email
from cte1
where rn>1;