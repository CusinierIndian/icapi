def searchable(queryParams, model):
	search = {
		'companyId' : {
			'operation' : 'ilike',
			'col' : model.companyId
		},
		'name' : {
			'operation' : 'ilike',
			'col' : model.name
		},
		'gender' : {
			'operation' : 'ilike',
			'col' : model.gender
		},
		'email' : {
			'operation' : 'ilike',
			'col' : model.email
		},
		'phone' : {
			'operation' : 'ilike',
			'col' : model.phone
		}
	}

	for key in queryParams.keys():
		if key in search:
			search.get(key)['value'] = queryParams.get(key)
			return search.get(key)

