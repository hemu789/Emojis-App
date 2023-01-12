from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    static_folder = os.path.join(os.getcwd(), 'static')
    png_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]
    random_image = random.choice(png_files)
    return render_template('index.html', image_file=random_image)

if __name__ == '__main__':
    app.run(debug=True)
