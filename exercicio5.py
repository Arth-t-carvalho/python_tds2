camisa = int(input('digite quantas camisas vc deseja'))
if camisa <= 5: 
    print(f"o valor a ser pago é{(camisa*12.50)-((camisa*12.50)*3)/100}")
if camisa > 5 and camisa <10:  
    print(f"o valor a ser pago é{(camisa*12.50)-((camisa*12.5)*5)/100}")
if camisa > 10: 
    print(f"o valor a ser pago é{(camisa*12.50)-((camisa*12.5)*7)/100}")
