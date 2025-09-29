marks = [4, 12, 36, 98, 64, 25, 49, 81, 100, 16]
for index, mark in enumerate(marks):
    if mark >= 50:
        print(f"Student {index + 1} has passed with a mark of {mark}.")
    else:
        print(f"Student {index + 1} has failed with a mark of {mark}.")
