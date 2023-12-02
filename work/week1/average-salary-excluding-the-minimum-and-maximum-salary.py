class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        count = len(salary)-2
        salary_sum = sum(salary)-(min_salary+max_salary)
        # # count = 0
        # for i in salary:
        #     if i != min_salary or max_salary:
        #         sum = sum + i
        #         # count += 1
        return salary_sum/count
