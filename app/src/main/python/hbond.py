import math
    #convert scientific to engineering
    #fine dist between 1,2 and 2,3
    #conver bohr dist to armstrongs
    #extract first atom van der waals constant minus from dist between 1,2 name it rd
    #extract last atom van der waals constant minus from dist between 2,3 name it ra
    #if rd>ra : distance criteria satisfied
    #if (rd+ra)>0 and (rd-ra)>0 print hydrogen bond if not print van der waals
def listToString(dis):

    str1 = ""
 
    for ele in dis:
        str1 += ele+'\n'
 
    return str1
def distance(x):
    coord=[]
    #FH=open (x,'r')
    #lines=FH.readlines()
    lines=x.splitlines()
    l=len(lines)
    for i in range(l):
        b=lines[i].split()
        for j in range (1,4):
                b[j]=float(b[j])
        coord.append(b)
    #print (coord)
    d=[]
    for j in range (0,l,3):
        d1=(math.sqrt((coord[j+1][1]-coord[j][1])**2 + (coord[j+1][2]-coord[j][2])**2 + (coord[j+1][3]-coord[j][3])**2))*0.5292
        d2=(math.sqrt((coord[j+2][1]-coord[j+1][1])**2 + (coord[j+2][2]-coord[j+1][2])**2 +(coord[j+2][3]-coord[j+1][3])**2))*0.5292
        d.append(d1)
        d.append(d2)
    #print (d)
    
    
    #for i in range 3:
     #   d1[i]*=0.5292
    vanderwaals_constants={"H":1.2,"C":1.70,"O":1.52,"N":1.55,"He":1.4,"F":1.47,"Si":2.10,"P":1.80,"S":1.80,"Cl":1.75,"As":1.85,"Se":1.90,"Br":1.85,"Te":2.06,"I":1.98}
    v=[]
    for j in range (0,l,3):
        vdw1=vanderwaals_constants[coord[j][0]]
        vdw2=vanderwaals_constants[coord[j+2][0]]
        v.append(vdw1)
        v.append(vdw2)
    #print (v)
    dis=[]
    for k in range (0,len(v),2):
        rd=v[k]-d[k]
        ra=v[k+1]-d[k+1]
        #print (rd,ra)
        if rd>ra:
            if (rd+ra)>0 and (rd-ra)>0:
                dis.append("Hydrogen bond")
            else:
                dis.append("Van der waals bond")
    str2=listToString(dis)
    return(str2)
