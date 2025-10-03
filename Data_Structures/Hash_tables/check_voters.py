voted = {}

def check_voters(name):
    if name in voted:
        print("kivk them out")
    else:
        voted[name] = True
        print("Let them vote")