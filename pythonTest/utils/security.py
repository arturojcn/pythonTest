import bcrypt
  
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))  
