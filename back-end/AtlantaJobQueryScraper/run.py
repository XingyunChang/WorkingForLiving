import threading
import json
import time
from clean_json import cleaned_name
from csv_to_json import json_name
from query import query

from flask import Flask,request

# Declaration of global variables
input_list = []
response_dict = {}
# Process lock
lock = threading.Lock()


def start():

    global input_list
    global response_dict
    global lock

    with open(cleaned_name, "r") as fh:
        job_database = json.load(fh)

    with open(json_name, "r") as fh:
        house_database = json.load(fh)

    print("Thread - Model >> Database starts ready for query.")

    while True:
        lock.acquire()
        if input_list:
            request = input_list.pop(0)
            ip = request.get('IP')
            infos = request.get('infos')
            print("Thread - Database >> Successfully removed request from IP", ip)

            result = query(job_database, house_database, infos)

            response_dict[ip] = result
            print("Thread - Database >> Successfully queried for request from IP", ip)
        lock.release()
        # time.sleep(0.1)


app = Flask(__name__)
@app.route('/api/atlantaJobQuery', methods=['get'])
def atlantaJobQuery():
    global input_list
    global response_dict
    global lock

    try:
        infos = request.args['infos']
    except:
        infos = {}
    ip = request.remote_addr

    lock.acquire()
    input_list.append({'IP': ip, 'infos': infos})
    print("Thread - HTTP Manager >> Successfully queued request from IP", ip)
    lock.release()

    while ip not in response_dict:
        time.sleep(0.01)

    lock.acquire()
    text = response_dict.pop(ip)
    print("Thread - HTTP Manager >> Successfully retrieved response for IP", ip)
    lock.release()

    return text


if __name__ == '__main__':
    app.debug = False
    model_thread = threading.Thread(target=start)
    model_thread.start()
    app.run(host='0.0.0.0', port=8000)
