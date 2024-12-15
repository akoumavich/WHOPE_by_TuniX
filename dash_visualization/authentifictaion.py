import pickle

# create a dictionary using {}
dico={'houssem': '1234', 'maissen': 'missou', 'gueddana': 'gaga', 'mohsen': 'momo'}
def save_dict(dico:dict):
    """Saves the usernames and passwords

    Args:
        dico (dict): dict of the passwords
    """    
    # save dictionary to authentification.pkl file
    with open('authentification.pkl', 'wb') as fp:
        pickle.dump(dico, fp)
        print('dictionary saved successfully to file')


if __name__=="__main__":
    with open('authentification.pkl', 'rb') as fp:
        USERNAME_PASSWORD_PAIRS = pickle.load(fp)
        key=input("Enter your username")
        password=input("Enter your password : ")
        USERNAME_PASSWORD_PAIRS[key]=password
    
    save_dict(USERNAME_PASSWORD_PAIRS)

def import_dico():
    """import usernames and passwords from file

    Returns:
        dict: dict of the passwords
    """    
    with open('authentification.pkl', 'rb') as fp:
        return pickle.load(fp)
    

