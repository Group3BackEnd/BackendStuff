import MySQLdb

def fword(lon,lat,radius,ids):
    #retrieve all datas in the vicinity of this point
    #filter the data to take off all existing ids
    #return a json string to init.py
    try:
        result = str(lon)+str(lat)+str(radius)+str(ids)
        return result
    except Exception as e:
        return str(e)
