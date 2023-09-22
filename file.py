from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jitesh'
app.config['MYSQL_PASSWORD'] = 'my_sql'
app.config['MYSQL_DB'] = 'user_db'

mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        user_details = request.form
        fname = user_details['f_name']
        lname = user_details['l_name']
        p_no = user_details['phone_no']
        cur = mysql.connection.cursor()
        cur.execute("insert into info(f_name,l_name,pho_no) values(%s,%s,%s)",
                    (fname, lname, p_no))
        mysql.connection.commit()
        cur.close()
        return render_template('user.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
