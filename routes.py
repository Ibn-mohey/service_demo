from flask import Flask, render_template, request, jsonify, url_for
from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    session
)
import sqlite3
from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)



from app import create_app,db,login_manager,bcrypt
from models import User,Event
from forms import login_form,register_form,UserForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

# url_for('static', filename='path/to/file')


#
# 

@app.route("/image") 
def serve_image(): 
    message = "Image Route"
    return render_template('image.html', message=message)


@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5000)
#to do 
#print data 
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
@login_required
def index():
    # print("session",session)
    return render_template('index.html')


@app.route("/service/", methods=("GET", "POST"), strict_slashes=False)
@login_required
def service():
    data = "from form"
    # model save 
    event_categorys = """فرح
    عيد ميلاد
    حفل تخرج
    الاحتفال بمولود جديد
    """.split('\n')[:-1]
    event_hall_categorys = """مفتوح
    مغطي بتهوية خارجية
    مغلق مكيف 
    مغلق بتهوية داخلية
    """.split('\n')[:-1]
    data = request.form.to_dict()
    conn = sqlite3.connect('./instance/database.db')
    cursor = conn.cursor()
    sql = f"""
    insert into events 
    {tuple(data.keys())}
    Values 
    {tuple(data.values())};
    """
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        pass
    conn.close()
    # print(data)
    # db.events.insert_one(data)
    # print("test service",type(request.form))
    return render_template('service.html',event_categorys=event_categorys,event_hall_categorys=event_hall_categorys)

@app.route("/booked_services/", methods=("GET", "POST"), strict_slashes=False)
@login_required
def test2():
    user_id = session['_user_id']
    events = Event.query.all()
    # print("test",)
    return render_template('orders.html',events=events)



@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("اسم المستخدم او كلمة السر غير صحيحة!", "danger")
        except Exception as e:
            flash(f'{e} خطا غير مفهوم حاول مجددا', "danger")

    return render_template("login.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )

# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = UserForm()
    if request.method == 'POST':
        print(request.form.get("username"))
        # print("form2: ",form2)
        try:
            username= request.form.get('username')
            first_name= request.form.get('first_name')
            last_name= request.form.get('last_name')
            national_id= request.form.get('national_id')
            nationality = request.form.get('nationality ')
            gender= request.form.get('gender')
            date_of_birth= request.form.get('date_of_birth')
            mobile_number= request.form.get('mobile_number')
            email= request.form.get('email')
            user_type= request.form.get('user_type')
            pwd = request.form.get('pwd')
            print("PWD",pwd)
            # username = form.username.data
            # form.populate_obj(request.form)
            newuser = User(
                first_name=first_name,
                last_name=last_name,
                national_id=national_id,
                nationality =nationality ,
                gender=gender,
                date_of_birth=date_of_birth,
                mobile_number=mobile_number,
                user_type=user_type,
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )
    
            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Successfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            print(f"Something went wrong!", "danger")
        except IntegrityError as e:
            db.session.rollback()
            print(e)
            print(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            print(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            print(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            print(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            print(f"An error occurred !", "danger")
    return render_template("register.html",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account"
        )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
# @app.route("/service/", methods=("GET", "POST"), strict_slashes=False)
# def service():

if __name__ == "__main__":
    app.run(debug=True)
