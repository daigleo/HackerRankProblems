def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2 < y1:
        fine = 10000
    elif y2 == y1 and m2 < m1:
        fine = 500 * (m1 - m2)
    elif y2 == y1 and m2 == m1 and d2 < d1:
        fine = 15 * (d1 - d2)
    else:
        fine = 0
    
    return fine
    

    


if __name__ == '__main__':
    day_returned, month_returned, year_returned = 9, 6, 2015
    day_due, month_due, year_due = 6, 6, 2015
fine = libraryFine(day_returned, month_returned, year_returned,
            day_due, month_due, year_due)


print(fine)