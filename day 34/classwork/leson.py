def is_greeting(message):
    greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    message_lower = message.lower()
    return any(greet in message_lower for greet in greetings)
