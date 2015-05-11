__author__ = 'voldy'

from bottle import request,route,static_file,run
import MeatWorker as workers

@route('/send', method='POST')
def send():
    workers.meatQueue.put(request._get_body_string())
    #print requestBody
    return "Success"



if __name__ == '__main__':
    workers.startWorker()
    run(host='localhost',port =8081)