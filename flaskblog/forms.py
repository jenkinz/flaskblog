"""
forms.py
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    TextAreaField,
    ValidationError,
)
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    """RegistrationForm"""

    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo(fieldname="password")],
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:  # user already exists
            raise ValidationError(
                "That username is taken. Please choose a different one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:  # user already exists
            raise ValidationError("That email is taken. Please choose a different one.")


class LoginForm(FlaskForm):
    """LoginForm"""

    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    """UpdateAccountForm"""

    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    picture = FileField(label="Update Profile Picture", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:  # user already exists
                raise ValidationError(
                    "That username is taken. Please choose a different one."
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:  # user already exists
                raise ValidationError("That email is taken. Please choose a different one.")


class PostForm(FlaskForm):
    """PostForm"""
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
