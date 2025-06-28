def calculate_fine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2 and d1 > d2:
            return 15 * (d1 - d2)
    return 0  # No fine if returned on or before due date


if __name__ == '__main__':
    d1, m1, y1 = map(int, input().strip().split())
    d2, m2, y2 = map(int, input().strip().split())
    print(calculate_fine(d1, m1, y1, d2, m2, y2))

"""
Explanation
Year Check (y1 > y2):
If the return year is later than the due year, the fine is 10,000 Hackos (regardless of months or days).
Same Year (y1 == y2):
Month Check (m1 > m2): If returned in a later month but the same year, the fine is 500 × (months late).
Same Month (m1 == m2):
Day Check (d1 > d2): If returned on a later day but the same month and year, the fine is 15 × (days late).
Otherwise, no fine (return 0).
Edge Cases:
If the return date is earlier than or equal to the due date, the fine is 0.
Sample Input    
9 6 2015   
6 6 2015 
calculation:
d1=9, m1=6, y1=2015
d2=6, m2=6, y2=2015
Sample Output
45
"""

