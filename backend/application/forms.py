from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class CreatePost(FlaskForm):
    blog_title = TextField('Blog Title', [DataRequired()])
    blog_category = SelectField(
        'Category',
        choices=[('writing', 'writing'), ('success', 'success'),
                 ('journal', 'journal'), ('tech', 'tech'), ('other', 'other')]
    )
    blog_content = TextAreaField('Content', [DataRequired(), Length(
        min=100, message="Your content is too little. Write some more!")])
    submit = SubmitField('Create Post')
