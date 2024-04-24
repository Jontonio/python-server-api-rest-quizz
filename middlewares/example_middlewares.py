# Define el middleware
from functools import wraps
from flask import request, jsonify
numero_magino = 10;

def middleware_example():
    def _home_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):
            all_param = request.args.get('all')
            print(all_param)
            result = f(*args, **kwargs)
            if int(request.view_args.get('id'))==10:
                print("Pasas")
            else:
                return jsonify({
                    "message": "No pasas"
                }), 401
            return result
        return __home_decorator
    return _home_decorator