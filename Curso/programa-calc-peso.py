peso = input('Digite su peso: ')
tip = input('(L)bs o (K)g: ')
if tip.lower() == 'l':
    pesoc = float(peso) *0.453592
    print('su peso de '+peso+' lb son '+str(pesoc) +' en kilogramos')
elif tip.lower()=='k':
    pesoc = float(peso) / 0.453592
    print('su peso de '+peso+' Kg son '+str(pesoc) +' en Libras')
else:
    print("Debe colocar un L para Libras y una K para kilogramos")