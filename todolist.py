from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    # deadline = Column(Date, default=datetime.strptime(datetime.today(), '%Y-%m-%d'))

    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


class ToDoList:

    def __init__(self, engines, session):
        self.engine = engines
        self.session = session

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_row(self, string_field, date_field):
        new_row = Table(task=string_field, deadline=date_field)
        self.session.add(new_row)
        self.session.commit()

    def query_table(self, Table):
        return self.session.query(Table).all()

    def days(self, day_number):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[day_number]

    def today_task(self, today, istoday):
        if today == datetime.today() and istoday:
            print('\nToday {} {}:'.format(today.day, today.strftime('%b')))
        else:
            print('\n{} {} {}:'.format(self.days(today.weekday()), today.day, today.strftime('%b')))
        rows = self.session.query(Table).filter(Table.deadline == today).all()
        if not rows:
            print("Nothing to do!\n")
        count = 1
        for row in rows:
            print(f'{count}) {row.task}')  # first_row = rows[0]
            count += 1

    def all_task(self):
        print('All tasks:')
        rows = self.query_table(Table)
        if not rows:
            print("Nothing to do!\n")
        count = 1
        for row in rows:
            print(
                f'{count}) {row.task} {row.deadline.day} {row.deadline.strftime("%b")}')  # first_row = rows[0]
            count += 1

    def missed_task(self):
        print('Missed tasks:')
        rows = self.query_table(Table)
        count = 1
        is_empty = True
        for row in rows:
            if row.deadline < datetime.today().date():
                is_empty = False
                print(
                    f'{count}) {row.task} {row.deadline.day} {row.deadline.strftime("%b")}')  # first_row = rows[0]
            count += 1
        if is_empty:
            print("Nothing is missed!")

    def delete_task(self):
        print("Chose the number of the task you want to delete:")
        rows = self.session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!\n")
        for row in rows:
            print(
                f'{row.id}) {row.task} {row.deadline.day} {row.deadline.strftime("%b")}')  # first_row = rows[0]
        to_delete = input()
        self.session.query(Table).filter(Table.id == int(to_delete)).delete()
        self.session.commit()
        print("The task has been deleted!")

    def main(self):
        self.create_table()
        while True:
            print()
            print("1) Today's tasks")
            print("2) Week's tasks")
            print("3) All tasks")
            print("4) Missed tasks")
            print("5) Add task")
            print("6) Delete task")
            print("0) Exit")

            command = input()

            if command == '1':
                today = datetime.today().date()
                self.today_task(today, True)

            elif command == '2':
                for i in range(7):
                    today = datetime.today().date() + timedelta(days=i)
                    self.today_task(today, False)

            elif command == '3':
                self.all_task()

            elif command == '4':
                self.missed_task()

            elif command == '5':
                print('\nEnter task')
                task = input()
                print('Enter deadline')
                user_deadline = input()
                deadline = datetime.strptime(user_deadline, '%Y-%m-%d')  # strp for string and strf for datetime
                self.add_row(task, deadline)
                print('The task has been added!')

            elif command == '6':
                self.delete_task()

            elif command == '0':
                break


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
to_do_list = ToDoList(engine, sessionmaker(bind=engine)())
to_do_list.main()
