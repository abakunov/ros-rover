from flask import Flask
from flask import request
import serial
import struct
import serial.tools.list_ports
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
serial_port = ''

@app.route('/get_serial_ports/', methods=['GET'])
@cross_origin()
def get_serial_ports():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    response = {'ports': connected, 'status': 'OK'}
    return response

@app.route('/set_serial_port/', methods=['POST'])
@cross_origin()
def set_serial_port():
    if request.method == "POST":
        global serial_port
        data = eval(request.get_data().decode('utf-8'))
        serial_port = data['port']
        return {'status': 'OK'}
    return {'status': 'Bad Request'}

@app.route('/execute_command/', methods=['POST'])
@cross_origin()
def execute_command ():
    if request.method == "POST":
        global serial_port
        data = eval(request.get_data().decode('utf-8'))
        command = data['command']
        value = data['value']
        command = eval("b'\\x"+command+"'")
        print(command)
        value = hex(int(value))[2::]

        f,s = "",""
        if len(value) == 1:
            s = "\\x0"+value
            f = "\\x00"
        elif len(value) == 2:
            s = "\\x"+value
            f = "\\x00"
        elif len(value) == 3:
            s = "\\x"+value[1::]
            f = "\\x0" + value[0]
        elif len(value) == 2:
            s = "\\x"+value[2:]
            f = "\\x"+value[:3:]

        
        
        strcuted_data = struct.pack('!3c', command, eval("b'"+f+"'") , eval("b'"+s+"'"))
        port = serial.Serial(serial_port, 19200)

        port.write(strcuted_data)
        return {'status': 'OK'}

    return {'status': 'Bad Request'}


if __name__ == "__main__":
    app.run(host='0.0.0.0')