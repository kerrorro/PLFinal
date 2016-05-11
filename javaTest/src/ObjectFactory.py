class Employee(object):
    def f(self):
        data = {
            'id': 0,
            'lastName': '',
            'firstName': '',
            'userId': '',
            'title':'',
            'dept_id': 0,
            'manager_id': 0,
            '$id': lambda x: data.update({'id': x}),
            '$lastName': lambda x: data.update({'lastName': x}),
            '$firstName': lambda x: data.update({'firstName': x}),
            '$userId': lambda x: data.update({'userId': x}),
            '$title': lambda x: data.update({'title': x}),
            '$dept_id': lambda x: data.update({'dept_id': x}),
            '$manager_id': lambda x: data.update({'manager_id': x}),
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)


    #
    # toReturn = substance()
    # toReturn.run("")