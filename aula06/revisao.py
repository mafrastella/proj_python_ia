kg = [1,10,0.5,0.25,0.01]
g = [(x*1000) for x in kg]
print ("{:<4}{:<6}{:<8}".format("N°","Kg","gramas"))
print("===+=====+========")
for x in range(0,len(kg),1):
    print("{:<4}{:<6}{:<8}".format(x+1,kg[x],g[x]))