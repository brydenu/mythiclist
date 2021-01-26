from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length


class CreateUserForm(FlaskForm):
    """Form for registering a new user"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login user form"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class ListForm(FlaskForm):
    """Create/modify list form"""

    title = StringField('Title', validators=[DataRequired()])
    ranked = BooleanField('Ranked ')
    private = BooleanField('Private')
