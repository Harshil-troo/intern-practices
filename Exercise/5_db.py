import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta
def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='harshil',
                                         user='root',
                                         password='1234')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def update_doctor_experience(Doctor_id):
    # Update Doctor Experience in Years
    try:
        # Get joining date
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select Joining_Date from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (Doctor_id,))
        joining_date = cursor.fetchone()

        # calculate Experience in years
        joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date = datetime.datetime.now()
        Experience = relativedelta(today_date, joining_date_1).years

        # Update doctor's Experience now
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
        cursor.execute(sql_select_query, (Experience, Doctor_id))
        connection.commit()
        records = cursor.fetchall()
        print("Doctor Id:", Doctor_id, " Experience updated to ", Experience, " years")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", Experience, "\n")

        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 5: Calculate and Update experience of all doctors  \n")
update_doctor_experience(101)