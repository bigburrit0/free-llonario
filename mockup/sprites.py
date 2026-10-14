from PIL import Image, ImageColor
from functools import lru_cache
_o=Image.Image.putpixel
_g=lru_cache(None)(ImageColor.getrgb)
def _p(self,xy,v): return _o(self,xy,_g(v) if isinstance(v,str) else v)
Image.Image.putpixel=_p
PAL={'o':'#2B1B2E','s':'#F3CFA9','S':'#D19A6A','y':'#F2D27A','Y':'#C99A4A','b':'#2A2230','B':'#4A4058',
'h':'#6B4226','H':'#9A6438','i':'#4E9A5A','k':'#1B1620','p':'#E08A8A','r':'#C0404A','n':'#1E2A4A','j':'#3D6EA8',
'w':'#F5F4FA','e':'#A0623A','z':'#24222C','q':'#3B3946','a':'#D9A07A','A':'#A87250','G':'#7A4A28','t':'#5A3218',
'x':'#3B2A20','m':'#C3CCD8','M':'#6E7A8C','c':'#5CF2FF','l':'#2B2F3A','v':'#D4E34A','g':'#3F8A3C','L':'#95C653','f':'#FF8A3D','F':'#FFD43B'}
def H(inner,l='..o',r='o..'): return l+inner+r
LU=["......oooo......","....ooyyyyoo....","...oyyyyyyyyo...",H("yyYyyyyyyy"),H("yYssssssyy"),H("yssssssssy"),
H("yssississy"),H("yssssssssy"),H("yYssppssYy"),H("yyYssssYyy"),H("yyyossoyyy"),H("yonnnnnnoy"),H("yonnnnnnoy"),H("yonnnnnnoy"),
"...onnnnnnnno...","...osnnnnnnso...","...osnnnnnnso...","....onnnnnno....","....ojjjjjjo....","....ojjjjjjo....",
"....ojjoojjo....","....ojjoojjo....","....owwoowwo....","....oooooooo...."]
ANDREA=["......oooo......","....oobbbboo....","...obbbbbbbbo...",H("bbBbbbbbbb"),H("bbsssssssb"),H("bsssssssbb"),
H("bsksssksbb"),H("bsssssssbb"),H("essrrrssbb"),H("ebsssssbbb"),H("bbbossobbb"),H("bzzwwwwzzb"),H("bzzzwwzzzb"),H("bzzzwwzzzb"),
"...ozzzwwzzzo...","...oszzzzzzso...","...ozzzzzzzzo...","....ozzzzzzo....","....oqqqqqqo....","....oqqooqqo....",
"....oqqooqqo....","....oqqooqqo....","....oxxooxxo....","....oooooooo...."]
CAMI=["......oooo......","....oobbbboo....","...obbbbbbbbo...",H("bbbbbbbBbb"),H("bbbbsssssb"),H("bbsssssssb"),
H("btttsstttb"),H("btktsstktb"),H("btttsstttb"),H("bbssrrssbb"),H("bbbossobbb"),H("aaazzzzaaa"),H("aaazzzzaaa"),H("AaazzzzaaA"),
H("AaazzzzaaA"),H("saazzzzaas"),"...oaGGFGGGao...","...oazzzzzzao...","....ozzzzzzo....","....ozzzzzzo....",
"....ozzoozzo....","....ozzoozzo....","....oxxooxxo....","....oooooooo...."]
VALE=["....oooooooo....","...ohhhhhhhho...",H("hhHhhhhhhh"),H("hhhhhhhhhh"),H("mmmmmmmmmm"),H("mMMMMMMMMm"),
H("mMcMMMMcMm"),H("mMMMMMMMMm"),H("mmmmmmmmmm"),H("mmmllllmmm"),H("ommmmmmmmo"),"......oMMo......","...oommmmmmoo...",
"..oMommmmmmoMo..","..oMomwcmmmoMo..","..oMommmmmmoMo..","..oMoMMMMMMoMo..","..ocoommmmooco..","....omMooMmo....",
"....omMooMmo....","....omMooMmo....","....omMooMmo....","....oMMooMMo....","....oooooooo...."]
NACHO=["......oooo......","....oohhhhoo....","...ohhhhhhhho...",H("hhHhhhhhhh"),H("hssssssssh"),H("ssssssssss"),
H("ssksssskss"),H("ssssssssss"),H("ssssrrssss"),H("SssssssssS"),"....ooossooo....",H("wwwvvvvwww"),H("wwwwwwwwww"),H("wwwwwwwwww"),
H("swwwwwwwws"),"...owwwwwwwwo...","...onnnnnnnno...","....onnnnnno....","....onnoonno....","....ossoosso....",
"....ossoosso....","....owwoowwo....","....oxxooxxo....","....oooooooo...."]
DRAGON=["..........o...",".........ogo..","....oo..oggoo.","...ogggoggggko","..ogLggggggggo",".oggLLggggfooo",
"ogggLLLgggo...",".ooggggggo....","...ogo.ogo....","...oo...oo...."]
FLAME=["..F.","fFF.","ffFF","fF.."]
for n,s in [('LU',LU),('ANDREA',ANDREA),('CAMI',CAMI),('VALE',VALE),('NACHO',NACHO),('DRAGON',DRAGON)]:
    for i,r in enumerate(s):
        assert len(r)==len(s[0]),(n,i,r,len(r))
def blit(img,spr,x,y,flip=False,k=1):
    for yy,row in enumerate(spr):
        if flip: row=row[::-1]
        for xx,c in enumerate(row):
            if c!='.':
                for a in range(k):
                    for b in range(k):
                        img.putpixel((x+xx*k+a,y+yy*k+b),PAL[c])
