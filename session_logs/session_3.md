1 / 33
  You
ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
s.py",line68,in 
test_coupon_reduces_taxable_amount
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError:87 !=78
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 5 s
FAILED (failures=1)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
reduces_ taxab le_
am o u n t - v
tes t_coupon_ reduces_ taxab 
le_am oun t
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
reduces_ taxab le_
am o u n t ) . . . o k
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 3 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m un ittestd iscover-s tests 
-v
te s t_ c a n c e l_ p a id _ o 
rd e r_ re s to c k s
(tes t_o rde rs .O rde rD 
eskTes t.tes t_cance l_pa id_o 
rde r_ res tocks ) ...
ok
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
ten_pe rcen t) ...
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
t i l lp o in (3 )
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
1/33

2 / 33
  ok
t e s t _ d a i l y _ s a l e s 
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
d a i l y _ s a l e s ) . . .
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
d e r _ p a i d ) . . .
ok
te s t_ p r ic e _ c h a n g e
(test_orders.O 
rderDeskTest.test_price_change) 
...ok
-----------------------------------------------------------------
-----
Ran8 tests in0.007s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
s ta tu s - - s h o r t
M tes ts / te s t_ o rd e rs 
.py
M t illpo in t /p r ic in g .p 
y
?? .DS_Store
? ? s e s s io n _ lo g s / .D 
S _ S to re
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py 
tillpoint/pricing.py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
comm it-m 
"Fixtaxcalculationaftercoupondiscount"
[m a i n e 6 f 6 c a d ] F i x 
t a x c a l c u l a t i o n a f 
t e r c o u p o n d i s c o u n 
t
2 fileschanged,20 
insertions(+),5deletions(-)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
"""Creating,cancellingand 
listingorders."""
f r o m . im p o r t d b , p r 
i c i n g
from .catalog importCatalog
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
2/33

3 / 33
 c la s s O rd e rE r ro r (E x 
c e p t io n ) :
pass
c lassO rde rs :
d e f _ _ in i t _ _ ( s e l f 
, c o n n , c a t a lo g = N o 
n e ) :
se lf.conn = conn
se lf.ca ta log = ca ta log o 
rC a ta log (conn )
defcreate(se lf,custom er, item 
s,reg ion="NONE",
c o u p o n _ c o d e = N o n e 
, n ow = N o n e ) :
"""items:listof(sku,qty).Reservesstock,redeems 
the
c o u p o n a n d s to re s th 
e o rd e r , a l l o r n o th 
in g ." " "
ifno t item s :
raiseOrderError("anorderneedsatleastone 
item")
ifany(qty<=0 for_,qty in 
items):
raiseO 
rderError("quantitiesmustbepositive")
self.conn.execute("BEGIN 
IMMEDIATE")
try:
coupon = se lf._coupon 
(coupon_code )
priced= [(sku,qty,
self.catalog.get_product(sku).price_cents)forsku,qty 
in items]
totals=pricing.price_order([(price,qty)for_,qty,price 
in
p r ic e d ] , re g io n , c o 
u p o n )
forsku,qty,_ inpriced:
se lf.ca ta log .rese rve (sku 
,q ty )
ifcoupon isnotNone:
s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s +
1W H E R E c o d e = ? " , (c o 
u p o n _ c o d e , ) )
cu r= se lf.conn .execu te (
"INSERT 
INTOorders(customer,region,coupon,
sub to ta l_cen ts ,d iscoun 
t_cen ts , tax_cen ts ,"
"total_cents,created_at)VALUES 
(?,?,?,?,?,?,?,?)",
(c u s tom e r , re g io n , c 
o u p o n _ c o d e ,
totals["subtotal_cents"],totals["d 
iscount_cents"],
to ta ls [ " ta x _ c e n ts " 
] , to ta ls [ " to ta l_ c e n 
ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
3/33

4 / 33
 order_id=cur.lastrow id
se lf.conn .execu tem any (
"INSERT 
INTOorder_items(order_id,sku,qty,
unit_price_cents)VALUES 
(?,?,?,?)",
[(order_id,sku,qty,price)forsku,qty,price 
inpriced],
)
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f c a n c e l ( s e l f , o 
r d e r _ id ) :
"""Cancelanorderthathasnotshipped.Itsstockand 
its
coupon use go back ."""
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"]== "cance 
lled":
re tu rn o rd e r
iforder["status"]== "sh ipped":
ra is e O rd e rE r ro r ( " a 
s h ip p e d o rd e r c a n n o 
t b e c a n c e l le d " )
self.conn.execute("BEGIN 
IMMEDIATE")
try:
i f o r d e r [ " s t a t u s " 
] = = " p a id " :
fo r i tem in o rd e r [ " i 
tem s " ] :
self.catalog.release(item 
["sku"],item ["qty"])
i f o rd e r [ " c o u p o n " 
] :
s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s -
1W H E R E c o d e = ? A N D u 
s e s > 0 " , (o rd e r [ " c o 
u p o n " ] , ) )
self.conn.execute("UPDATEordersSET 
status=
'cancelled'WHERE 
id=?",(order_id,))
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f s h ip ( s e l f , o r d 
e r _ id ) :
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"] != "pa id":
r a i s e O r d e r E r r o r ( 
" o n l y a p a id o r d e r c 
a n s h ip " )
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
4/33

5 / 33
  
self.conn.execute("UPDATEordersSETstatus= 
'shipped'
WHERE id=?",(order_id,))
re tu rn se lf.ge t(o rde r_ id 
)
d e f g e t ( s e l f , o r d e 
r _ id ) :
row=self.conn.execute("SELECT*FROM 
ordersWHERE id
= ? " , ( o r d e r _ id , ) ) 
. f e t c h o n e ( )
if row is N one :
ra iseO rde rE rro r(f"no o rde 
r {o rde r_ id }")
o rd e r = d ic t ( row )
order["items"]= 
[dict(r)forrinself.conn.execute(
"SELECTsku,qty,unit_price_centsFROM 
order_items
WHEREorder_id=?ORDERBY row 
id",(order_id,))]
re tu rn o rd e r
d e f l is t_ fo r ( s e l f , 
c u s tom e r , p a g e = 1 , p 
e r_ p a g e = 2 0 ) :
row s = se lf.conn .execu te (
"SELECT idFROM 
ordersWHEREcustomer=?ORDERBY
c r e a t e d _ a t D E S C , i 
d D E S C L IM I T ? O F F S E 
T ? " ,
(c u s tom e r , p e r_ p a g e 
, (p a g e - 1 ) * p e r_ p a g 
e ) ,
).fe tcha ll()
return [self.get(r["id"])forr 
in rows]
def_coupon(se lf,code):
ifcode isNone:
re tu rn N o n e
row=self.conn.execute("SELECT*FROM 
couponsWHERE
code= ?",(code,)).fetchone()
if row is N one :
raisepricing.CouponRejected(f"unknowncoupon 
{code}")
re tu rn row
ChatGPT
You
"""Creating,cancellingand 
listingorders."""
f r o m . im p o r t d b , p r 
i c i n g
from .catalog importCatalog
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
5/33

6 / 33
 c la s s O rd e rE r ro r (E x 
c e p t io n ) :
pass
c lassO rde rs :
d e f _ _ in i t _ _ ( s e l f 
, c o n n , c a t a lo g = N o 
n e ) :
se lf.conn = conn
se lf.ca ta log = ca ta log o 
rC a ta log (conn )
defcreate(se lf,custom er, item 
s,reg ion="NONE",
c o u p o n _ c o d e = N o n e 
, n ow = N o n e ) :
"""items:listof(sku,qty).Reservesstock,redeems 
the
c o u p o n a n d s to re s th 
e o rd e r , a l l o r n o th 
in g ." " "
ifno t item s :
raiseOrderError("anorderneedsatleastone 
item")
ifany(qty<=0 for_,qty in 
items):
raiseO 
rderError("quantitiesmustbepositive")
self.conn.execute("BEGIN 
IMMEDIATE")
try:
coupon = se lf._coupon 
(coupon_code )
priced= [(sku,qty,
self.catalog.get_product(sku).price_cents)forsku,qty 
in items]
totals=pricing.price_order([(price,qty)for_,qty,price 
in
p r ic e d ] , re g io n , c o 
u p o n )
forsku,qty,_ inpriced:
se lf.ca ta log .rese rve (sku 
,q ty )
ifcoupon isnotNone:
s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s +
1W H E R E c o d e = ? " , (c o 
u p o n _ c o d e , ) )
cu r= se lf.conn .execu te (
"INSERT 
INTOorders(customer,region,coupon,
sub to ta l_cen ts ,d iscoun 
t_cen ts , tax_cen ts ,"
"total_cents,created_at)VALUES 
(?,?,?,?,?,?,?,?)",
(c u s tom e r , re g io n , c 
o u p o n _ c o d e ,
totals["subtotal_cents"],totals["d 
iscount_cents"],
to ta ls [ " ta x _ c e n ts " 
] , to ta ls [ " to ta l_ c e n 
ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
6/33

7 / 33
 order_id=cur.lastrow id
se lf.conn .execu tem any (
"INSERT 
INTOorder_items(order_id,sku,qty,
unit_price_cents)VALUES 
(?,?,?,?)",
[(order_id,sku,qty,price)forsku,qty,price 
inpriced],
)
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f c a n c e l ( s e l f , o 
r d e r _ id ) :
"""Cancelanorderthathasnotshipped.Itsstockand 
its
coupon use go back ."""
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"]== "cance 
lled":
re tu rn o rd e r
iforder["status"]== "sh ipped":
ra is e O rd e rE r ro r ( " a 
s h ip p e d o rd e r c a n n o 
t b e c a n c e l le d " )
self.conn.execute("BEGIN 
IMMEDIATE")
try:
iforder["status"] in ("pend 
ing","pa id"):
fo r i tem in o rd e r [ " i 
tem s " ] :
self.catalog.release(item 
["sku"],item ["qty"])
i f o rd e r [ " c o u p o n " 
] :
s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s -
1W H E R E c o d e = ? A N D u 
s e s > 0 " , (o rd e r [ " c o 
u p o n " ] , ) )
self.conn.execute("UPDATEordersSET 
status=
'cancelled'WHERE 
id=?",(order_id,))
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f s h ip ( s e l f , o r d 
e r _ id ) :
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"] != "pa id":
r a i s e O r d e r E r r o r ( 
" o n l y a p a id o r d e r c 
a n s h ip " )
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
7/33

8 / 33
  
self.conn.execute("UPDATEordersSETstatus= 
'shipped'
WHERE id=?",(order_id,))
re tu rn se lf.ge t(o rde r_ id 
)
d e f g e t ( s e l f , o r d e 
r _ id ) :
row=self.conn.execute("SELECT*FROM 
ordersWHERE id
= ? " , ( o r d e r _ id , ) ) 
. f e t c h o n e ( )
if row is N one :
ra iseO rde rE rro r(f"no o rde 
r {o rde r_ id }")
o rd e r = d ic t ( row )
order["items"]= 
[dict(r)forrinself.conn.execute(
"SELECTsku,qty,unit_price_centsFROM 
order_items
WHEREorder_id=?ORDERBY row 
id",(order_id,))]
re tu rn o rd e r
d e f l is t_ fo r ( s e l f , 
c u s tom e r , p a g e = 1 , p 
e r_ p a g e = 2 0 ) :
row s = se lf.conn .execu te (
"SELECT idFROM 
ordersWHEREcustomer=?ORDERBY
c r e a t e d _ a t D E S C , i 
d D E S C L IM I T ? O F F S E 
T ? " ,
(c u s tom e r , p e r_ p a g e 
, (p a g e - 1 ) * p e r_ p a g 
e ) ,
).fe tcha ll()
return [self.get(r["id"])forr 
in rows]
def_coupon(se lf,code):
ifcode isNone:
re tu rn N o n e
row=self.conn.execute("SELECT*FROM 
couponsWHERE
code= ?",(code,)).fetchone()
if row is N one :
raisepricing.CouponRejected(f"unknowncoupon 
{code}")
re tu rn row
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
8/33

9 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
9/33

10 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
10/33

11 / 33
  se lf.asse rtEqua l(o rde 
r["d iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde 
r["tax_cen ts"],78 )
se lf.asse rtEqua l(o rde r["to 
ta l_cen ts"],1158 )
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
from til lp o i n t im p o r t 
d b , r e por ts
from til lp o i n t . a p i im 
p o r t A p p
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
11/33

12 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
12/33

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
13 / 33
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
13/33

You
14 / 33
  gitcomm it-m 
"Fixtaxcalculationaftercoupondiscount"
[m a i n e 6 f 6 c a d ] F i x 
t a x c a l c u l a t i o n a f 
t e r c o u p o n d i s c o u n 
t
2 fileschanged,20 
insertions(+),5deletions(-)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 4 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
f r om til l p o in t im p o r 
t d b , re p o rts
f r om til l p o in t . a p i 
im p o r t A p p
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
14/33

15 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
15/33

3)
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
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
16 / 33
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
16/33

ChatGPT
You
ekkada add cheyya li
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
17 / 33
      
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
17/33

18 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
18/33

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
19 / 33
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
19/33

You
------------------------
Ran8 tests in0.007s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
s ta tu s - - s h o r t
M tes ts /tes t_o rde rs .py
M t il lpo in t /p r ic in g .p 
y
?? .DS_Store
? ? s e s s io n _ lo g s / .D 
S _ S to re
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py 
tillpoint/pricing.py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
comm it-m 
"Fixtaxcalculationaftercoupondiscount"
[m a i n e 6 f 6 c a d ] F i x 
t a x c a l c u l a t i o n a f 
t e r c o u p o n d i s c o u n 
t
2 fileschanged,20 
insertions(+),5deletions(-)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 4 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
20 / 33
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
20/33

21 / 33
  -----
R a n 1 te s t in 0 .0 0 7 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
"""Creating,cancellingand 
listingorders."""
f r o m . im p o r t d b , p r 
i c i n g
from .catalog importCatalog
c la s s O rd e rE r ro r (E x 
c e p t io n ) :
pass
c lassO rde rs :
d e f _ _ in i t _ _ ( s e l f 
, c o n n , c a t a lo g = N o 
n e ) :
se lf.conn = conn
se lf.ca ta log = ca ta log o 
rC a ta log (conn )
defcreate(se lf,custom er, item 
s,reg ion="NONE",
c o u p o n _ c o d e = N o n e 
, n ow = N o n e ) :
"""items:listof(sku,qty).Reservesstock,redeems 
the
c o u p o n a n d s to re s th 
e o rd e r , a l l o r n o th 
in g ." " "
ifno t item s :
raiseOrderError("anorderneedsatleastone 
item")
ifany(qty<=0 for_,qty in 
items):
raiseO 
rderError("quantitiesmustbepositive")
self.conn.execute("BEGIN 
IMMEDIATE")
try:
coupon = se lf._coupon 
(coupon_code )
priced= [(sku,qty,
self.catalog.get_product(sku).price_cents)forsku,qty 
in items]
totals=pricing.price_order([(price,qty)for_,qty,price 
in
p r ic e d ] , re g io n , c o 
u p o n )
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
21/33

22 / 33
 forsku,qty,_ inpriced:
se lf.ca ta log .rese rve (sku 
,q ty )
ifcoupon isnotNone:
s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s +
1W H E R E c o d e = ? " , (c o 
u p o n _ c o d e , ) )
cu r= se lf.conn .execu te (
"INSERT 
INTOorders(customer,region,coupon,
sub to ta l_cen ts ,d iscoun 
t_cen ts , tax_cen ts ,"
"total_cents,created_at)VALUES 
(?,?,?,?,?,?,?,?)",
(c u s tom e r , re g io n , c 
o u p o n _ c o d e ,
totals["subtotal_cents"],totals["d 
iscount_cents"],
to ta ls [ " ta x _ c e n ts " 
] , to ta ls [ " to ta l_ c e n 
ts " ] ,
db .to_ iso (now o rdb .u tcnow 
())),
)
order_id=cur.lastrow id
se lf.conn .execu tem any (
"INSERT 
INTOorder_items(order_id,sku,qty,
unit_price_cents)VALUES 
(?,?,?,?)",
[(order_id,sku,qty,price)forsku,qty,price 
inpriced],
)
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f c a n c e l ( s e l f , o 
r d e r _ id ) :
"""Cancelanorderthathasnotshipped.Itsstockand 
its
coupon use go back ."""
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"]== "cance 
lled":
re tu rn o rd e r
iforder["status"]== "sh ipped":
ra is e O rd e rE r ro r ( " a 
s h ip p e d o rd e r c a n n o 
t b e c a n c e l le d " )
self.conn.execute("BEGIN 
IMMEDIATE")
try:
iforder["status"] in ("paid"):
fo r i tem in o rd e r [ " i 
tem s " ] :
self.catalog.release(item 
["sku"],item ["qty"])
i f o rd e r [ " c o u p o n " 
] :
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
22/33

23 / 33
 s e l f .c o n n .e x e c u te 
( "U P D A T E c o u p o n s S 
E T u s e s = u s e s -
1W H E R E c o d e = ? A N D u 
s e s > 0 " , (o rd e r [ " c o 
u p o n " ] , ) )
self.conn.execute("UPDATEordersSET 
status=
'cancelled'WHERE 
id=?",(order_id,))
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO 
LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id 
)
d e f s h ip ( s e l f , o r d 
e r _ id ) :
o rde r= se lf.ge t(o rde r_ id 
)
iforder["status"] != "pa id":
r a i s e O r d e r E r r o r ( 
" o n l y a p a id o r d e r c 
a n s h ip " )
self.conn.execute("UPDATEordersSETstatus= 
'shipped'
WHERE id=?",(order_id,))
re tu rn se lf.ge t(o rde r_ id 
)
d e f g e t ( s e l f , o r d e 
r _ id ) :
row=self.conn.execute("SELECT*FROM 
ordersWHERE id
= ? " , ( o r d e r _ id , ) ) 
. f e t c h o n e ( )
if row is N one :
ra iseO rde rE rro r(f"no o rde 
r {o rde r_ id }")
o rd e r = d ic t ( row )
order["items"]= 
[dict(r)forrinself.conn.execute(
"SELECTsku,qty,unit_price_centsFROM 
order_items
WHEREorder_id=?ORDERBY row 
id",(order_id,))]
re tu rn o rd e r
d e f l is t_ fo r ( s e l f , 
c u s tom e r , p a g e = 1 , p 
e r_ p a g e = 2 0 ) :
row s = se lf.conn .execu te (
"SELECT idFROM 
ordersWHEREcustomer=?ORDERBY
c r e a t e d _ a t D E S C , i 
d D E S C L IM I T ? O F F S E 
T ? " ,
(c u s tom e r , p e r_ p a g e 
, (p a g e - 1 ) * p e r_ p a g 
e ) ,
).fe tcha ll()
return [self.get(r["id"])forr 
in rows]
def_coupon(se lf,code):
ifcode isNone:
re tu rn N o n e
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
23/33

24 / 33
  
row=self.conn.execute("SELECT*FROM 
couponsWHERE
code= ?",(code,)).fetchone()
if row is N o n e :
raisepricing.CouponRejected(f"unknowncoupon 
{code}")
re tu rn row
ChatGPT
You
R a n 1 te s t in 0 .0 0 3 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m un ittestd iscover-s tests 
-v
te s t_ c a n c e l_ p a id _ o 
rd e r_ re s to c k s
(tes t_o rde rs .O rde rD 
eskTes t.tes t_cance l_pa id_o 
rde r_ res tocks ) ...
ok
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
ten_pe rcen t) ...
ok
t e s t _ d a i l y _ s a l e s 
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
d a i l y _ s a l e s ) . . .
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
d e r _ p a i d ) . . .
ok
te s t_ p r ic e _ c h a n g e
(test_orders.O 
rderDeskTest.test_price_change) 
...ok
-----------------------------------------------------------------
-----
Ran8 tests in0.007s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
24/33

OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
s ta tu s - - s h o r t
M tes ts /tes t_o rde rs .py
M t il lpo in t /p r ic in g .p 
y
?? .DS_Store
? ? s e s s io n _ lo g s / .D 
S _ S to re
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py 
tillpoint/pricing.py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
comm it-m 
"Fixtaxcalculationaftercoupondiscount"
[m a i n e 6 f 6 c a d ] F i x 
t a x c a l c u l a t i o n a f 
t e r c o u p o n d i s c o u n 
t
2 fileschanged,20 
insertions(+),5deletions(-)
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 4 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 7 s
OK
25 / 33
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
25/33

26 / 33
  
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 4 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 1 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
f r o m t ill p o in t im p o r 
t db , repo rts
f r o m t ill p o in t . a p i 
im p o r t A p p
from tillpoint.catalog 
importOutOfStock
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
26/33

27 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
27/33

28 / 33
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
28/33

29 / 33
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
You
k
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
ten_pe rcen t) ...
ok
t e s t _ d a i l y _ s a l e s 
( t e s t _ o r d e r s .O r d 
e r D e s k T e s t . t e s t _ 
d a i l y _ s a l e s ) . . .
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
d e r _ p a i d ) . . .
ok
te s t_ p r ic e _ c h a n g e
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
29/33

(test_orders.O 
rderDeskTest.test_price_change) 
...ok
-----------------------------------------------------------------
-----
Ran9 tests in0.008s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ c a n c e l _ p e n d 
i n g _ o r d e r _ r e s
tocks -v
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...FA IL
================================================
======================
FA IL : tes t_cance l_pend 
ing_o rde r_ res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks)
-----------------------------------------------------------------
-----
T r a c e b a c k (m o s t r e 
c e n t c a l l l a s t ) :
F ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
s .py", line 52 , in tes 
t_cance l_pend ing_o rde r_ res 
tocks
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,3)
~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^
A s s e r t io n E r ro r : 1 
!= 3
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 3 s
FAILED (failures=1)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
30 / 33
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
30/33

You
-----------------
R a n 1 te s t in 0 .0 0 5 s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
n9 tests in0.007s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
nex t
ChatGPT
You
nd ing o rde rs
2 fileschanged,11 
insertions(+),1deletion(-)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
31 / 33
 ChatGPT
       Takeyourcuriosity 
further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
31/33

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
i.un it_p rice_cen ts)AS g 
ross_cen ts"
" F R O M o r d e r _ i t e m s 
i J O IN o r d e r s o O N o . 
i d = i . o r d e r _ i d "
"WHEREo.status IN 
('paid','shipped')GROUPBY i.sku
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
32 / 33
    
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
32/33

33 / 33
  O R D E R B Y u n i t s D E S 
C , i . s k u L IM I T ? " ,
(lim it,),
).fe tcha ll()
re tu rn [d ic t ( r ) fo r r 
in row s ]
ChatGPT
   Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b02581d-1580-83ee-89b3-eb221c7a28eb
33/33

