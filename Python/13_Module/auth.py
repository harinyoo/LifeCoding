def login(id):
    members = ['brooklyn', 'sydney', 'victoria']
    for member in members:
        if member == id:
            return True
    return False
