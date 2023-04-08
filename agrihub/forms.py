from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,IntegerField,FileField
from wtforms.validators import InputRequired,DataRequired,Length,Email,EqualTo,ValidationError

from agrihub.models import Farmer,Buyer


class RegistrationFormFarmer(FlaskForm):
    username=StringField('Username',validators=[InputRequired(),Length(min=5,max=50)])
    email=StringField('Email',validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[InputRequired(),Length(min=4,max=50)])
    confirm_password=PasswordField('Confirm Password',validators=[InputRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        farmer=Farmer.query.filter_by(username=username.data).first()
        if farmer:
            raise ValidationError('This username is taken.Please choose a different one.')
    def validate_email(self,email):
        farmer=Farmer.query.filter_by(email=email.data).first()
        if farmer:
            raise ValidationError('This email is taken.Please choose a different one.')
        
class RegistrationFormBuyer(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=5,max=50)])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=4,max=50)])
    confirm_password=PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        buyer=Buyer.query.filter_by(username=username.data).first()
        if buyer:
            raise ValidationError('This username is taken.Please choose a different one.')
    def validate_email(self,email):
        buyer=Buyer.query.filter_by(email=email.data).first()
        if buyer:
            raise ValidationError('This email is taken.Please choose a different one.')

class LoginFormFarmer(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class LoginFormBuyer(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CropForm(FlaskForm):
    crop_name=StringField('crop_name',validators=[DataRequired(),Length(min=4,max=20)])
    crop_info=StringField('crop_info',validators=[DataRequired(),Length(min=20,max=100)])
    crop_rate=IntegerField('crop_rate',validators=[DataRequired()])
    address=StringField('address',validators=[DataRequired(),Length(min=5,max=100)])

    add_crop=SubmitField('Add Crop')
