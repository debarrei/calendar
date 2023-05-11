import calendarutils
from datetime import datetime

def main():
    event = calendarutils.generate_text("summary", "description", datetime(2023,6,18,13,30,00), datetime(2023,6,18,14,30,00))
    print(event)


if __name__ == '__main__':
    main()