"""
    Given the names and grades for each student in a 
    class of N students, store them in a nested list 
    and print the name(s)  of any student(s) having the 
    second lowest grade.
    """
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])   # Store each student as [name, score]

    # Step 2: Find all scores in a list
    scores = []
    for record in records:
        scores.append(record[1])  # just collect scores

    # Step 3: Remove duplicates by converting to set, then back to list and sort
    unique_scores = list(set(scores))
    unique_scores.sort()

    # Step 4: The second lowest score is at index 1 (after sorting)
    second_lowest_score = unique_scores[1]

    # Step 5: Find all names with the second lowest score
    names_with_second_lowest = []
    for record in records:
        if record[1] == second_lowest_score:
            names_with_second_lowest.append(record[0])  # collect matching names

    # Step 6: Sort names alphabetically
    names_with_second_lowest.sort()

    # Step 7: Print each name
    for name in names_with_second_lowest:
        print(name)

