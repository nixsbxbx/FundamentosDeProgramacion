''' 
una tienda ofrece un descueto del 15% sobre el total de la
compra y un cliente desea saber cuanto debera pagar 
finalmente por su compra
entrada:
total de compra: = tc
salidas:
total de compra - descuento
precio final: 
'''
tc = input("escribe el total de compra: ")
tc = int(tc)
pf = (tc- (tc * 0.15))
print("El pago final de la compra es: " , pf)