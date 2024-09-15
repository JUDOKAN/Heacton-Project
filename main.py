from flask import Flask, render_template, request, jsonify, abort, session
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

# Flask uygulamasını başlat
app = Flask(__name__)

# Konfigürasyonlar
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy veritabanı
db = SQLAlchemy(app)

# Veritabanı modeli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# FlaskForm ile anket formu
class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    date = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    selected_options = SelectField('Country', choices=[
        ('tr', 'Turkey'), 
        ('us', 'United States'),
        ('ru', 'Russia')
    ], validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired(), Length(min=5, max=10)])
    submit = SubmitField('Submit')

# Dil seçimi için session kullanımı
@app.before_request
def set_language():
    if 'lang' not in session:
        session['lang'] = request.args.get('lang', default='tr')
    else:
        session['lang'] = request.args.get('lang', session['lang'])

# Anasayfa rotası
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', lang=session.get('lang', 'tr'))

# Hakkında sayfası rotası
@app.route('/about.html')
def about():
    return render_template('about.html', lang=session.get('lang', 'tr'))

# Tarihçe sayfası rotası
@app.route('/history.html')
def history():
    return render_template('history.html', lang=session.get('lang', 'tr'))

# Sıkça Sorulan Sorular (SSS) sayfası rotası
@app.route('/faq.html')
def faq():
    return render_template('faq.html', lang=session.get('lang', 'tr'))

# Ürünler sayfası rotası
@app.route('/products.html')
def products():
    return render_template('products.html', lang=session.get('lang', 'tr'))

# Anket formu sayfası
@app.route('/form.html', methods=['GET', 'POST'])
def form():
    form = SurveyForm()
    if form.validate_on_submit():
        # Form verilerini işleyin
        return jsonify(message="Form başarıyla gönderildi!")
    return render_template('form.html', form=form, lang=session.get('lang', 'tr'))

# Bot çalıştırma rotası
@app.route('/bot.py')
def run_bot():
    return jsonify(message="Bot çalıştırma işlemi üzerinde çalışılıyor!")

# Veritabanını başlatma
with app.app_context():
    db.create_all()

# Uygulama çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
