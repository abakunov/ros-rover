from flask import Flask
from flask import request
import serial
import struct
import serial.tools.list_ports

app = Flask(__name__)

serial_port = ''

@app.route('/get_serial_ports/', methods=['GET'])
def get_serial_ports():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    response = {'ports': connected, 'status': 'OK'}
    return response

@app.route('/set_serial_port/', methods=['POST'])
def set_serial_port():
    if request.method == "POST":
        global serial_port
        serial_port = request.form['port']
        return {'status': 'OK'}
    return {'status': 'Bad Request'}

@app.route('/execute_command/', methods=['POST'])
def execute_command ():
    if request.method == "POST":
        global serial_port
        command = request.form['command']
        value = request.form['value']
        command = eval("b'\\x"+command+"'")
        
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
        global serial_port
        
        
        strcuted_data = struct.pack('!3c', command, eval("b'"+f+"'") , eval("b'"+s+"'"))
        port = serial.Serial(serial_port, 19200)
        port.write(strcuted_data)
        return {'status': 'OK'}

    return {'status': 'Bad Request'}


if __name__ == "__main__":
    app.run(host='0.0.0.0')