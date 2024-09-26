# 2] Below is a text with several characters enclosed in square brackets [ and ].
# Scan the text and print out all characters which are between square brackets.
text  =	"""And  sending	tinted  postcards  of  places  they  don ' t
realise  they  haven ' t	even	visited  to	' All  at  nu[m]ber  22,  weather
w[on]derful ,  our	room	is	marked  with	an	' X ' .  Wish  you  were  here.
Food  very  greasy	but  we ' ve  found  a  charming  li[t]tle  local  place
hidden	awa[y  ]in	the  back  streets  where  they  serve  Watney ' s  Red
Barrel	and  cheese	and	onion  cris[p]s	and	the  accordionist  pla[y]s
"Maybe	i[t ] ' s  because	I ' m  a  Londoner " '  and  spending  four  days  on
the  tarmac  at  Luton  airport  on  a  five -day  package  tour  wit[h]
n[o]thing  to  eat	but	dried  Watney ' s	sa[n]dwiches ... """
si=0
while(True):
    si=text.find("[",si)
    if(si==-1):break
    ei=text.find("]",si+1)
    if(ei==-1):break
    print(text[si:ei])
