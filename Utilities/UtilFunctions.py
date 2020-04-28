import json
import ast

def getData(data_path, logger):
    f = open(data_path, "r")
    raw_data = f.read().split('\n')
    data = []
    cat_count = {}
    for row in raw_data:
        temp = json.loads(row)
        data.append(temp)
        category = temp['category']
        if category in cat_count:
            cat_count[category]+=1
        else:
            cat_count[category]=1


    logger.Log('Info', str(cat_count))
    logger.Log('Info', 'Number of links found : '+ str(len(data)))
    return data

def getData2(data_path, logger):
    f = open(data_path, "r")
    raw_data = f.read().split('\n')
    data = []
    cat_count = {}
    for row in raw_data:
        temp = ast.literal_eval(row)
        data.append(temp)
        category = temp['category']
        if category in cat_count:
            cat_count[category]+=1
        else:
            cat_count[category]=1


    logger.Log('Info', str(cat_count))
    logger.Log('Info', 'Number of links found : '+ str(len(data)))
    return data

def divideList(n, data, logger):
    list_of_lists = []
    l = len(data)
    size = int(l / n)
    logger.Log('Info', 'Number of divisions = ' + str(n))
    logger.Log('Info', 'Length of all data = ' + str(l))
    logger.Log('Info', 'Length of divisions =  ' + str(size))

    for i in range(0, n):
        if i== n-1:
            temp = data[i * size: ]
        else:
            temp = data[i* size : (i+1)*size]
        list_of_lists.append(temp)

    return list_of_lists




