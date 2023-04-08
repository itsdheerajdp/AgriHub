from flask import render_template,url_for,redirect,flash,request
from agrihub import app,db,bcrypt
from agrihub.forms import RegistrationFormBuyer,RegistrationFormFarmer,LoginFormBuyer,LoginFormFarmer,CropForm
from flask_login import login_required,logout_user
from agrihub.models import Farmer,Buyer,Crop
from flask_login import login_user,current_user,logout_user,login_required
import pickle 

model=pickle.load(open("./agrihub/model.pkl","rb"))

@app.route("/")
@app.route("/home")
def home():
    print("home")
    return render_template('home.html')


@app.route('/predictor', methods=["GET","POST"])
def predictor():
    if(request.method=="POST"):
        nitrogen=request.form["Nitrogen"]
        phosphorus=request.form["phosphorus"]
        potassium=request.form["potassium"]
        temper=request.form["temperature"]
        hum=request.form["humidity"]
        ph=request.form["ph"]
        rf=request.form["rainfall"]
        prediction=model.predict([[nitrogen,phosphorus,potassium,temper,hum,ph,rf]])
        return render_template('prediction.html',predict=prediction)
    return render_template('predictor.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/marketprice')
def marketprice():
    return render_template('marketprice.html')
@app.route('/register')
def register():
    print("register")
    return render_template('register.html')

@app.route("/registerFarmer" ,methods=['GET','POST'])
def registerFarmer():
    print("farmer register")
    # if current_user.is_authenticated:
    #     print("authenticated")
    #     return redirect(url_for('home'))
    print("farmer not authenticated")
    form=RegistrationFormFarmer()
    if form.validate_on_submit():
        print("validate on submit")
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode ('utf-8')
        farmer=Farmer(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(farmer)
        db.session.commit()
        print(Farmer.query.filter_by(username=form.username.data).first())
        print("added to database")
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('farmerLogin'))
    return render_template('register_farmer.html',form=form)

@app.route("/registerBuyer",methods=['GET','POST'])
def registerBuyer():
    print("hello")
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form=RegistrationFormBuyer()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode ('utf-8')
        buyer=Buyer(username=form.username.data,email=form.email.data,password=hashed_password)
        print(buyer)
        db.session.add(buyer)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('buyerLogin',error='Your'))
    print("hello")
    return render_template('register_buyer.html',form=form)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/farmerLogin",methods=['GET','POST'])
def farmerLogin():
    if current_user.is_authenticated:
        return redirect(url_for('farmerDashboard'))
    form =LoginFormFarmer()
    if form.validate_on_submit():
        farmer=Farmer.query.filter_by(email=form.email.data).first()
        if farmer and bcrypt.check_password_hash(farmer.password,form.password.data):
            login_user(farmer)
            # return redirect(url_for('farmerDashboard'))
            next_page=request.args.get('next')
            return redirect(next_page)if next_page else redirect(url_for('farmerDashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('farmer_login.html', form=form)

@app.route('/farmerdashboard',methods=["GET","POST"])
def farmerDashboard():
     form=CropForm()
     if form.validate_on_submit():
        crop=Crop(crop_name=form.crop_name.data,content=form.crop_info.data,price=form.crop_rate.data,farmer_address=form.address.data)
        db.session.add(crop)
        db.session.commit()
        # flash('Crop added successfully!','success')
        return redirect('/farmerdashboard')
     return render_template('farmerdashboard.html',form=form)
    

@app.route("/buyerLogin",methods=['GET','POST'])
def buyerLogin(): 
    if current_user.is_authenticated:
        return redirect('/buyerdashboard')
    form =LoginFormBuyer()
    if form.validate_on_submit():
        buyer=Buyer.query.filter_by(email=form.email.data).first()
        if buyer and bcrypt.check_password_hash(buyer.password,form.password.data):
            login_user(buyer)
            return render_template('buyerdashboard.html')
            # next_page=request.args.get('next')
            # return redirect(next_page)if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')

    return render_template('buyer_login.html',form=form)

@app.route('/buyerdashboard',methods=["GET","POST"])
def buyerDashboard():
     crops=Crop.query.all()
     print(crops)
     return render_template('buyerdashboard.html',crops=crops)



@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
   

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))