B=[]
while 1:
 C=input();c=C[0];t=C[2:]
 if c=='r':B=open(t).read().splitlines()
 elif c=='w':open(t,'w').write('\n'.join(B))
 elif c=='a':B.append(t)
 elif c=='d':B.pop(int(t))
 elif c=='l':print('\n'.join(f'{i}:{l}'for i,l in enumerate(B)))
 elif c=='q':break
