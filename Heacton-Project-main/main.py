from flask import Flask, render_template, request, jsonify, abort, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Rastgele bir secret key oluşturur

@app.before_request
def set_language():
    session['lang'] = request.args.get('lang', default='tr')  # session kullanımı için secret_key gerekiyor

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
    if request.method == 'POST':
        # Form verilerini işleyin
        return jsonify(message="Form başarıyla gönderildi!")
    return render_template('form.html', lang=session.get('lang', 'tr'))

# Uygulama çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
