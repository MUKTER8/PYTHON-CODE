if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    print(f"{avg:.2f}")

    """The first line contains the integer n, the number of students' records. 
    The next n lines contain the names and marks obtained by a student, each value separated by a space.
    The final line contains query_name, the name of a student to query.
    Sample Input 0
3
K 67 68 69
A 70 98 63
M 52 56 60
M
Sample Output 0
56.00
    """
