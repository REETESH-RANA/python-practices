# here player name virat and rohit and their jerrsey number 18,45
# and in second tuple there are six entries first for dotball means no run count,2nd for scoring 1 run ,
# 3rd for scoring 2 runs, 4th for scoring 3 runs,5th for scoring 4runs, 6th for scoring 6s and change player when someone score 3 runs or when over is over
# and finally print the summary of the match
T=(('Virat',"18",(0,0,0,0,0,0)),('Rohit',"45",(0,0,0,0,0,0)))
temp=()
rep=0
for i in range(1,7):
    run=int(input("enter the runs:"))
    if(run==1 or run==3 or i==6):
        rep=1
        if(rep==0):
         if(run==6):
            t=T[rep][2][run-1]
