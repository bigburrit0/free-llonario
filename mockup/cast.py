from scene import *
img=Image.new('RGB',(W,Hh)); d=ImageDraw.Draw(img)
R(d,0,0,W,Hh,'#1A0F3D')
for y in range(0,Hh,2):
    for x in range((y//2)%2,W,4): img.putpixel((x,y),'#22144D')
text(img,8,6,'ELENCO','#FFD43B'); text(img,52,6,'- SPRITES 16X24 CON SELECTIVE OUTLINE','#7C7B91')
cast=[('CAMI',CAMI,'FAN DE','DRAGONES'),('VALENTINO',VALE,'MODO','ROBOT'),('LU',LU,'SUZUKI','ROJO'),('ANDREA',ANDREA,'AROS DE','MADERA'),('NACHO',NACHO,'PELOTA','XXL')]
for i,(n,s,a,b) in enumerate(cast):
    cx=32+i*64
    d.ellipse([cx-20,86,cx+20,94],fill='#3A1F7A')
    blit(img,s,cx-24,18,k=3)
    text(img,cx-width(n)//2,100,n,'#F5F4FA')
    text(img,cx-width(a)//2,111,a,'#C6C5D6'); text(img,cx-width(b)//2,120,b,'#C6C5D6')
R(d,0,132,W,133,'#3A1F7A')
text(img,8,138,'PROPS','#FFD43B')
blit(img,DRAGON,10,152,k=2); text(img,8,170,'DRAGÓN','#C6C5D6')
ball(img,d,82,158,11); text(img,74,172,'XXL','#C6C5D6')
car(img,d,118,143); text(img,114,170,'EL SUZUKI','#C6C5D6')
# towers mini
tower1(img,d,190,142,222,168); tower2(img,d,232,144,256,168)
text(img,180,170,'TORRE 1','#FFB765'); text(img,226,170,'TORRE 2','#A8DBFF')
R(d,274,140,316,176,'#12111A')
for i,c in enumerate(['#E8772E','#3D8FE0','#3F8A3C','#FFD43B','#E23A3A','#F5F4FA']):
    R(d,278+(i%3)*12,146+(i//3)*13,287+(i%3)*12,155+(i//3)*13,c)
img.save('s3.png'); img.resize((W*4,Hh*4),Image.NEAREST).save('s3x4.png')
