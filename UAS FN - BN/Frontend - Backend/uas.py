from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
import os

# Inisialisasi Flask dan MongoDB
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/') 
db = client['db_penginapan']
rooms_collection = db['user']

# Route untuk halaman daftar kamar
@app.route('/')
def index():
    rooms = list(rooms_collection.find())
    return render_template('daftarkamar.html', rooms=rooms)

# Endpoint untuk menambah kamar baru
@app.route('/add_room', methods=['POST'])
def add_room():
    room_name = request.form.get('nama_kamar')
    if not room_name:
        return jsonify({'status': 'error', 'message': 'Nama kamar tidak boleh kosong'}), 400

    room_data = {
        'name': room_name,
        'image': 'default.jpg',  # Pastikan ada file 'default.jpg' di folder 'static/images'
        'details': 'Ukuran kamar: 18 m²/194 ft²\nPemandangan: Kota\n2 kasur single'
    }
    rooms_collection.insert_one(room_data)
    return redirect(url_for('daftarkamar'))

# Route untuk halaman detail kamar
@app.route('/detail')
def detail():
    room_name = request.args.get('nama')
    room = rooms_collection.find_one({'name': room_name})
    if not room:
        return "Kamar tidak ditemukan", 404

    # Convert ObjectId to string for JSON compatibility
    room['_id'] = str(room['_id'])

    return render_template('detail.html', room=room)

if __name__ == '__main__':
    # Pastikan jalankan aplikasi pada mode debug
    app.run(debug=True)