# https://leetcode.com/problems/employee-importance/submissions/
# 690. Employee Importance
#
# You are given a data structure of employee information, which includes the employee's unique id,
# their importance value and their direct subordinates' id.
#
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
# They have importance value 15, 10 and 5, respectively.
# Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]],
# and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1,
# the relationship is not direct.
#
# Now given the employee information of a company, and an employee id, you need to return the total
# importance value of this employee and all their subordinates.

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importanceValue = 0
        employeeTracker = {}
        queue = [id]

        for emp in employees:
            employeeTracker[emp.id] = emp #[1, 5, [2, 3]] -> 1: [1, 5, [2, 3]]

        while len(queue):
            queueId = queue.pop(0)
            importanceValue += employeeTracker[queueId].importance # [1, 5, [2, 3]]
            queue.extend(employeeTracker[queueId].subordinates)

        return importanceValue
