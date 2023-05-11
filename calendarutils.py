from datetime import datetime


def is_valid_entry_data(summary, description, start_date, end_date):
    if not all([summary, description, start_date, end_date]):
    #lo mismo que: not summary or not description or not start_date or not end_date:
        return False
    elif not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        return False
    elif start_date > end_date:
        return False
    elif start_date < datetime.now():
        return False
    else: return True


def generate_text(summary, description, start_date = datetime(1999,1,31,3,20,6), end_date = datetime(1999,1,31,3,20,6)):
    if not is_valid_entry_data(summary, description, start_date, end_date):
        return -1
    else:
        event_text = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
SUMMARY:{summary}
DTSTART;VALUE=DATE:{datetime.strftime(start_date, '%Y%m%d')}T{datetime.strftime(start_date, '%H%M%S')}
DTEND;VALUE=DATE:{datetime.strftime(end_date, '%Y%m%d')}T{datetime.strftime(end_date, '%H%M%S')}
DESCRIPTION:{description}
END:VEVENT
END:VCALENDAR"""
        return event_text

if __name__ == "__main__":
    print(datetime.now())
    assert generate_text("summary", "description", datetime(2023,2,18,13,30,00), datetime(2023,2,18,14,30,00)) == -1