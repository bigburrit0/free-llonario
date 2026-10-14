from scene import *
img=Image.new('RGB',(W,Hh)); d=ImageDraw.Draw(img)
R(d,0,0,W,Hh,'#1A0F3D')
# light beams (dithered)
for k,(bx,ang) in enumerate([(60,0.35),(160,0),(260,-0.35)]):
    for y in range(0,120):
        cxb=bx+ang*(120-y)*-1; half=6+y*0.18
        for x in range(int(cxb-half),int(cxb+half)):
            if 0<=x<W and (x+y)%2==0: img.putpixel((x,y),'#3A1F7A')
# floor ellipse
for y in range(96,134):
    for x in range(W):
        e=((x-160)/150)**2+((y-118)/18)**2
        if e<1: img.putpixel((x,y),'#3A1F7A' if e>0.55 else ('#4B2A94' if (x+y)%2 else '#3A1F7A'))
        if 0.92<e<1: img.putpixel((x,y),'#FFD43B')
# Fran monitor
R(d,128,10,192,52,'#C6C5D6'); R(d,130,12,190,50,'#12111A'); R(d,132,14,188,48,'#1E4F9A')
for y in range(14,48,2): R(d,132,y,188,y+1,'#2A5FB0')
R(d,148,24,154,30,'#A8DBFF'); R(d,166,24,172,30,'#A8DBFF')
R(d,150,38,170,40,'#A8DBFF'); R(d,148,36,150,38,'#A8DBFF'); R(d,170,36,172,38,'#A8DBFF')
R(d,156,52,164,58,'#7C7B91'); R(d,146,58,174,60,'#7C7B91')
text(img,133,62,'FRAN 2.0','#FFD43B')
# contestant podium with Cami + dragon
R(d,28,96,60,124,'#E8772E'); R(d,28,96,60,99,'#FFB765'); R(d,58,96,60,124,'#A3471B')
blit(img,CAMI,36,72); blit(img,DRAGON,14,64); blit(img,FLAME,28,69)
# lifelines
for i,(lx,l) in enumerate([(232,'F'),(254,'L'),(276,'A')]):
    d.ellipse([lx,10,lx+18,24],fill='#12111A',outline='#FFD43B'); text(img,lx+7,14,l,'#FFD43B')
text(img,226,30,'COMODINES','#C6C5D6')
# elevator display
box(d,262,44,316,136)
text(img,272,49,'PISO','#C6C5D6')
for i,fl in enumerate(range(8,0,-1)):
    y=60+i*9; cur=(fl==1)
    if cur: R(d,267,y-1,311,y+8,'#E8772E')
    col='#12111A' if cur else ('#7C7B91' if fl>1 else '#F5F4FA')
    text(img,270,y,str(fl),col)
    lab={8:'META',1:'BPS'}.get(fl,'- - -')
    text(img,280,y,lab,col)
# question capsule
def capsule(x0,y0,x1,y1,fill,edge):
    m=(y1-y0)//2
    for y in range(y0,y1):
        o=abs(y-(y0+m));
        R(d,x0+o,y,x1-o,y+1,edge)
    for y in range(y0+1,y1-1):
        o=abs(y-(y0+m))
        R(d,x0+o+2,y,x1-o-2,y+1,fill)
R(d,0,145,W,146,'#FFD43B'); R(d,0,163,W,164,'#FFD43B')
capsule(8,128,256,148,'#12111A','#C6C5D6')
text(img,24,135,'¿QUÉ AUTOMATIZÓ EL EQUIPO DE INNOVACIÓN?','#F5F4FA')
answers=[('A','LAS EXCUSAS',0),('B','DOCS BPS Y DGI',2),('C','LAVAR TAZAS',0),('D','TODO EN 3 COPIAS',0)]
for i,(L,t,st) in enumerate(answers):
    x0=8+(i%2)*128; y0=150+(i//2)*14
    fill={0:'#12111A',1:'#E8772E',2:'#3F8A3C'}[st]
    capsule(x0,y0,x0+122,y0+13,fill,'#C6C5D6')
    text(img,x0+10,y0+3,L+':','#FFD43B' if st==0 else '#12111A')
    text(img,x0+24,y0+3,t,'#F5F4FA')
    if st==2:
        for p in [(108,7),(109,8),(110,9),(111,8),(112,7),(113,6),(114,5)]: d.point((x0+p[0],y0+p[1]-1),'#F5F4FA')
img.save('s2.png'); img.resize((W*4,Hh*4),Image.NEAREST).save('s2x4.png')
