Card12=int (input ("Ange pris för årskort: "))
print("Årskort kostar" ,Card12, "Kr" )
Entry=int (input ("Ange pris för inträde: "))
Entrykr=int (input ("Hur många gånger per år är du där: "))
kostnad= (Entry * Entrykr)
print ("Det kostar samalagt" ,kostnad, "kr för varje gång")
if kostnad<Card12:
    print("Du tjänar inte på ett årskort")    
else:
    print("Du tjänar på att köpa ett årskort")