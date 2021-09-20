from time import sleep
def maior(* valores):
    mai = max(valores)
    tam = len(valores)
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i, v in enumerate(valores):
        print(f'{v} ', end='')
        sleep(1)
    print(f'Foram informados {tam} valores ao todo.', end='')
    print()
    print(f'O maior valor informado foi {mai}.')



maior(5, 4, 3, 1, 55, 24)
maior(10, 0, 25, 19)