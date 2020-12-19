from random import choice

answers = ['Sim', 'Não', 'Sim!', 'Não!', 'Acho que sim...', 'Acho que não...', 'Óbvio que sim', 'Óbvio que não', 'Claro que sim', 'Claro que não', 'Talvez...', 'Melhor não...', 'Com certeza!', 'Não sei...', 'Sei lá', 'Não posso responder isso', 'Você que sabe', 'Se você quer...', 'A decisão é sua!']

while True:

    question = input('Digite sua pergunta: ')

    if question.isalpha() != True and not '?' in question:
        print('Ei, faça uma pergunta!')
        continue
    
    else:
        print(choice(answers))
