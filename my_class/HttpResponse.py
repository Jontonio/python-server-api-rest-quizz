from flask import jsonify

class HttpResponse:
    
    def res_error(self, message:str, status:int, data):
        return jsonify({
            "message":message,
            "status":status,
            "error":True,
            "data":data,
        }), status
    
    def res_success(self, message:str, status:int, data):
        return jsonify({
            "message":message,
            "status":status,
            "error":False,
            "data":data,
        }), status
    