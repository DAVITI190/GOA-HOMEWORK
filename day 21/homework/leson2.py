def who_ate_the_cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)):
        name = "Monica"
    else:
        name = "the dog"
    return f"Who ate the last cookie? It was {name}!"


who_ate_the_cookie("hi")    
who_ate_the_cookie(3.14)      
who_ate_the_cookie(True)      
