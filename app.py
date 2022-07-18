from flask import Flask, render_template, send_file
from flask import make_response
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    data = {}
    data["Create_the_files"] = "/createFiles"
    data["dnld_2mb_file"] = "/dnld2mb"
    data["dnld_100mb_file"] = "/dnld100mb"
    data["dnld_1gb_file"] = "/dnld1gb"
    return data

@app.route('/createFiles', methods=['GET'])
def createTextFiles():
    f = open("2MBFile.txt", "w")
    size = 1000*1000*2 # 2 mb
    f.write("a" * size)

    f = open("100MBFile.txt", "w")
    size = 1000*1000*100 # 100 mb
    f.write("\0" * size)

    f = open("1GBFile.txt", "w")
    size = 1000*1000*1000*1 # 1 gb
    f.write("\0" * size)

    f = open("sample.txt", "w")
    size = 1000*1000*1000*5 # 1 gb
    f.write("\0" * size)

    
    return "File created"


@app.route('/dnld', methods=['GET'])
def write_file():
    out_file = "./sample.txt"
    response = make_response(send_file(out_file, as_attachment=True))
    response.headers['Content-Length'] = "10"
    return response 

@app.route('/dnld2mb', methods=['GET'])
def write_file_from_text2mb():
    out_file = "./2MBFile.txt"
    response = make_response(send_file(out_file, as_attachment=True))
    response.headers['Content-Length'] = "10"
    return response 

@app.route('/dnld100mb', methods=['GET'])
def write_file_from_text2():
    out_file = "./100MBFile.txt"
    response = make_response(send_file(out_file, as_attachment=True))
    response.headers['Content-Length'] = "10"
    return response 

@app.route('/dnld1gb', methods=['GET'])
def write_file_from_text3():
    out_file = "./1GBFile.txt"
    response = make_response(send_file(out_file, as_attachment=True))
    response.headers['Content-Length'] = "1"
    return response 

if __name__ == '__main__':
    app.run(host='0.0.0.0')
