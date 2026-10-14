import re,sys,glob
NARROW={'I':3,' ':2,'!':1,'¡':1,'.':1,':':1,',':2,'-':3,'"':3,'>':3}
def gw(ch):
    ch={'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U','Ñ':'N'}.get(ch,ch)
    return NARROW.get(ch,5)
def width(s):
    s=s.upper(); return sum(gw(c)+1 for c in s)-1 if s else 0
def wrap(s,maxw):
    words=s.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if width(t)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
issues=[]
for f in sorted(glob.glob('guion-humor/0[2-5]*.md')):
    B='03-' in f
    for n,line in enumerate(open(f,encoding='utf-8'),1):
        L=line.rstrip()
        opt=re.match(r'- \*\*[A-D]\)\*\* (.+?) · ',L)
        if opt:
            t=opt.group(1); lines=wrap(t,130)
            if len(lines)>2 or len(t)>36: issues.append((f.split('/')[-1],n,'OPCIÓN',len(t),len(lines),t))
            continue
        if L.startswith('**Pregunta'):
            for q in re.findall(r'«(.+?)»',L):
                if len(q)>60: issues.append((f.split('/')[-1],n,'PREGUNTA',len(q),0,q))
            continue
        if L.startswith('**Tarjeta') or L.startswith('**Zócalo'):
            for q in re.findall(r'«(.+?)»',L):
                if len(q)>140: issues.append((f.split('/')[-1],n,'TARJETA',len(q),0,q))
            continue
        for q in re.findall(r'«(.+?)»',L):
            if B and '[INTERTÍTULO]' in L:
                if len(q)>40: issues.append((f.split('/')[-1],n,'INTERTÍTULO',len(q),0,q))
            elif L.startswith('|'):
                lines=wrap(q,262)
                if len(lines)>2: issues.append((f.split('/')[-1],n,'DIÁLOGO',len(q),len(lines),q))
for i in issues: print(i)
print('total issues',len(issues))
