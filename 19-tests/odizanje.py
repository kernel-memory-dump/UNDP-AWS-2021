
def pripremi_operande(dal_ce_biti_greske):
    print('xxx')
    if dal_ce_biti_greske:
        raise Exception('dal_ce_biti_greske=True a ne sme da bude true, pa ce program puci')


def zbir(a, b, dal_ce_biti_greske):
    pripremi_operande(dal_ce_biti_greske)
    if a < 0:
        raise Exception('failed')
    return a+b


def f2(a):
    return zbir(2,2, a)

def f1(a):
    f2(a)

#try:
f1(True)
#     print('znaci nece doci dovde')
# #except:
#     print('we have failed xxxxxx')
#     print('upali smo u except, nsto je puklo')