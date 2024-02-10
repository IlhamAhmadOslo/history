plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title('Strømproduksjon fra et innstråling areal på 47 kvadratmeter for et år')
y = G['P'] + F['P']


c=[]
for i in y:
    if i  > 0:
        c.append(i)
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title('Strømproduksjon fra et innstråling areal på 47 kvadratmeter for et år')
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')
jan1= y[0:744]
r=[]
for i in jan1:
    if i  > 0:
        r.append(i)
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1750)
x=plt.hist(r, color = "black", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('PV_produksjon') 
plt.title('Varighetskurv til januar med innstrålingsareal på 137 m2')
sum(jan1)
feb= y[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)
sum(feb)
mar1= y[1440:2184]
m=[]
for i in mar1:
    if i  > 0:
        m.append(i)
sum(mar1)
apr= y[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)
sum(apr)
mai= y[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)
sum(mai)
jun= y[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)
sum(jun)
juli= y[4368:5112]
jul=[]
for i in juli:
    if i  > 0:
        jul.append(i)
sum(juli)
aug= y[5112:5856]
au=[]
for i in aug:
    if i  > 0:
        au.append(i)
sum(aug)
sep= y[5856:6576]
o=[]
for i in sep:
    if i  > 0:
        o.append(i)
sum(sep)
okt= y[6576:7320]
ok=[]
for i in okt:
    if i  > 0:
        ok.append(i)
sum(okt)
nov= y[7320:8040]
n=[]
for i in nov:
    if i  > 0:
        n.append(i)
sum(nov)

des= y[8040:8783]
d=[]
for i in des:
    if i  > 0:
        d.append(i)
sum(des)
if 16000 in jan1:
    print bra
if 16000 in jan1:
    print (bra)
    
jan1
if 155 in jan1:
    print (bra)
    
if 155 in jan1:
    print ('bra')
    
if 16000 in jan1:
    print ('bra')
else:
    print('ikke bra')
    
if 16000 in apr:
    print ('bra')
else:
    print('ikke bra')
    
if 16000 in mai:
    print ('bra')
else:
    print('ikke bra')
    
if 16000 in juni:

    print ('bra')
else:
    print('ikke bra')    
    
if 16000 in jun:

    print ('bra')
else:
    print('ikke bra')
    
if 16000 in jul:

    print ('bra')
else:
    print('ikke bra')
    
if 16000 in aug:

    print ('bra')
else:
    print('ikke bra')
    
for t in aug:
    if t>=15999
for t in aug:
    if t>=15999:
        print (bra)
        
for t in jul:
    if t>=15999:
        print (bra)
        
for t in jul:
    if t>=15999:
        print ('bra')
        
for t in jul:
    if t>=15999:
        print (t)
        
sum(jul)
for t in jul:
    if t>=15999:
        t+=t
        print (t)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ma, color = "black", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 137 kvadratmeter for et år")
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ma, color = "black", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 137 kvadratmeter for mai")
S= pd.read_csv("C:/Users/Eier/Downloads/sistesol/s.csv")
S = S.dropna()
S['P'] = S['P'].astype(float)

N= pd.read_csv("C:/Users/Eier/Downloads/no.csv")
N = N.dropna()
N['P'] = N['P'].astype(float)

O= pd.read_csv("C:/Users/Eier/Downloads/sistesol/o.csv")
O = O.dropna()
O['P'] = O['P'].astype(float)

hele = G['P'] + F['P'] + S['P'] + N['P']+ O['P']
jan= hele[0:744]
sum(jan)
feb= hele[744:1440]
sum(feb)
mar= hele[1440:2184]
sum(mar)
apr= hele[2184:2904]
sum(apr)
mai= hele[2904:3648]
sum(mai)
jun= hele[3648:4368]
sum(jun)
juli= hele[4368:5112]
sum(juli)
aug= hele[5112:5856]
sum(aug)
sep= hele[5856:6576]
sum(sep)
okt= hele[6576:7320]
sum(okt)
nov= hele[7320:8040]
sum(nov)
des= hele[8040:8783]
sum(des)
des
des= hele[8040:8759]
sum(des)
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('PV_produksjon') 
plt.title('Varighetskurv til et år')
for t in jul:
    if t>=17499:
        print (t)
        
for t in jul:
    if t>=17000:
        print (t)
        
for t in jul:
    if t>=16000:
        print (t)
        
for t in apr:
    if t>=16000:
        print (t)
        
16385.67+16119.97- sum(apr)
for t in mai:
    if t>=16000:
        print (t)
        
c=[]
for t in mai:
    if t>=16000:
    c.append(t)
c
for t in mai:
    if t>=16000:
c.append(t)
for t in mai:
    if t>=16000:
        c.append(t)
        
c
sum(c)
sum(mai)-sum(c)
for t in apr:
    if t>=16000:
        c.append(t)
        
sum(apr)-sum(c)
sum(apr)
c
k=[]
for t in apr:
    if t>=16000:
        k.append(t)
        
k
sum(apr)-sum(k)
l=[]
for t in jun:
    if t>=16000:
        l.append(t)
        
l
sum(jun)-sum(l)
j=[]
for t in juli:
    if t>=16000:
        j.append(t)
        
j
sum(juli)-sum(j)
i=[]
for t in aug:
    if t>=16000:
        i.append(t)
        
sum(aug)-sum(i)
for t in b:
    if t>=16000:
        i.append(t)    
        
i
len(i)
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('PV_produksjon') 
plt.title('Varighetskurv til et år')
x=[]
for t in b:
    if t>=15900:
        x.append(t)
        
len(x)
x1=[]
for t in b:
    if t>=14900:
        x1.append(t)
        
len(x1)
x11=[]
for t in b:
    if t>=16000:
        x11.append(t)
        
len(x11)

## ---(Sun Jan 22 02:46:25 2023)---
from scipy.integrate import quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# areal 90 m^2
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")
F = F.dropna()
F['P'] = F['P'].astype(float)

h=[]
for i in F['P']:
    if i  == 0:
        h.append(i)


g=[]
for i in F['P']:
    if i  > 0:
        g.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
import seaborn as sns
# areal 90 m^2
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")
F = F.dropna()
F['P'] = F['P'].astype(float)




# Januar
jan= F['P'][0:744]
r=[]
for i in jan:
    if i  > 0:
        r.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(r, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(F['P'], color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")

## ---(Tue Jan 24 02:36:29 2023)---
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")
F = F.dropna()
F['P'] = F['P'].astype(float)

h=[]
for i in F['P']:
    if i  == 0:
        h.append(i)


g=[]
for i in F['P']:
    if i  > 0:
        g.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
import scipy as sp
from scipy.integrate import cumulative_trapezoid
from scipy.integrate import quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# areal 90 m^2
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")
F = F.dropna()
F['P'] = F['P'].astype(float)

h=[]
for i in F['P']:
    if i  == 0:
        h.append(i)


g=[]
for i in F['P']:
    if i  > 0:
        g.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
y = G['P'] + F['P']


c=[]
for i in y:
    if i  > 0:
        c.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')
G= pd.read_csv("C:/Users/Eier/Downloads/sistesol/nord47 ekte.csv")
G = G.dropna()
G['P'] = G['P'].astype(float)
y = G['P'] + F['P']


c=[]
for i in y:
    if i  > 0:
        c.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')
S= pd.read_csv("C:/Users/Eier/Downloads/sistesol/s.csv")
S = S.dropna()
S['P'] = S['P'].astype(float)

N= pd.read_csv("C:/Users/Eier/Downloads/no.csv")
N = N.dropna()
N['P'] = N['P'].astype(float)

O= pd.read_csv("C:/Users/Eier/Downloads/sistesol/o.csv")
O = O.dropna()
O['P'] = O['P'].astype(float)

hele = G['P'] + F['P'] + S['P'] + N['P']+ O['P']
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(b, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
#y=plt.hist(g)
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(b, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")
jan= hele[0:744]
r=[]
for i in jan:
    if i  > 0:
        r.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1800)
x=plt.hist(r, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i januar')
feb= hele[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 12000)
x=plt.hist(f, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i februar')
mar= hele[1440:2184]
m=[]
for i in mar:
    if i  > 0:
        m.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 15000)
x=plt.hist(m, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i mars')
a=[]
for i in apr:
    if i  > 0:
        a.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(a, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i april')
apr= hele[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(a, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i april')
mai= hele[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ma, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i mai')
jun= hele[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ju, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurv til 156 kvadratmeter i juni')
des= hele[8040:8759]
d=[]
for i in des:
    if i  > 0:
        d.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 800)
x=plt.hist(d, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i desember')
nov= hele[7320:8040]
n=[]
for i in nov:
    if i  > 0:
        n.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 6000)
x=plt.hist(n, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i november')
okt= hele[6576:7320]
ok=[]
for i in okt:
    if i  > 0:
        ok.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 11000)
x=plt.hist(ok, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i oktober')
sep= hele[5856:6576]
o=[]
for i in sep:
    if i  > 0:
        o.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 15000)
x=plt.hist(o, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i september')
aug= hele[5112:5856]
au=[]
for i in aug:
    if i  > 0:
        au.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(au, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i august')
juli= hele[4368:5112]
jul=[]
for i in juli:
    if i  > 0:
        jul.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(jul, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i juli')
jun= hele[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ju, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i juni')
mai= hele[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ma, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i mai')
apr= hele[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(a, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i april')

mar= hele[1440:2184]
m=[]
for i in mar:
    if i  > 0:
        m.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 15000)
x=plt.hist(m, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i mars')
feb= hele[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 12000)
x=plt.hist(f, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i februar')
jan= hele[0:744]
r=[]
for i in jan:
    if i  > 0:
        r.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1800)
x=plt.hist(r, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i januar')
jan1= y[0:744]
r=[]
for i in jan1:
    if i  > 0:
        r.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1750)
x=plt.hist(r, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i januar')
feb= y[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 10000)
x=plt.hist(f, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i februar')
mar1= y[1440:2184]
m=[]
for i in mar1:
    if i  > 0:
        m.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 14000)
x=plt.hist(m, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i mars')
apr= y[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(a, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i april')
mai= y[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ma, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i mai')
jun= y[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ju, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i juni')
juli= y[4368:5112]
jul=[]
for i in juli:
    if i  > 0:
        jul.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(jul, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i juli')
aug= y[5112:5856]
au=[]
for i in aug:
    if i  > 0:
        au.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(au, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i august')
sep= y[5856:6576]
o=[]
for i in sep:
    if i  > 0:
        o.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 14000)
x=plt.hist(o, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i september')
okt= y[6576:7320]
ok=[]
for i in okt:
    if i  > 0:
        ok.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 10000)
x=plt.hist(ok, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i oktober')
nov= y[7320:8040]
n=[]
for i in nov:
    if i  > 0:
        n.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 6000)
x=plt.hist(n, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i november')
des= y[8040:8783]
d=[]
for i in des:
    if i  > 0:
        d.append(i)


plt.style.use('seaborn-whitegrid')
plt.ylim(1, 800)
x=plt.hist(d, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i desember ')
S= pd.read_csv("C:/Users/Eier/Downloads/sistesol/s.csv")
S = S.dropna()
S['P'] = S['P'].astype(float)

N= pd.read_csv("C:/Users/Eier/Downloads/no.csv")
N = N.dropna()
N['P'] = N['P'].astype(float)

O= pd.read_csv("C:/Users/Eier/Downloads/sistesol/o.csv")
O = O.dropna()
O['P'] = O['P'].astype(float)

hele = G['P'] + F['P'] + S['P'] + N['P']+ O['P']
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(b, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")
b=[]
for i in hele:
    if i  > 0:
        b.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
c=[]
for i in y:
    if i  > 0:
        c.append(i)

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")