def add(matrix1, matrix2):
    combined = []
    for rows in zip(matrix1, matrix2):
        row = []
        for items in zip(rows[0], rows[1]):
            row.append(items[0] + items[1])
        combined.append(row)
    return combined

