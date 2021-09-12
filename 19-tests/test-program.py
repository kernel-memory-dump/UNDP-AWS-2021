import program 
import sys

testovi_pali = []
testovi_prosli = []

def test1_zbir_poz_brojeva():
    ocekivano = 4
    dobijeno = program.poslovna_logika(2, 2)
    if dobijeno != ocekivano:
        testovi_pali.append(f'FAIL: poslovna_logika_test1 TEST NIJE PROSAO (2+2) je vratilo {dobijeno} UMESTO OCEKIVANOG {ocekivano}')
    else: 
        testovi_prosli.append(f'PASS: poslovna_logika_test1')

def test2_zbir_neg_brojeva():
    ocekivano = -1
    dobijeno = program.poslovna_logika(-2, 2)
    if ocekivano != dobijeno:
        testovi_pali.append(f'FAIL: test2_zbir_neg_brojeva TEST NIJE PROSAO (2+2) je vratilo {dobijeno} UMESTO OCEKIVANOG {ocekivano}')
    else: 
        testovi_prosli.append(f'PASS: test2_zbir_neg_brojeva')

def test2_zbir_nul_brojeva():
    ocekivano = -2
    dobijeno = program.poslovna_logika(0, 2)
    if ocekivano != dobijeno:
        testovi_pali.append(f'FAIL: test2_zbir_neg_brojeva TEST NIJE PROSAO (2+2) je vratilo {dobijeno} UMESTO OCEKIVANOG {ocekivano}')
    else: 
        testovi_prosli.append(f'PASS: test2_zbir_neg_brojeva')

test1_zbir_poz_brojeva()
test2_zbir_neg_brojeva()
test2_zbir_nul_brojeva()

# for each 
for prosao_test in testovi_prosli:
    print(prosao_test)

for test_pao in testovi_pali:
    print(test_pao)

sve_ok = 0
nije_sve_ok = 1

if len(testovi_pali) > 0:
    sys.exit(nije_sve_ok) # vratiti izlazni / code naseg programa
else:
    sys.exit(sve_ok)
