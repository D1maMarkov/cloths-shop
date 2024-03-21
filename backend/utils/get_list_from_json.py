def get_list_from_json(json):
    if json:
        return json.split(',')
    else:
        return []