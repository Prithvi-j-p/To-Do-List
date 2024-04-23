from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
import random
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect


def one(request):

    return render(request, 'apple.html',{'msg':'Logged In as '+request.COOKIES.get('username')})
def onewithoutlogin(request):

    return render(request, 'apple.html',{'msg':'Please Login'})

def two(request):
    return render(request, '2.html')

def three(request):
    return render(request, '3.html')

def four(request):
    return render(request, '4.html')

def weekone(request):
    return render(request, 'weekoneinsert.html')


from django.views.decorators.csrf import csrf_exempt
#
@csrf_exempt
def weekoneinsert(request):
    print(request.GET.get("weekonedata"))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO activity VALUES (%s, %s,%s,%s)"
    val = (random.randint(1000,10000),1,request.GET.get("weekonedata"),request.GET.get("weekonedeadline"))
    print(val)
    mycursor.execute(sql, val)
    d={"msg":request.GET.get("weekonedata")+"Task Added Successfully"}
    mydb.commit()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM activity where week='1'")

    # Fetch all rows
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
    mydb.close()
    print()
    return render(request, 'weekoneinsert.html',{'rows': rows})
def weektwoinsert(request):
    print(request.POST.get("weektwodata"))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO activity VALUES (%s, %s,%s,%s)"
    val = (random.randint(1000, 10000), 2, request.GET.get("weektwodata"),request.GET.get("weektwodeadline"))
    print(val)
    mycursor.execute(sql, val)
    d = {"msg1": request.GET.get("weektwodata") + "Task delete Successfully"}
    mydb.commit()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM activity where week='2'")

    # Fetch all rows
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
    mydb.close()
    print()
    return render(request, 'weektwoinsert.html',{'rows': rows})

def weektwo(request):
    return render(request, 'weektwoinsert.html')

def weekthreeinsert(request):
    print(request.POST.get("weekthreedata"))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO activity VALUES (%s, %s,%s,%s)"
    val = (random.randint(1000, 10000), 3, request.GET.get("weekthreedata"), request.GET.get("weekthreedeadline"))
    print(val)
    mycursor.execute(sql, val)
    d = {"msg1": request.GET.get("weekthreedata") + "Task delete Successfully"}
    mydb.commit()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM activity where week='3'")

    # Fetch all rows
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
    mydb.close()
    print()
    return render(request, 'weekthreeinsert.html', {'rows': rows})

def weekthree(request):
    return render(request, 'weekthreeinsert.html')

def weekfourinsert(request):
    print(request.POST.get("weekfourdata"))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO activity VALUES (%s, %s,%s,%s)"
    val = (random.randint(1000, 10000), 4, request.GET.get("weekfourdata"), request.GET.get("weekfourdeadline"))
    print(val)
    mycursor.execute(sql, val)
    d = {"msg1": request.GET.get("weekfourdata") + "Task delete Successfully"}
    mydb.commit()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM activity where week='4'")

    # Fetch all rows
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
    mydb.close()
    print()
    return render(request, 'weekfourinsert.html', {'rows': rows})


def allrows(request):
    import mysql.connector

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    # Execute SQL query to fetch all rows from the table
    mycursor.execute("SELECT * FROM activity ")

    # Fetch all rows
    rows = mycursor.fetchall()

    # Close the cursor and connection
    mycursor.close()
    mydb.close()

    # Pass the data to the template
    return render(request, 'all.html', {'rows': rows})


def weekfour(request):
    return render(request, 'weekfourinsert.html')

def deleteweekonedata(request):
    import mysql.connector

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    mycursor.execute("delete from activity where task=\'"+request.GET['deleteweekonedata']+"\'")
    mydb.commit()
    mycursor = mydb.cursor()

    d = request.GET.get("deleteweekonedata") + " - Task Delete Successfully"
    mycursor.execute("SELECT * FROM activity ")
    # Fetch all rows
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and connection
    mycursor.close()
    mydb.close()
    print()
    print("Delete from activity where task=\'"+request.GET['deleteweekonedata']+"\'")


    # Pass the data to the template
    return render(request, 'deleteweekone.html', {'rows': rows,'msg1':d})


def deleteweekone(request):
    return render(request,'deleteweekone.html')

def set_cookie(request):
    response = HttpResponse("Cookie set successfully")
    response.set_cookie('username',request.POST.get("set_user") , max_age=3600)
    return response

def get_cookie(request):
    try:
        username = request.COOKIES.get('username')
        print(username)
    except :
        print('error')
    d = {"msg1": f"Welcome- { username }"}
    # return HttpResponse("Cookie set")
    return render(request, 'apple.html', d)

def delete_cookie(request):
    response = HttpResponse("Cookie deleted successfully")
    response.delete_cookie('username')
    return response

def cookie(request):
    return render(request,'cookie.html')
def cookie2(request):
    return render(request,'cookie2.html')

def delete(request):
    return render(request, 'delete_cookie.html')

def loginpage(request):
    return render(request,'loginpage.html')

def registerpage(request):
    return render(request,'register.html')

def register(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="todo"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO logindetails VALUES (%s, %s,%s)"
    val = (request.POST.get("EmailID"), request.POST.get("Username"),request.POST.get("password"))
    print(val)
    mycursor.execute(sql, val)
    d = {"msg1": "account created successfully"}
    mydb.commit()
    mycursor = mydb.cursor()

    return render(request, 'loginpage.html', d)
def loginpage(request):
    return render(request, 'loginpage.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render
import mysql.connector


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="todo"
        )

        mycursor = mydb.cursor()

        # Execute SQL query to fetch user with given email ID and password
        mycursor.execute("SELECT * FROM logindetails WHERE email = %s AND password = %s", (email, password))
        user = mycursor.fetchone()

        # Close the cursor and connection
        mycursor.close()
        mydb.close()
        print(email,password)
        if user is not None:
            # User exists and credentials are correct
            return render(request, 'apple.html')  # Render success page after login
        else:
            # User does not exist or credentials are incorrect
            return render(request, 'register.html')  # Render failure page after login

    else:
        # Render login page for GET request
        return render(request, 'loginpage.html')
