from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/karyawan', methods=['GET','POST','PUT','DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama': 'Yanto GET',
                'pekerjaan': 'Web Designer',
                'usia': '27'
            }]
        elif request.method == 'POST':
            data = [{
                'nama': 'Sunarto POST',
                'pekerjaan': 'Web Engineer',
                'usia': '33'
            }]
        elif request.method == 'PUT':
            data = [{
                'nama': 'Sunarti PUT',
                'pekerjaan': 'UI UX',
                'usia': '23'
            }]
        elif request.method == 'DELETE':
            data = [{
                'nama': 'Sugeng DELETE',
                'pekerjaan': 'Data Analyst',
                'usia': '31'
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()