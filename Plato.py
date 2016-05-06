class substance(object):
    def f(self):
        data = {
            'name': 'Rita',
            '$name': lambda x: data.update({'name': x}),
            'age': 67,
            '$age': lambda x: data.update({'age': x})
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