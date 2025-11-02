CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT max(salary)
    from Employee e
    Where (N-1)=(select count(distinct salary) from Employee ep where ep.salary > e.salary)
  );
END