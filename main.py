import json as J,os,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
N=(-33,-31,-18,-14,14,18,31,33)
K=(-17,-16,-15,-1,1,15,16,17)
Y=(-17,-15,15,17)
H=(-16,-1,1,16)
D={0:2,7:1,112:8,119:4}
def P(p,b):
 try:
  with U.urlopen(E+p,J.dumps(b).encode())as r:return J.load(r)
 except Exception:return {}
B=[0]*128;SD=1;C=0;EP=-1
def F(f):
 global B,SD,C,EP
 B=[0]*128;SD=1;C=0;EP=-1
 w=f.split()
 s="".join("."*int(c)if c.isdigit()else c for c in w[0].replace("/",""))
 for k,ch in enumerate(s):
  if ch!=".":
   j="PNBRQKpnbrqk".index(ch);B[(7-k//8)*16+k%8]=(j%6+1)*(1-2*(j>5))
 SD=1-2*(w[1]=="b")
 C=sum(1<<k for k in range(4)if"KQkq"[k]in w[2])
 EP=-1 if w[3]=="-" else ord(w[3][0])-97+(int(w[3][1])-1)*16
def S(m):
 f=m&127;t=m>>7&127;r=m>>14
 return chr(f%8+97)+str(f//16+1)+chr(t%8+97)+str(t//16+1)+("nbrq"[r-2] if r else"")
def A(q,s):
 for x in(q-15*s,q-17*s):
  if not x&0x88 and B[x]==s:return 1
 for d in N+K:
  x=q+d
  if not x&0x88 and B[x]==(2*s if d in N else 6*s):return 1
 for d in K:
  x=q+d
  while not x&0x88:
   if B[x]:
    if B[x]==5*s or B[x]==(3*s if d in Y else 4*s):return 1
    break
   x+=d
 return 0
def G(q):
 m=[]
 for i,p in enumerate(B):
  if p*SD<=0 or i&0x88:continue
  t=abs(p)
  if t==1:
   d=16*SD;o=i+d
   if not B[o]:
    if o<8 or o>111:m+=[i|o<<7|k<<14 for k in(5,4,3,2)]
    elif not q:
     m.append(i|o<<7)
     if i>>4==1+5*(SD<0) and not B[i+2*d]:m.append(i|(i+2*d)<<7)
   for o in(i+d-1,i+d+1):
    if not o&0x88 and(B[o]*SD<0 or o==EP):m+=[i|o<<7|k<<14 for k in(5,4,3,2)]if o<8 or o>111 else[i|o<<7]
  elif t==2 or t==6:
   for d in(N if t==2 else K):
    o=i+d
    if not o&0x88 and B[o]*SD<=0 and(B[o]or not q):m.append(i|o<<7)
  else:
   for d in(Y if t==3 else H if t==4 else Y+H):
    o=i+d
    while not o&0x88:
     if not B[o] and not q:m.append(i|o<<7)
     elif B[o]*SD<0:m.append(i|o<<7)
     if B[o]:break
     o+=d
 if not q:
  o=112*(SD<0)
  for k,y,r,b,t in((4+o,(5+o,6+o),7+o,1 if SD>0 else 4,6+o),(4+o,(1+o,2+o,3+o),o,2 if SD>0 else 8,2+o)):
   if C&b and B[r]==4*SD and all(not B[x]for x in y)and all(not A(x,-SD)for x in(k,)+y[-2:]):m.append(k|t<<7)
 return m
def MK(m):
 global C,EP,SD
 f=m&127;t=m>>7&127;p=B[f];r=m>>14;oc=C;oe=EP;cap=B[t];cs=rf=rt=-1
 if abs(p)==1 and t==EP and not cap:
  cs=t-16*(p//abs(p));cap=B[cs];B[cs]=0
 B[t]=r*(p//abs(p))if r else p;B[f]=0
 if abs(p)==6 and abs(t-f)==2:
  o=112*(p<0);rf=7*(t>f)+o;rt=3+2*(t>f)+o
  B[rt]=B[rf];B[rf]=0
 if abs(p)==6:C&=-(4+9*(p<0))
 C&=~(D.get(f,0)|D.get(t,0))
 EP=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
 SD=-SD
 return(f,t,p,cap,cs,oc,oe,rf,rt)
def UM(u):
 global C,EP,SD
 f,t,p,cap,cs,oc,oe,rf,rt=u
 B[f]=p;B[t]=cap if cs<0 else 0
 if cs>=0:B[cs]=cap
 if rf>=0:B[rf]=B[rt];B[rt]=0
 C,EP,SD=oc,oe,-SD
def EV():
 s=0
 for i,p in enumerate(B):
  if not p or i&0x88:continue
  t=abs(p);c=min(i&7,7-(i&7))+min(i>>4,7-(i>>4))
  if t==1:z=100+((i>>4)if p>0 else 7-(i>>4))**2*3+c*2
  elif t==6:z=0
  else:z=V[t]+c*(0,0,6,4,2,2)[t]
  s+=z if p>0 else-z
 return s*SD
def O(ms):
 ms.sort(key=lambda m:-V[abs(B[m>>7&127])])
 return ms
NN=0;NB=15000;W=10**6
def SR(a,b,d,pl):
 global NN,QN
 NN+=d>0
 QN+=d<1
 if NN>NB:raise StopIteration
 if QN>1e4 and d<1:return EV()
 if d<1:
  a=max(a,EV())
  if a>=b:return b
 ms=O(G(d<1));bv=-W
 for m in ms:
  u=MK(m)
  if A(B.index(-6*SD),SD):UM(u);continue
  v=-SR(-b,-a,d-1,pl+1)
  UM(u)
  if v>=b:return b
  a=max(a,v);bv=max(bv,v)
 if d<1:return a
 if bv==-W:return-9999+pl if A(B.index(6*SD),-SD) else 0
 return max(a,bv)
def TH(lg):
 global NN,QN
 ms=[m for m in G(0)if S(m)in lg]
 O(ms);bo=ms[0];NN=0;QN=0;d=1
 while 1:
  try:
   bv=-W;nb=bo
   for m in ms:
    u=MK(m)
    if A(B.index(-6*SD),SD):UM(u);continue
    v=-SR(-W,W,d-1,1)
    UM(u)
    if v>bv:bv=v;nb=m
   bo=nb;ms.remove(bo);ms[:0]=[bo];d+=1
  except StopIteration:break
 return [S(m)for m in ms]
while 1:
 g=P("/game",{})
 if g.get("status")=="done":break
 while g.get("status")=="your_move":
  n=g["game"];F(g["fen"]);od=TH(g["legal_moves"]);g={}
  g=next(filter(None,(P("/move",{"game":n,"move":mv})for mv in od)),{})
