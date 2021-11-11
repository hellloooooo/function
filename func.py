# 1
def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
random_list_of_nums = [166,4,24,52,345,64,75,33, 26, 61, 887, 4]  
bubble_sort(random_list_of_nums)  
print(random_list_of_nums)
# 2
class Student:
        def __init__(character):
            a=1
            b=2
            c=3
        def __repr__(self):
            return repr((self.a, self.b, self.c))
        def weighted_grade(self):
            return 'CBA'.index(self.grade) / self.age

>>> student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
>>> sorted(student_objects, key=lambda student: student.age)   # сортируем по возрасту
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
