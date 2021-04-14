#09/12/20

ent = input("DIGITE ALGUMA COISA:")
print('Tipo: {}'.format(type(ent)),
      '\nÉ somente espaços: {}'.format(ent.isspace()),
        '\nÉ um número: {}'.format(ent.isnumeric()),
      '\nÉ um letra: {}'.format(ent.isalpha()),
      '\nÉ um alfanumérico: {}'.format(ent.isalnum()),
      '\nEstá em letras maisculas: {}'.format(ent.isupper()),
      '\nEstá em letras minúsculas: {}'.format(ent.islower()),
      '\nEstá capitalizada: {}'.format(ent.istitle()))