from django.db import connection
from rest_framework.response import Response
from base64 import b64encode
import redis
from rest_framework.decorators import api_view


@api_view(['GET'])
def hasch_gen(request, id):
    r = redis.Redis(host='localhost', port=6379, db=0)
        
    q = '''SELECT new_function();'''
    l = r.llen('hesc')
    
    if l > 4000:
        return Response({'status' : '200'})
    else:
        for i in range(id):
            try:
                cursor = connection.cursor()
                cursor.execute(q)
                result = cursor.fetchall()
            
                text = str(result[0][0])
                text = text.encode('ascii')
                text_b64 = b64encode(text)
                    
                r.rpush('hesc', text_b64)
            except:
                print('Ошибка запроса')
    return Response({'status' : '200'})


