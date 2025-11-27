import csv
import random

INPUT_PATH = 'north-pole-capture.csv'


def shuffle_csv(path: str) -> None:
    # Read all rows
    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return

    header, data = rows[0], rows[1:]

    # Shuffle data rows in place
    random.shuffle(data)

    # Write back
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


if __name__ == '__main__':
    shuffle_csv(INPUT_PATH)
    print('Shuffled myfile.csv')
