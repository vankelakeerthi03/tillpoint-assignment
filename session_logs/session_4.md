1 / 32
  You
"""Sa les repo rts fo r the 
shop ow ne r."""
from datetime 
importdatetime,timedelta,timezone
from .importdb
defday_bounds_utc(day,utc_offset_m 
inutes=0):
"""TheUTC 
instantsatwhichashop-localcalendardaystarts
a n d e n d s . d a y is 'Y Y Y 
Y -M M -D D ' ." " "
s t a r t = d a t e t im e . s 
t r p t im e ( d a y , "% Y -% 
m -
% d " ) . r e p l a c e ( t z i 
n f o = t im e z o n e . u t c 
)
start+= timedelta(m 
inutes=utc_offset_m inutes)
returndb.to_iso(start),db.to_iso(start+ 
timedelta(days=1))
defdaily_sales(conn,day,utc_offset_m 
inutes=0):
" " "M o n e y re c e iv e d o 
n o n e s h o p - lo c a l d a 
y , a n d h ow m a n y
orders itcame from ."""
start,end=day_bounds_utc(day,utc_offset_m 
inutes)
row = conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)AS revenue,
C O U N T ( D I S T IN C T o r 
d e r _ i d ) A S o r d e r s "
"FROM paymentsWHERE 
received_at>=?AND
re c e iv e d _ a t < ? " ,
(start,end),
) . fe tc h o n e ( )
re tu rn {"day" :day 
,"revenue_cen ts" : row 
["revenue"],"o rde rs" :
row ["orders"]}
deftop_products(conn,lim it=5):
"""Bestsellersbyunits,countingorders 
thatwerepaidor
sh ipped ."""
row s = conn .execu te (
"SELECT i.sku,SUM 
(i.qty)ASunits,SUM (i.qty*
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
t i l lp o in (4 )
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
1/32

2 / 32
  i.un it_p rice_cen ts)AS g 
ross_cen ts"
" F R O M o r d e r _ i t e m s 
i J O IN o r d e r s o O N o . 
i d = i . o r d e r _ i d "
"WHEREo.status IN 
('paid','shipped')GROUPBY i.sku
O R D E R B Y u n i t s D E S C 
, i . s k u L IM I T ? " ,
(lim it,),
).fe tcha ll()
re tu rn [d ic t ( r ) fo r r 
in row s ]
ChatGPT
You
firsterror thesukova liga
ChatGPT
You
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
78-
79-
8 0 - i f _ _ n am e _ _ = = " 
_ _m a in _ _ " :
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
1080)
d e f te s t_ o u t_ o f_ s to 
c k ( s e l f ) :
w 
ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te 
("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
de f tes t_paym en t_m a rks_o 
rde r_pa id (se lf):
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
      
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
2/32

3 / 32
 o r d e r = s e l f . a p p . 
o r d e r s . c r e a t e ( " a 
n a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app 
.hand le ("PO ST ",
" /w e b h o o k s / p a y m e 
n t s " , {
" id " : " e v t _ 1 " , " t y 
p e " : " p a ym e n t . s u c 
c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l 
( ( s t a t u s , p a y lo a d 
[ " s t a t u s " ] ) , ( 2 0 0 
, " p a id " ) )
d e f t e s t _ c a n c e l_ p 
a id _ o r d e r _ r e s t o c 
k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 2 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o rd e r [ " id " ] , " am o u 
n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
d e f t e s t _ c a n c e l_ p 
e n d in g _ o r d e r _ r e s 
t o c k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
1)
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
se lf.assertEqua l(se lf.app 
.orders.get(order["id"])["status"],
" c a n c e l le d " )
d e f te s t_ d a i ly _ s a le 
s ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 
2 5 , 3 , 1 0 , 1 2 , 0 , t z i 
n f o = t im e z o n e . u t c 
)
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 3 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } , 
n o w = n o o n )
s e lf .a s s e r tE q u a l( 
re p o r ts .d a i ly_ s a le s 
(s e lf .c o n n , "2 0 2 5 -0 
3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 
,
"orders":1})
d e f t e s t _ p r ic e _ c h 
a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( 
" P U T " , " / p r o d u c t s 
/M U G " , { " p r i c e _ c e 
n t s " :
1500})
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
3/32

4 / 32
  s e l f . a s s e r t E q u a 
l ( s e l f . a p p . c a t a l 
o g . g e t _ p r o d u c t ( 
"M U G " ) . p r i c e _ c e n 
t
s,1500)
d e f t e s t _ c o u p o n _ r 
e d u c e s _ t a x a b le _ am 
o u n t ( s e l f ) :
o rde r= se lf.app .o rde rs .c 
rea te (
"ana",
[ ( "M U G " , 1 ) ] ,
reg ion="CA",
coupon_code="TEN "
)
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],1200 )
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
reports l9na
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
f r o m t i l l p o i n t im p 
o r t d b , r e p o r t s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
     
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
4/32

5 / 32
 f r o m t i l l p o i n t . a 
p i im p o r t A p p
from tillpoint.catalog 
importOutOfStock
c lassO rderDeskTest(un 
ittest.TestCase):
d e f s e tU p ( s e l f ) :
se lf.conn = db .connec t()
se lf.app = App (se lf.conn )
s e l f . a p p . c a t a l o g 
. a d d _ p r o d u c t ( "M U 
G " , "M u g " , 1 2 0 0 ,
stock=10)
se lf.app .ca ta log .add_p 
roduc t("TEE","T-sh irt",2500 ,
stock=3)
self.conn.execute("INSERT 
INTOcoupons(code,kind,value)
VALUES ('TEN ','percent',10)")
deftest_order_totals_w 
ith_tax(self):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 2 ) , ( " 
T E E " ,
1)],reg ion="CA")
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],4900 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],355 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],5255 )
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . s t o c k , 8 )
de f tes t_coupon_ takes_ 
ten_pe rcen t(se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] ,
coupon_code="TEN ")
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1080 )
d e f te s t_ o u t_ o f_ s to 
c k ( s e l f ) :
w 
ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te 
("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
de f tes t_paym en t_m a rks_o 
rde r_pa id (se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app 
.hand le ("PO ST ",
" /w e b h o o k s / p a y m e 
n t s " , {
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
5/32

6 / 32
 " id " : " e v t _ 1 " , " t y 
p e " : " p a ym e n t . s u c 
c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l 
( ( s t a t u s , p a y lo a d 
[ " s t a t u s " ] ) , ( 2 0 0 
, " p a id " ) )
d e f t e s t _ c a n c e l_ p 
a id _ o r d e r _ r e s t o c 
k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 2 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o rd e r [ " id " ] , " am o u 
n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
d e f t e s t _ c a n c e l_ p 
e n d in g _ o r d e r _ r e s 
t o c k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
1)
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
se lf.assertEqua l(se lf.app 
.orders.get(order["id"])["status"],
" c a n c e l le d " )
d e f te s t_ d a i ly _ s a le 
s ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 
2 5 , 3 , 1 0 , 1 2 , 0 , t z i 
n f o = t im e z o n e . u t c 
)
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 3 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } , 
n o w = n o o n )
s e lf .a s s e r tE q u a l( 
re p o r ts .d a i ly_ s a le s 
(s e lf .c o n n , "2 0 2 5 -0 
3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 
,
"orders":1})
d e f t e s t _ d a i l y _ s a 
l e s _ i n d i a _ t im e z o 
n e ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
p a y m e n t _ t im e = d a t 
e t im e ( 2 0 2 5 , 3 , 9 , 1 
9 , 0 ,
t z i n f o = t im e z o n e . 
u t c )
se lf.app .paym en ts .hand 
le_even t(
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
6/32

7 / 32
 {
" id " : " e v t_ in d ia " ,
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
},
n o w = p a y m e n t _ t im e 
,
)
se lf.asse rtEqua l(
r e p o r t s .d a i ly _ s a 
le s ( s e l f .c o n n , " 2 0 
2 5 - 0 3 - 1 0 " ,
utc_offset_m inutes=330),
{"day":"2025-03-10","revenue_cents":1200 
,"orders":
1},
)
d e f t e s t _ p r ic e _ c h 
a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( 
" P U T " , " / p r o d u c t s 
/M U G " , { " p r i c e _ c e 
n t s " :
1500})
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . p r i c e _ c e n t
s,1500)
d e f t e s t _ c o u p o n _ r 
e d u c e s _ t a x a b le _ am 
o u n t ( s e l f ) :
o rde r= se lf.app .o rde rs .c 
rea te (
"ana",
[ ( "M U G " , 1 ) ] ,
reg ion="CA",
coupon_code="TEN "
)
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],1200 )
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
7/32

ChatGPT
You
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
{"day":"2025-03-10","revenue_cents":1200 
,"orders":1},
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^
)
^
A s s e r t io n E r ro r : { 
'd a y ' : '2 0 2 5 -0 3 - 10 ' 
, ' re v e n u e _ c e n ts ' : 
0 , 'o rd e rs ' :
0}!= 
{'day':'2025-03-10','revenue_cents':1200,'orders':1}
- {'day ': '2025 -03 -10 ', 'o 
rde rs ':0 , 'revenue_cen ts 
':0 }
?^
+ 
{'day':'2025-03-10','orders':1,'revenue_cents':1200}
? ^+++
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
FAILED (failures=1)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
"""Sa les repo rts fo r the 
shop ow ne r."""
from datetime 
importdatetime,timedelta,timezone
from .importdb
defday_bounds_utc(day,utc_offset_m 
inutes=0):
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
8 / 32
      
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
8/32

"""TheUTC 
instantsatwhichashop-localcalendardaystarts
a n d e n d s . d a y is 'Y Y Y 
Y -M M -D D ' ." " "
s t a r t = d a t e t im e . s 
t r p t im e ( d a y , "% Y -% 
m -
% d " ) . r e p l a c e ( t z i 
n f o = t im e z o n e . u t c 
)
start-= timedelta(m 
inutes=utc_offset_m inutes)
returndb.to_iso(start),db.to_iso(start+ 
timedelta(days=1))
defdaily_sales(conn,day,utc_offset_m 
inutes=0):
" " "M o n e y re c e iv e d o 
n o n e s h o p - lo c a l d a 
y , a n d h ow m a n y
orders itcame from ."""
start,end=day_bounds_utc(day,utc_offset_m 
inutes)
row = conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)AS revenue,
C O U N T ( D I S T IN C T o r 
d e r _ i d ) A S o r d e r s "
"FROM paymentsWHERE 
received_at>=?AND
re c e iv e d _ a t < ? " ,
(start,end),
) . fe tc h o n e ( )
re tu rn {"day" :day 
,"revenue_cen ts" : row 
["revenue"],"o rde rs" :
row ["orders"]}
deftop_products(conn,lim it=5):
"""Bestsellersbyunits,countingorders 
thatwerepaidor
sh ipped ."""
row s = conn .execu te (
"SELECT i.sku,SUM 
(i.qty)ASunits,SUM (i.qty*
i.un it_p rice_cen ts)AS g 
ross_cen ts"
" F R O M o r d e r _ i t e m s 
i J O IN o r d e r s o O N o . 
i d = i . o r d e r _ i d "
"WHEREo.status IN 
('paid','shipped')GROUPBY i.sku
O R D E R B Y u n i t s D E S C 
, i . s k u L IM I T ? " ,
(lim it,),
).fe tcha ll()
re tu rn [d ic t ( r ) fo r r 
in row s ]
ChatGPT
9 / 32
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
9/32

You
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^
)
^
A s s e r t io n E r ro r : { 
'd a y ' : '2 0 2 5 -0 3 - 10 ' 
, ' re v e n u e _ c e n ts ' : 
0 , 'o rd e rs ' :
0}!= 
{'day':'2025-03-10','revenue_cents':1200,'orders':1}
- {'day ': '2025 -03 -10 ', 'o 
rde rs ':0 , 'revenue_cen ts 
':0 }
?^
+ 
{'day':'2025-03-10','orders':1,'revenue_cents':1200}
? ^ +++
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
FAILED (failures=1)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
-v
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
10 / 32
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
10/32

11 / 32
 You
 ------------------
Ran10 tests in0.007s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
s .p y
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
e n t % g i t c o m m i t - m " 
F i x d a i l y s a l e s t im 
e z o n e o f f s e t "
[m a i n a 7 9 d a 3 9 ] F i x 
d a i l y s a l e s t im e z o 
n e o f f s e t
2 fileschanged,19 
insertions(+),1deletion(-)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
am oun t_cen ts"],db .to_ iso 
(now o rdb .u tcnow ())),
)
iforder["status"]== "pend 
ing"and
se lf.pa 
id_cents(order["id"])>= 
order["tota l_cents"]:
self.conn.execute("UPDATEordersSETstatus= 
'paid'
WHERE id=?",(order["id"],))
re tu rn "p a id "
re tu rn o rd e r [ " s ta tu s 
" ]
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
      
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
11/32

12 / 32
  d e f p a id _ c e n t s ( s 
e l f , o r d e r _ id ) :
row = se lf.conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
"],120)
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
-v
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e ) ...FA IL
================================================
======================
F A I L : t e s t _ d a i l y _ 
s a l e s _ i n d i a _ t im e 
z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e)
-----------------------------------------------------------------
-----
T r a c e b a c k (m o s t r e 
c e n t c a l l l a s t ) :
F ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
12/32

13 / 32
 s . p y " , l i n e 7 6 , i n 
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
se lf.asse rtEqua l(
~~~~~~~~~~~~~~~~^
r e p o r t s .d a i ly _ s a 
le s ( s e l f .c o n n , " 2 0 
2 5 - 0 3 - 1 0 " ,
utc_offset_m inutes=330),
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^
{"day":"2025-03-10","revenue_cents":1200 
,"orders":1},
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^
)
^
A s s e r t io n E r ro r : { 
'd a y ' : '2 0 2 5 -0 3 - 10 ' 
, ' re v e n u e _ c e n ts ' : 
0 , 'o rd e rs ' :
0}!= 
{'day':'2025-03-10','revenue_cents':1200,'orders':1}
- {'day ': '2025 -03 -10 ', 'o 
rde rs ':0 , 'revenue_cen ts 
':0 }
?^
+ 
{'day':'2025-03-10','orders':1,'revenue_cents':1200}
? ^ +++
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
FAILED (failures=1)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
-v
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
13/32

14 / 32
 OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m un ittestd iscover-s tests 
-v
te s t_ c a n c e l_ p a id _ o 
rd e r_ re s to c k s
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
c a n c e l _ p a i d _ o r d e 
r _ r e s t o c k s ) . . .
ok
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
c a n c e l _ p e n d i n g _ o 
r d e r _ r e s t o c k
s) ...ok
tes t_coupon_ reduces_ taxab 
le_am oun t
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
c o u p o n _ r e d u c e s _ t 
a x a b l e _ a m o u
n t) ...ok
tes t_coupon_ takes_ ten_pe 
rcen t
(tes t_o rde rs .O rde rD 
eskTes t.tes t_coupon_ takes_ 
ten_pe rcen t)
...ok
t e s t _ d a i l y _ s a l e s 
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
d a i l y _ s a l e s ) . . .
ok
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
d a i l y _ s a l e s _ i n d i 
a _ t im e z o n e ) . . .
ok
test_order_totals_w ith_tax
(test_orders.OrderDeskTest.test_order_totals_w 
ith_tax)...ok
te s t_ o u t_ o f_ s to c k
(tes t_o rde rs .O rde rD 
eskTes t.tes t_ou t_o f_s tock 
) ...ok
tes t_paym en t_m a rks_o rde 
r_pa id
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
p a y m e n t _ m a r k s _ o r 
d e r _ p a i d )
...ok
te s t_ p r ic e _ c h a n g e
(test_orders.O 
rderDeskTest.test_price_change) 
...ok
-----------------------------------------------------------------
-----
Ran10 tests in0.007s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py tillpo 
int/reports.py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
c o m m i t - m " F i x d a i l 
y s a l e s t im e z o n e o f 
f s e t "
[m a i n a 7 9 d a 3 9 ] F i x 
d a i l y s a l e s t im e z o 
n e o f f s e t
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
14/32

15 / 32
 2 fileschanged,19 
insertions(+),1deletion(-)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
cat
t i l lp o in t /p a ym e n ts 
.p y
" " " P a ym e n t p r o v id e 
r w e b h o o k s . T h e p r o 
v id e r r e t r ie s a d e l 
iv e r y
untilitgetsa2xx,soeventscan 
repeat."""
from .importdb
c la s s P a ym e n tE r ro r 
(E x c e p t io n ) :
pass
c la s s P a ym e n ts :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
d e f h a n d le _ e v e n t ( 
s e l f , e v e n t , n o w = N 
o n e ) :
" " " e v e n t : d ic t ( id , 
ty p e , o rd e r_ id , am o u 
n t_ c e n ts ) . R e tu rn s 
th e
o rd e r 's s ta tu s a f te r 
th e e v e n t ." " "
i f e v e n t .g e t ( " t y p 
e " ) != " p a ym e n t . s u c 
c e e d e d " :
re tu rn N o n e
order=self.conn.execute("SELECT*FROM 
ordersWHERE
id = ? " , ( e v e n t [ " o r 
d e r _ id " ] , ) ) . f e t c 
h o n e ( )
i f o rd e r is N o n e :
ra ise Paym en tE rro r(f"paym 
en t fo runknow n o rde r
{e v e n t [ 'o rd e r_ id ' ] 
} " )
iforder["status"]== "cance 
lled":
raisePaymentError(f"order{order['id']} 
iscancelled")
se lf.conn .execu te (
"INSERT 
INTOpayments(order_id,event_id,
amount_cents,received_at)VALUES 
(?,?,?,?)",
(o rd e r [ " id " ] , e v e n 
t [ " id " ] , e v e n t [ " am 
o u n t_ c e n ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
iforder["status"]== "pend 
ing"and
se lf.pa 
id_cents(order["id"])>= 
order["tota l_cents"]:
self.conn.execute("UPDATEordersSETstatus= 
'paid'
WHERE id=?",(order["id"],))
re tu rn "p a id "
re tu rn o rd e r [ " s ta tu s 
" ]
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
15/32

16 / 32
 d e f p a id _ c e n t s ( s e 
l f , o r d e r _ id ) :
row = se lf.conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
cat
t i l lp o in t /p a ym e n ts 
.p y
" " " P a ym e n t p r o v id e 
r w e b h o o k s . T h e p r o 
v id e r r e t r ie s a d e l 
iv e r y
untilitgetsa2xx,soeventscan 
repeat."""
from .importdb
c la s s P a ym e n tE r ro r 
(E x c e p t io n ) :
pass
c la s s P a ym e n ts :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
d e f h a n d le _ e v e n t ( 
s e l f , e v e n t , n o w = N 
o n e ) :
" " " e v e n t : d ic t ( id , 
ty p e , o rd e r_ id , am o u 
n t_ c e n ts ) . R e tu rn s 
th e
o rd e r 's s ta tu s a f te r 
th e e v e n t ." " "
i f e v e n t .g e t ( " t y p 
e " ) != " p a ym e n t . s u c 
c e e d e d " :
re tu rn N o n e
order=self.conn.execute("SELECT*FROM 
ordersWHERE
id = ? " , ( e v e n t [ " o r 
d e r _ id " ] , ) ) . f e t c 
h o n e ( )
i f o rd e r is N o n e :
ra ise Paym en tE rro r(f"paym 
en t fo runknow n o rde r
{e v e n t [ 'o rd e r_ id ' ] 
} " )
iforder["status"]== "cance 
lled":
raisePaymentError(f"order{order['id']} 
iscancelled")
se lf.conn .execu te (
"INSERT 
INTOpayments(order_id,event_id,
amount_cents,received_at)VALUES 
(?,?,?,?)",
(o rd e r [ " id " ] , e v e n 
t [ " id " ] , e v e n t [ " am 
o u n t_ c e n ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
16/32

17 / 32
  iforder["status"]== "pend 
ing"and
se lf.pa 
id_cents(order["id"])>= 
order["tota l_cents"]:
self.conn.execute("UPDATEordersSETstatus= 
'paid'
WHERE id=?",(order["id"],))
re tu rn "p a id "
re tu rn o rd e r [ " s ta tu s 
" ]
d e f p a id _ c e n t s ( s e 
l f , o r d e r _ id ) :
row = se lf.conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
f r o m t i l l p o i n t im p 
o r t d b , r e p o r t s
f r o m t i l l p o i n t . a p 
i im p o r t A p p
from tillpoint.catalog 
importOutOfStock
c lassO rderDeskTest(un 
ittest.TestCase):
d e f s e tU p ( s e l f ) :
se lf.conn = db .connec t()
se lf.app = App (se lf.conn )
s e l f . a p p . c a t a l o g 
. a d d _ p r o d u c t ( "M U 
G " , "M u g " , 1 2 0 0 ,
stock=10)
se lf.app .ca ta log .add_p 
roduc t("TEE","T-sh irt",2500 ,
stock=3)
self.conn.execute("INSERT 
INTOcoupons(code,kind,value)
VALUES ('TEN ','percent',10)")
deftest_order_totals_w 
ith_tax(self):
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
17/32

18 / 32
 o r d e r = s e l f . a p p . 
o r d e r s . c r e a t e ( " a 
n a " , [ ( "M U G " , 2 ) , ( 
" T E E " ,
1)],reg ion="CA")
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],4900 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],355 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],5255 )
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . s t o c k , 8 )
de f tes t_coupon_ takes_ 
ten_pe rcen t(se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] ,
coupon_code="TEN ")
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1080 )
d e f te s t_ o u t_ o f_ s to 
c k ( s e l f ) :
w 
ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te 
("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
de f tes t_paym en t_m a rks_o 
rde r_pa id (se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app 
.hand le ("PO ST ",
" /w e b h o o k s / p a y m e 
n t s " , {
" id " : " e v t _ 1 " , " t y 
p e " : " p a ym e n t . s u c 
c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l 
( ( s t a t u s , p a y lo a d 
[ " s t a t u s " ] ) , ( 2 0 0 
, " p a id " ) )
de f tes t_dup lica te_paym en 
t_even t_ is_ igno red (se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
event= {
"id":"evt_dup licate",
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
}
se lf.app .paym en ts .hand 
le_even t(even t)
se lf.app .paym en ts .hand 
le_even t(even t)
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
18/32

19 / 32
 se lf.assertEqua l(se lf.app 
.paym ents.pa 
id_cents(order["id"]),
1200)
d e f t e s t _ c a n c e l_ p 
a id _ o r d e r _ r e s t o c 
k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 2 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o rd e r [ " id " ] , " am o u 
n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
d e f t e s t _ c a n c e l_ p 
e n d in g _ o r d e r _ r e s 
t o c k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
1)
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
se lf.assertEqua l(se lf.app 
.orders.get(order["id"])["status"],
" c a n c e l le d " )
d e f te s t_ d a i ly _ s a le 
s ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 
2 5 , 3 , 1 0 , 1 2 , 0 , t z i 
n f o = t im e z o n e . u t c 
)
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 3 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } , 
n o w = n o o n )
s e lf .a s s e r tE q u a l( 
re p o r ts .d a i ly_ s a le s 
(s e lf .c o n n , "2 0 2 5 -0 
3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 
,
"orders":1})
d e f t e s t _ d a i l y _ s a 
l e s _ i n d i a _ t im e z o 
n e ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
p a y m e n t _ t im e = d a t 
e t im e ( 2 0 2 5 , 3 , 9 , 1 
9 , 0 ,
t z i n f o = t im e z o n e . 
u t c )
se lf.app .paym en ts .hand 
le_even t(
{
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
19/32

" id " : " e v t_ in d ia " ,
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
},
n o w = p a y m e n t _ t im e 
,
)
se lf.asse rtEqua l(
r e p o r t s .d a i ly _ s a 
le s ( s e l f .c o n n , " 2 0 
2 5 - 0 3 - 1 0 " ,
utc_offset_m inutes=330),
{"day":"2025-03-10","revenue_cents":1200 
,"orders":
1},
)
d e f t e s t _ p r ic e _ c h 
a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( 
" P U T " , " / p r o d u c t s 
/M U G " , { " p r i c e _ c e 
n t s " :
1500})
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . p r i c e _ c e n t
s,1500)
d e f t e s t _ c o u p o n _ r 
e d u c e s _ t a x a b le _ am 
o u n t ( s e l f ) :
o rde r= se lf.app .o rde rs .c 
rea te (
"ana",
[ ( "M U G " , 1 ) ] ,
reg ion="CA",
coupon_code="TEN "
)
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],1200 )
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
ChatGPT
20 / 32
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
20/32

You
21 / 32
  
================================================
======================
FA IL :
tes t_dup lica te_paym en 
t_even t_ is_ igno red (tes ts 
.tes t_o rde rs .O rd
e rD eskTes t.tes t_dup lica 
te_paym en t_even t_ is_ igno 
red )
-----------------------------------------------------------------
-----
T r a c e b a c k (m o s t r e 
c e n t c a l l l a s t ) :
F ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
s.py",line52,in 
test_duplicate_payment_event_is_ignored
se lf.assertEqua l(se lf.app 
.paym ents.pa 
id_cents(order["id"]),
1200)
~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^
AssertionError:2400 != 1200
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 4 s
FAILED (failures=1)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
" " " P a ym e n t p r o v id e 
r w e b h o o k s . T h e p r o 
v id e r r e t r ie s a d e l 
iv e r y
untilitgetsa2xx,soeventscan 
repeat."""
from .importdb
c la s s P a ym e n tE r ro r 
(E x c e p t io n ) :
pass
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
21/32

22 / 32
 c la s s P a ym e n ts :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
d e f h a n d le _ e v e n t ( 
s e l f , e v e n t , n o w = N 
o n e ) :
" " " e v e n t : d ic t ( id , 
ty p e , o rd e r_ id , am o u 
n t_ c e n ts ) . R e tu rn s 
th e
o rd e r 's s ta tu s a f te r 
th e e v e n t ." " "
i f e v e n t .g e t ( " t y p 
e " ) != " p a ym e n t . s u c 
c e e d e d " :
re tu rn N o n e
order=self.conn.execute("SELECT*FROM 
ordersWHERE
id = ? " , ( e v e n t [ " o r 
d e r _ id " ] , ) ) . f e t c 
h o n e ( )
i f o rd e r is N o n e :
ra ise Paym en tE rro r(f"paym 
en t fo runknow n o rde r
{e v e n t [ 'o rd e r_ id ' ] 
} " )
iforder["status"]== "cance 
lled":
raisePaymentError(f"order{order['id']} 
iscancelled")
e x is t in g = s e l f .c o n 
n .e x e c u te (
" S E L E C T 1 F R O M p a ym 
e n t s W H E R E e v e n t _ 
id = ? " ,
( e v e n t [ " id " ] , ) ,
) . fe tc h o n e ( )
i f e x is t in g :
re tu rn o rd e r [ " s ta tu s 
" ]
se lf.conn .execu te (
"INSERT 
INTOpayments(order_id,event_id,
amount_cents,received_at)VALUES 
(?,?,?,?)",
(o rd e r [ " id " ] , e v e n 
t [ " id " ] , e v e n t [ " am 
o u n t_ c e n ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
iforder["status"]== "pend 
ing"and
se lf.pa 
id_cents(order["id"])>= 
order["tota l_cents"]:
self.conn.execute("UPDATEordersSETstatus= 
'paid'
WHERE id=?",(order["id"],))
re tu rn "p a id "
re tu rn o rd e r [ " s ta tu s 
" ]
d e f p a id _ c e n t s ( s e 
l f , o r d e r _ id ) :
row = se lf.conn .execu te (
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
22/32

"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
ChatGPT
You
R a n 1 te s t in 0 .0 0 3 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
an11tests in0.010s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
epthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py 
tillpoint/payments.py
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
23 / 32
        Takeyourcuriosity 
further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
23/32

24 / 32
 You
 % gitcomm it-m 
"Ignoreduplicatepaymentwebhookevents"
[m a i n 9 f 8 7 4 a 3 ] I g n 
o r e d u p l i c a t e p a y m 
e n t w e b h o o k e v e n t s
2 fileschanged,21 insertions(+)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
inka enn iunnay
ChatGPT
You
d e f r e le a s e ( s e l f , 
s k u , q t y ) :
"""Putqtyunitsback 
intostock."""
s e l f .c o n n .e x e c u te 
( "U P D A T E p ro d u c ts S 
E T s to c k = s to c k + ?
W H E R E s k u = ? " , (q ty , 
s k u ) )
se lf._cache .pop (sku ,N one )
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
ss
@ d a ta c la s s ( f ro z e n 
= T ru e )
c la s s P ro d u c t :
sku :str
n am e : s t r
p r ic e _ c e n t s : in t
s to c k : in t
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
      
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
24/32

25 / 32
 c la s s C a ta lo g :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
self._cache= {}
d e f a d d _ p r o d u c t ( s 
e l f , s k u , n am e , p r ic 
e _ c e n t s , s t o c k = 0 ) 
:
se lf.conn .execu te (
"INSERT 
INTOproducts(sku,name,price_cents,stock)
VALUES (?,?,?,?)",
(s k u , n am e , p r ic e _ c 
e n ts , s to c k ) ,
)
se lf._cache .pop (sku ,N one )
de fge t_p roduc t(se lf,sku ):
p roduc t= se lf._cache .ge 
t(sku )
i f p ro d u c t is N o n e :
row = se lf.conn .execu te 
("SELECT *FROM p roduc ts
W H E R E s k u = ? " , ( s k u 
, ) ) . fe tc h o n e ( )
if row is N o n e:
ra is e U n k n ow n P ro d u c 
t (s k u )
p ro d u c t = P ro d u c t ( 
row [ " s k u " ] , row [ " n 
am e " ] ,
row ["price_cents"],row 
["stock"])
se lf._cache [sku ]= p roduc t
returnproduct
d e f u p d a t e _ p r ic e ( 
s e l f , s k u , p r ic e _ c 
e n t s ) :
i f p r ic e _ c e n t s < 0 :
r a is e V a lu e E r ro r ( " 
p r ic e m u s t n o t b e n e 
g a t iv e " )
c u r = s e l f .c o n n .e x e 
c u te ( "U P D A T E p ro d u 
c ts S E T p r ic e _ c e n ts
= ?W H E R E s k u = ? " , (p r 
ic e _ c e n ts , s k u ) )
ifcu r.row coun t== 0 :
ra is e U n k n ow n P ro d u c 
t (s k u )
se lf._cache .pop (sku ,N one )
de f rese rve (se lf,sku ,q ty 
):
" " " T a k e q t y u n i t s o 
u t o f s t o c k , o r r a i s 
e O u tO f S t o c k . " " "
p roduc t= se lf.ge t_p roduc 
t(sku )
if p ro d u c t .s to c k < q 
ty :
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
25/32

26 / 32
  r a i s e O u tO f S t o c k 
( s k u , q t y , p r o d u c t 
. s t o c k )
s e l f .c o n n .e x e c u te 
( "U P D A T E p ro d u c ts S 
E T s to c k = s to c k - ?
W H E R E s k u = ? " , (q ty , 
s k u ) )
se lf._cache .pop (sku ,N one )
d e f r e le a s e ( s e l f , 
s k u , q t y ) :
"""Putqtyunitsback 
intostock."""
s e l f .c o n n .e x e c u te 
( "U P D A T E p ro d u c ts S 
E T s to c k = s to c k + ?
W H E R E s k u = ? " , (q ty , 
s k u ) )
se lf._cache .pop (sku ,N one )
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
grep-n-
A 2 5 "d e f re s e rv e " t i 
l lp o in t /c a ta lo g .p y
53: defreserve(self,sku,qty):
5 4 - " ""Take q ty un its ou t 
of s t o c k , o r r a i s e O 
u tO f S t o c k . " " "
55 - p roduc t= se lf.ge t_p 
roduc t(sku )
5 6 - if p ro d u c t .s to c k 
< q ty :
5 7 - r a i s e O u tO f S t o 
c k ( sku ,qty,pr oduct.stock)
58 - se lf.conn .execu te ("U 
PDATE p roduc tsSET s tock = s 
tock -
?W H E R E s k u = ? " , (q ty 
, s k u ) )
59 - se lf._cache .pop (sku 
,None)
60-
61- defrelease(self,sku,qty):
62- """Putqtyunitsback in to s 
to c k ." " "
63 - se lf.conn .execu te ("U 
PDATE productsSET stock= stock+
?W H E R E s k u = ? " , (q ty 
, s k u ) )
64 - se lf._cache .pop (sku 
,None)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
65-
66 -de f from _ iso (tex t):
67- 
returndatetime.strptime(text,"%Y-%m 
-
% d T % H :% M :% S Z " ) . r e 
p l a c e ( t z i n f o = t im 
e z o n e . u t c )
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
26/32

ChatGPT
You
5-
66 -de f from _ iso (tex t):
67- 
returndatetime.strptime(text,"%Y-%m 
-
% d T % H :% M :% S Z " ) . r e 
p l a c e ( t z i n f o = t im 
e z o n e . u t c )
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
);
CREATETABLE IFNOTEXISTSorders(
i d I N T E G E R P R IM A R Y 
K E Y A U T O I N C R E M E N T 
,
c u s tom e r T E X T N O T N U 
L L ,
r e g io n T E X T N O T N U L 
L ,
statusTEXTNOTNULLDEFAULT 
'pending',
coupon TEXT ,
subtotal_cents INTEGERNOTNULL,
d i s c o u n t _ c e n t s IN 
T E G E R N O T N U L L D E F A 
U L T 0 ,
tax_cents 
INTEGERNOTNULLDEFAULT0,
total_cents INTEGERNOTNULL,
created_atTEXTNOTNULL
);
CREATETABLE 
IFNOTEXISTSorder_items(
order_ id 
INTEGERNOTNULLREFERENCES 
orders(id),
skuTEXTNOTNULLREFERENCES 
products(sku),
qty INTEGERNOTNULL,
unit_price_cents INTEGERNOTNULL
);
CREATETABLE 
IFNOTEXISTSpayments(
i d I N T E G E R P R IM A R Y 
K E Y A U T O I N C R E M E N T 
,
order_ id 
INTEGERNOTNULLREFERENCES 
orders(id),
e v e n t _ id T E X T N O T N 
U L L ,
amount_cents INTEGERNOTNULL,
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
27 / 32
      
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
27/32

28 / 32
  rece ived_atTEXTNOTNULL
);
CREATE INDEX IFNOTEXISTS 
idx_payments_orderON
p a ym e n ts (o rd e r_ id ) ;
CREATE INDEX IFNOTEXISTS 
idx_orders_customerON
o rd e rs (c u s tom e r , c re 
a te d _ a t ) ;
"""
d e f c o n n e c t ( p a t h = 
" :m e m o r y : " ) :
c o n n = s q l i te 3 .c o n n 
e c t (p a th , is o la t io n 
_ le v e l= N o n e )
c o n n . r o w _ f a c t o r y 
= s q l i t e 3 .R o w
conn.execute("PRAGMA 
foreign_keys=ON")
c o n n .e x e c u te s c r ip 
t (S C H EM A )
re tu rn conn
d e f u tc n ow ( ) :
returndatetime.now(timezone.utc).replace(m 
icrosecond=0)
d e f to _ is o (d t ) :
r e t u r n d t . a s t im e z 
o n e ( t im e z o n e . u t c 
) . s t r f t im e ( " % Y - % 
m -
% d T % H :% M :% S Z " )
d e f f rom _ is o ( te x t ) :
returndatetime.strptime(text,"%Y-%m 
-
% d T % H :% M :% S Z " ) . r e 
p l a c e ( t z i n f o = t im 
e z o n e . u t c )
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
fr om t i l l p o i n t im p o 
r t d b , r e p o r t s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
28/32

29 / 32
 f r o m t i l l p o i n t . a 
p i im p o r t A p p
from tillpoint.catalog 
importOutOfStock
c lassO rderDeskTest(un 
ittest.TestCase):
d e f s e tU p ( s e l f ) :
se lf.conn = db .connec t()
se lf.app = App (se lf.conn )
s e l f . a p p . c a t a l o g 
. a d d _ p r o d u c t ( "M U 
G " , "M u g " , 1 2 0 0 ,
stock=10)
se lf.app .ca ta log .add_p 
roduc t("TEE","T-sh irt",2500 ,
stock=3)
self.conn.execute("INSERT 
INTOcoupons(code,kind,value)
VALUES ('TEN ','percent',10)")
deftest_order_totals_w 
ith_tax(self):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 2 ) , ( " 
T E E " ,
1)],reg ion="CA")
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],4900 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],355 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],5255 )
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . s t o c k , 8 )
de f tes t_coupon_ takes_ 
ten_pe rcen t(se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] ,
coupon_code="TEN ")
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1080 )
d e f te s t_ o u t_ o f_ s to 
c k ( s e l f ) :
w 
ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te 
("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
de f tes t_paym en t_m a rks_o 
rde r_pa id (se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app 
.hand le ("PO ST ",
" /w e b h o o k s / p a y m e 
n t s " , {
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
29/32

30 / 32
 " id " : " e v t _ 1 " , " t y 
p e " : " p a ym e n t . s u c 
c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l 
( ( s t a t u s , p a y lo a d 
[ " s t a t u s " ] ) , ( 2 0 0 
, " p a id " ) )
de f tes t_dup lica te_paym en 
t_even t_ is_ igno red (se lf):
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
event= {
"id":"evt_dup licate",
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
}
se lf.app .paym en ts .hand 
le_even t(even t)
se lf.app .paym en ts .hand 
le_even t(even t)
se lf.assertEqua l(se lf.app 
.paym ents.pa 
id_cents(order["id"]),
1200)
d e f t e s t _ c a n c e l_ p 
a id _ o r d e r _ r e s t o c 
k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 2 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o rd e r [ " id " ] , " am o u 
n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
d e f t e s t _ c a n c e l_ p 
e n d in g _ o r d e r _ r e s 
t o c k s ( s e l f ) :
order= se lf.app 
.orders.create("ana",[("TEE",2)])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
1)
se lf.app .orders.cance 
l(order["id"])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
se lf.assertEqua l(se lf.app 
.orders.get(order["id"])["status"],
" c a n c e l le d " )
d e f te s t_ d a i ly _ s a le 
s ( s e l f ) :
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
30/32

31 / 32
 o r d e r = s e l f . a p p . 
o r d e r s . c r e a t e ( " a 
n a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 
2 5 , 3 , 1 0 , 1 2 , 0 , t z i 
n f o = t im e z o n e . u t c 
)
se lf.app .paym en ts .hand 
le_even t(
{ " id " : " e v t _ 3 " , " t 
y p e " : " p a ym e n t . s u 
c c e e d e d " , " o r d e r _ 
id " :
o r d e r [ " id " ] , " am o u 
n t _ c e n t s " : 1 2 0 0 } , 
n o w = n o o n )
s e lf .a s s e r tE q u a l( 
re p o r ts .d a i ly_ s a le s 
(s e lf .c o n n , "2 0 2 5 -0 
3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 
,
"orders":1})
d e f t e s t _ d a i l y _ s a 
l e s _ i n d i a _ t im e z o 
n e ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
p a y m e n t _ t im e = d a t 
e t im e ( 2 0 2 5 , 3 , 9 , 1 
9 , 0 ,
t z i n f o = t im e z o n e . 
u t c )
se lf.app .paym en ts .hand 
le_even t(
{
" id " : " e v t_ in d ia " ,
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
},
n o w = p a y m e n t _ t im e 
,
)
se lf.asse rtEqua l(
r e p o r t s .d a i ly _ s a 
le s ( s e l f .c o n n , " 2 0 
2 5 - 0 3 - 1 0 " ,
utc_offset_m inutes=330),
{"day":"2025-03-10","revenue_cents":1200 
,"orders":
1},
)
d e f t e s t _ p r ic e _ c h 
a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( 
" P U T " , " / p r o d u c t s 
/M U G " , { " p r i c e _ c e 
n t s " :
1500})
s e l f . a s s e r t E q u a l 
( s e l f . a p p . c a t a l o 
g . g e t _ p r o d u c t ( "M 
U G " ) . p r i c e _ c e n t
s,1500)
d e f t e s t _ c o u p o n _ r 
e d u c e s _ t a x a b le _ am 
o u n t ( s e l f ) :
o rde r= se lf.app .o rde rs .c 
rea te (
"ana",
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
31/32

32 / 32
  [ ( "M U G " , 1 ) ] ,
reg ion="CA",
coupon_code="TEN "
)
se lf.asse rtEqua l(o rde 
r["sub to ta l_cen ts"],1200 )
se lf.asse rtEqua l(o rde r["d 
iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
ChatGPT
   Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b025cc5-2530-83ec-bc99-6dc5e9c0930b
32/32

