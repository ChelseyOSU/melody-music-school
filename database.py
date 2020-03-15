import pymysql


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        db = "test"
        self.con = pymysql.connect(host=host, user=user, password=None, db=db, cursorclass=pymysql.cursors.DictCursor)

    def list_students(self):
        """
        Show all students in "students" MySQL table
        :return:
        """
        try:
            with self.con.cursor() as cursor:
                sql_query = "SELECT id, first_name, last_name, age FROM students"
                cursor.execute(sql_query)
                result = cursor.fetchall()
            self.con.commit()
        finally:
            self.con.close()
        return result

    def add_student(self, first_name, last_name, age):
        """
        Add student record to MySQL "students" table
        :param first_name:
        :param last_name:
        :param age:
        :return:
        """
        try:
            with self.con.cursor() as cursor:
                sql_query = "INSERT INTO students (first_name, last_name, age) VALUES (%s, %s, %s)"
                cursor.execute(sql_query, (first_name, last_name, age))
            self.con.commit()
        finally:
            self.con.close()

    def change_student(self, first_name, last_name, age, id):
        """
        Alter student record in MySQL "students" table
        :param first_name:
        :param last_name:
        :param age:
        :return:
        """
        try:
            with self.con.cursor() as cursor:
                sql_query = "UPDATE students SET first_name = %s, last_name = %s, age = %s WHERE id = %"
                cursor.execute(sql_query, (first_name, last_name, age))
            self.con.commit()
        finally:
            self.con.close()

    def list_classes(self):
        """
        Show all students in "students" MySQL table
        :return:
        """
        try:
            with self.con.cursor() as cursor:
                sql_query = "SELECT id, name FROM classes"
                cursor.execute(sql_query)
                result = cursor.fetchall()
            self.con.commit()
        finally:
            self.con.close()
        return result

