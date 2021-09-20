from random import randint
pc = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'''Os valores sorteados foram: {pc} 
O Maior valor foi {max(pc)}
O menor valor foi {min(pc)}''')
