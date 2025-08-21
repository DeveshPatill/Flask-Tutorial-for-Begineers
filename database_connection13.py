
from flask import Flask,render_template,session,request
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="myflaskdb"
mysql=MySQL(app)


@app.route('/')
def index():
    iid=4
    firstname="kavita"
    lastname="patil"
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO user_students(id,fname,lname) VALUES(%s,%s,%s)", (iid,firstname,lastname))
    mysql.connection.commit()
    cur.close()
    return "succesfully inserted the data in mysql database"


if __name__ == "__main__":
    app.run(debug=True)
