class Conversao:
    
    def velocidade () : 
        kmh = [75.4, 30.6, 120, 32.8, 20.8]
        mph = [round(x/1.61,2) for x in kmh]
        x = 0
        while(x<5) :
            print(kmh[x],"kmh em mph são", mph [x])
            x += 1  
    
    def temperatura ():
        celsius = [45,30,12.5,32.6,50]
        fahrenheit = [round((x*1.8)+32,2) for x in celsius]
        x = 0
        while(x<5) :
            print(celsius[x],"celsius em fahreheit são",fahrenheit[x])
            x += 1   
   
    def altura ():

        pés = [57,63,77,82,94]
        metros = [round((x*1)*0.3048,2 ) for x in pés]   
        x = 0
        while(x<5) :
            print(pés[x],"pés em metros são",metros [x])
            x += 1   
       
    
    def idade():
        anos = [13,16,18,19,23]
        meses = [ (x*12) for x in anos]
        x = 0
        while(x<5) :
            print(anos[x],"anos em meses são", meses[x])
            x += 1 