import math
from PIL import Image, ImageDraw
from sprites import *
from font import text, width
W,Hh=320,180
O1=['#4A1F0E','#A3471B','#E8772E','#FFB765']; B2=['#0F1E45','#1E4F9A','#3D8FE0','#A8DBFF']
N=['#12111A','#3B3A4F','#7C7B91','#C6C5D6','#F5F4FA']
def R(d,x0,y0,x1,y1,c): d.rectangle([x0,y0,x1-1,y1-1],fill=c)
def sky(img,cols,y0,y1):
    n=len(cols)-1;
    for y in range(y0,y1):
        t=(y-y0)/(y1-y0)*n; i=min(int(t),n-1); f=t-i
        for x in range(W):
            th=[[0,.5],[.75,.25]][y%2][x%2]
            img.putpixel((x,y),cols[i+1] if f>th+0.12 else cols[i])
def cloud(d,x,y,w):
    R(d,x+4,y,x+w-4,y+3,'#FFFFFF');R(d,x,y+3,x+w,y+7,'#FFFFFF');R(d,x+2,y+7,x+w-2,y+8,'#DCEBFA')
def tower1(img,d,x0,y0,x1,y1):
    side=x1-14
    R(d,x0,y0,side,y1,O1[1]); R(d,side,y0+3,x1,y1,'#6E2A12')
    # windows
    for y in range(y0+6,y1-6,5):
        for i,x in enumerate(range(x0+3,side-3,5)):
            c=O1[3] if (i%3!=1) else O1[2]
            if (x*7+y*3)%23==0: c='#FFF1C9'
            R(d,x,y,x+3,y+3,c)
        for x in range(side+2,x1-2,4): R(d,x,y,x+2,y+3,O1[1])
    for i,x in enumerate(range(x0+3,side-3,5)):
        if i%3==1: R(d,x,y0+4,x+3,y1,O1[2])  # stripe
    R(d,x0,y0,side,y0+4,O1[0]); R(d,x0+2,y0-3,side-2,y0,O1[1]); R(d,side,y0,x1,y0+3,'#4A1F0E')
    # selective outline
    R(d,x0-1,y0,x0,y1,O1[2]); R(d,x1,y0+3,x1+1,y1,O1[0]); R(d,x0+2,y0-4,side-2,y0-3,O1[2])
    R(d,x0-1,y1-8,x1+1,y1,'#3B3A4F'); R(d,x0+8,y1-7,x0+22,y1,'#A8DBFF')
def tower2(img,d,x0,y0,x1,y1):
    w=x1-x0; rx=w/2; cx=x0+rx; ry=5
    for x in range(x0,x1):
        t=(x+0.5-x0)/w; b=math.cos((t-0.36)*math.pi*1.05)
        idx=3 if b>0.85 else 2 if b>0.45 else 1 if b>-0.1 else 0
        dx=(x+0.5-cx)/rx; e=ry*math.sqrt(max(0,1-dx*dx))
        top=int(y0+e)
        for y in range(top,y1):
            c=B2[idx]
            band=(y-int(e)-y0)%6
            if band in (3,4): c=B2[max(idx-1,0)] if idx>0 else '#0A1530'
            img.putpixel((x,y),c)
        # cap
        for y in range(int(y0-e),top): img.putpixel((x,y),B2[3] if idx>=2 else B2[2])
        img.putpixel((x,int(y0-e)-1),B2[0] if idx<2 else B2[2])
    R(d,x0-1,y0,x0,y1,B2[1]); R(d,x1,y0,x1+1,y1,B2[0])
    # crown ring
    for x in range(x0,x1):
        dx=(x+0.5-cx)/rx; e=ry*math.sqrt(max(0,1-dx*dx)); img.putpixel((x,int(y0+e)+1),B2[0])
    R(d,x0-1,y1-8,x1+1,y1,'#3B3A4F'); R(d,int(cx)-8,y1-7,int(cx)+8,y1,'#A8DBFF')
def city(d,y1):
    import random; random.seed(3)
    x=0
    while x<W:
        w=random.randint(8,20); h=random.randint(8,30); R(d,x,y1-h,x+w,y1,'#8FB3D9')
        for yy in range(y1-h+3,y1-2,4):
            for xx in range(x+2,x+w-2,4): d.point((xx,yy),'#B5CFEA')
        x+=w+random.randint(0,3)
def car(img,d,x,y,crash=True):
    Rr=['#5A0E14','#A3202A','#E23A3A','#FF8A80']
    # body (facing left), x..x+46, y..y+22
    R(d,x+4,y+10,x+46,y+19,Rr[2]); R(d,x+12,y+2,x+38,y+10,Rr[2])
    R(d,x+14,y+4,x+24,y+10,'#A8DBFF'); R(d,x+26,y+4,x+36,y+10,'#7FB6E6')
    R(d,x+12,y+2,x+38,y+3,Rr[3]); R(d,x+4,y+10,x+46,y+11,Rr[3])
    R(d,x+4,y+17,x+46,y+19,Rr[1]); R(d,x+25,y+11,x+26,y+17,Rr[1])
    R(d,x+40,y+12,x+44,y+15,'#FFD43B')  # rear light
    if crash:
        for i,yy in enumerate(range(y+9,y+19)):
            R(d,x+2+(i%3),yy,x+6+(i%2),yy+1,Rr[1])
        R(d,x+2,y+12,x+5,y+15,'#FFF1C9')
    for wx in (x+8,x+34):
        R(d,wx,y+16,wx+9,y+23,'#1B1620'); R(d,wx+3,y+18,wx+6,y+21,'#7C7B91')
    # outline selective (dark bottom/right)
    R(d,x+4,y+19,x+46,y+20,Rr[0]); R(d,x+46,y+10,x+47,y+19,Rr[0]); R(d,x+38,y+3,x+39,y+10,Rr[0])
def ball(img,d,cx,cy,r):
    for y in range(-r,r+1):
        for x in range(-r,r+1):
            if x*x+y*y<=r*r:
                c='#D4E34A'
                if (x+r*0.35)**2+(y+r*0.35)**2<(r*0.45)**2: c='#EEF58A'
                if x*x+y*y>(r-1.5)**2: c='#7E8A1E' if x+y>0 else '#A9B830'
                img.putpixel((cx+x,cy+y),c)
    for yy in range(-r,r+1):
        for xx in range(-r,r+1):
            if xx*xx+yy*yy<(r-1)**2:
                for sgn in (-1,1):
                    ox=cx+sgn*1.3*r; dd=math.hypot(cx+xx-ox,yy)
                    if abs(dd-1.05*r)<0.6: img.putpixel((cx+xx,cy+yy),'#FFFFFF')
def box(d,x0,y0,x1,y1):
    R(d,x0,y0,x1,y1,'#F5F4FA'); R(d,x0+1,y0+1,x1-1,y1-1,'#12111A'); R(d,x0+2,y0+2,x1-2,y1-2,'#3B3A4F'); R(d,x0+3,y0+3,x1-3,y1-3,'#12111A')

# ---------- SCENE 1 ----------
img=Image.new('RGB',(W,Hh)); d=ImageDraw.Draw(img)
sky(img,['#3D8FE0','#7FB8EE','#A8DBFF','#FFE2B8'],0,118)
cloud(d,20,18,26); cloud(d,150,10,34); cloud(d,268,30,22)
city(d,118)
tower1(img,d,30,26,92,120)
tower2(img,d,196,20,252,120)
# ground
R(d,0,118,W,180,'#C6C5D6')
for y in range(122,180,6): R(d,0,y,W,y+1,'#A9A8BC')
for y in range(118,180,6):
    for x in range((y//6)%2*8,W,16): R(d,x,y,x+1,y+6,'#A9A8BC')
R(d,0,118,W,120,'#7C7B91')
# plants
for px in (6,104,172,292):
    R(d,px,108,px+12,118,'#3B3A4F');
    for i in range(6): R(d,px+1+i*2,100+(i%2)*3,px+3+i*2,110,'#3F8A3C' if i%2 else '#95C653')
# portico + columns
R(d,110,74,186,80,'#C6C5D6'); R(d,110,80,186,82,'#7C7B91'); R(d,110,73,186,74,'#F5F4FA')
for cx in (124,170):
    R(d,cx,82,cx+8,134,'#E4E3EE'); R(d,cx+6,82,cx+8,134,'#9C9BB0'); R(d,cx,82,cx+1,134,'#FFFFFF')
    R(d,cx-1,132,cx+9,135,'#7C7B91')
# car crashed into left column
car(img,d,131,110)
# smoke + stars
for (sx,sy,r) in [(136,104,4),(141,98,3),(134,94,2)]:
    d.ellipse([sx-r,sy-r,sx+r,sy+r],fill='#E4E3EE',outline='#9C9BB0')
for (sx,sy) in [(118,92),(130,86),(140,90)]:
    for p in [(0,-2),(0,-1),(0,0),(0,1),(0,2),(-2,0),(-1,0),(1,0),(2,0)]: d.point((sx+p[0],sy+p[1]),'#FFD43B')
# characters (feet at y=134)
blit(img,LU,182,111,flip=True)
text(img,190,100,'!',  '#E23A3A','#12111A');
blit(img,CAMI,44,111); blit(img,DRAGON,58,98,flip=True); blit(img,FLAME,73,103)
blit(img,VALE,72,111)
blit(img,ANDREA,214,111,flip=True)
blit(img,NACHO,246,111,flip=True); ball(img,d,270,122,11)
# HUD
box(d,4,4,62,18); text(img,9,8,'PISO 1','#FFD43B')
box(d,256,4,316,18); text(img,261,8,'MATES 3','#95C653')
# dialog
box(d,6,140,314,176)
R(d,11,145,41,171,'#3A1F7A')
blit(img,LU[:12],12,146,k=2) if False else None
# portrait: head crop scaled 2x
for yy,row in enumerate(LU[1:13]):
    for xx,c in enumerate(row[2:14]):
        if c!='.': d.rectangle([14+xx*2,146+yy*2,15+xx*2,147+yy*2],fill=PAL[c])
text(img,48,147,'LU','#E8772E')
text(img,48,159,'¿QUIÉN DEJÓ ESA COLUMNA AHÍ?','#F5F4FA')
text(img,302,166,'▼','#FFD43B')
img.save('s1.png'); img.resize((W*4,Hh*4),Image.NEAREST).save('s1x4.png')
