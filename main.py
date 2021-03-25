import socketio
import subprocess

# traverse the software list
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)
print("Try Done")
# try block
try:
    print("Try Done")
    # arrange the string
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])

except IndexError as e:
    print("All Done")
# standard Python
sio = socketio.Client()
sio.connect('http://localhost:5000')
print('my sid is', sio.sid)
sio.emit('chat', {sio.sid: a})
