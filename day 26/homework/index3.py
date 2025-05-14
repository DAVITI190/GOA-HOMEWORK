def get_expression_type():
    expr = input("შეიყვანე მათემატიკური გამოსახულება: ")
    try:
        result = eval(expr)
        print("შედეგის ტიპი:", type(result).__name__)
    except Exception as e:
        print("შეცდომა:", e)
