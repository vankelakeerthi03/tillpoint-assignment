1 / 25
  You
im p o r t u n i t t e s t
from datetime 
importdatetime,timezone
f r o m t i l l p o i n t im p 
o r t d b , r e p o r t s
f r o m t i l l p o i n t . a p 
i im p o r t A p p
from tillpoint.catalog 
importCatalog,OutOfStock
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
t i l lp o in (7 )
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
1/25

2 / 25
 w 
ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te 
("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app 
.cata log 
.get_product("TEE").stock,
3)
d e f t e s t _ s t a le _ c a 
t a lo g _ c a c h e _ d o e s 
_ n o t _ o v e r s e l l ( s e 
l f ) :
w o r k e r 1 = C a t a lo g ( 
s e l f .c o n n )
w o rke r2 = C a ta log (se 
lf.conn )
w o r k e r 1 .g e t _ p r o d 
u c t ( "M U G " )
w o r k e r 2 .g e t _ p r o d 
u c t ( "M U G " )
w o r k e r 1 . r e s e r v e ( 
"M U G " , 7 )
w 
ithself.assertRaises(OutOfStock):
w o r k e r 2 . r e s e r v e ( 
"M U G " , 7 )
s tock = se lf.conn .execu te (
" S E L E C T s t o c k F R O M 
p r o d u c t s W H E R E s k u 
= 'M U G ' "
) . fe tc h o n e ( ) [ " s to 
c k " ]
se lf.asse rtEqua l(s tock ,3 )
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
2/25

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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
3 / 25
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
3/25

4 / 25
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
d e f te s t_ s e c o n d _ p a 
ym e n t_ is _ f la g g e d _ 
fo r_ re fu n d ( s e l f ) :
o r d e r = s e l f . a p p . o 
r d e r s . c r e a t e ( " a n 
a " , [ ( "M U G " , 1 ) ] )
se lf.app .paym en ts .hand 
le_even t({
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
4/25

5 / 25
  "id":"evt_first",
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
})
se lf.app .paym en ts .hand 
le_even t({
"id":"evt_second",
" t y p e " : " p a ym e n t . 
s u c c e e d e d " ,
" o rd e r_ id " : o rd e r [ " 
id " ] ,
" am o u n t _ c e n t s " : 1 
2 0 0 ,
})
paym en ts = se lf.conn .execu 
te (
"SELECT am oun t_cen ts , re 
fund_ requ ired_cen ts FROM
paymentsWHEREorder_id=?ORDERBY 
id",
(o rd e r [ " id " ] , ) ,
).fe tcha ll()
se lf.assertEqua l(len(paym 
ents),2)
s e l f . a s s e r t E q u a l 
( p a ym e n t s [ 0 ] [ " r e 
f u n d _ r e q u i r e d _ c e 
n t s " ] , 0 )
se lf.assertEqua l(paym 
ents[1]["refund_requ 
ired_cents"],
1200)
i f _ _ n am e _ _ = = " _ _m a 
in _ _ " :
u n i t t e s t .m a i n ( )
ChatGPT
You
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 3 s
FAILED (errors=1)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
5/25

You
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ s e c o n d _ p a y m 
e n t _ i s _ f l a g g
ed_for_refund -v
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_for_refund) ...ERROR
================================================
======================
E R R O R : te s t_ s e c o n d 
_ p a ym e n t_ is _ f la g g e 
d _ fo r_ re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund )
-----------------------------------------------------------------
-----
T r a c e b a c k (m o s t r e 
c e n t c a l l l a s t ) :
F ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
s.py",line145,in 
test_second_payment_is_flagged_for_refund
paym en ts = se lf.conn .execu 
te (
~~~~~~~~~~~~~~~~~^
"SELECT am oun t_cen ts , re 
fund_ requ ired_cen ts FROM
paymentsWHEREorder_id=?ORDERBY 
id",
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(o rd e r [ " id " ] , ) ,
^^^^^^^^^^^^^^^
).fe tcha ll()
^
s q l i t e 3 .O p e r a t i o 
n a l E r r o r : n o s u c h c 
o l u m n : r e f u n d _ r e q 
u i r e d _ c e n t s
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 3 s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
6 / 25
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
6/25

7 / 25
  FAILED (errors=1)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
"""SQLitestorage.Allmoney is 
integercents;alltimestampsare
U T C IS O - 8 6 0 1 s t r in g 
s ." " "
im p o r t s q l i t e 3
from datetime 
importdatetime,timezone
S C H EM A = " " "
CREATETABLE 
IFNOTEXISTSproducts(
s k u T E X T P R IM A R Y K E 
Y ,
n am e T E X T N O T N U L L ,
price_cents INTEGERNOTNULL,
stock INTEGERNOTNULLDEFAULT0
);
CREATETABLE IFNOTEXISTScoupons(
c o d e T E X T P R IM A R Y K 
E Y ,
kindTEXTNOTNULLCHECK (kind IN 
('percent','fixed')),
value INTEGERNOTNULL,
m in_subtotal_cents 
INTEGERNOTNULLDEFAULT0,
m a x _ u s e s IN T E G E R ,
uses INTEGERNOTNULLDEFAULT0
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
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
7/25

8 / 25
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
8/25

ChatGPT
You
waitartham kalaaekkadaem 
addcheyyali
ChatGPT
You
ha
ChatGPT
You
"""SQLitestorage.Allmoney is 
integercents;alltimestampsare
U T C IS O - 8 6 0 1 s t r in g 
s ." " "
im p o r t s q l i t e 3
from datetime 
importdatetime,timezone
S C H EM A = " " "
CREATETABLE 
IFNOTEXISTSproducts(
s k u T E X T P R IM A R Y K E 
Y ,
n am e T E X T N O T N U L L ,
price_cents INTEGERNOTNULL,
stock INTEGERNOTNULLDEFAULT0
);
CREATETABLE IFNOTEXISTScoupons(
c o d e T E X T P R IM A R Y K 
E Y ,
kindTEXTNOTNULLCHECK (kind IN 
('percent','fixed')),
value INTEGERNOTNULL,
m in_subtotal_cents 
INTEGERNOTNULLDEFAULT0,
m a x _ u s e s IN T E G E R ,
uses INTEGERNOTNULLDEFAULT0
);
9 / 25
        Takeyourcuriosity 
further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
9/25

10 / 25
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
refund_required_cents 
INTEGERNOTNULLDEFAULT0,
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
10/25

11 / 25
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
ChatGPT
You
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
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ s e c o n d _ p a y m 
e n t _ i s _ f l a g g
ed_for_refund -v
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
11/25

ed_for_refund) ...ERROR
================================================
======================
E R R O R : te s t_ s e c o n d 
_ p a ym e n t_ is _ f la g g e 
d _ fo r_ re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund )
-----------------------------------------------------------------
-----
T r a c e b a c k (m o s t r e 
c e n t c a l l l a s t ) :
F ile
" /U s e rs /d e e p th i /D ow 
n lo a d s / t i l lp o in t_ a 
s s ig nm e n t / te s ts / te 
s t_ o rd e r
s.py",line145,in 
test_second_payment_is_flagged_for_refund
paym en ts = se lf.conn .execu 
te (
~~~~~~~~~~~~~~~~~^
"SELECT am oun t_cen ts , re 
fund_ requ ired_cen ts FROM
paymentsWHEREorder_id=?ORDERBY 
id",
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(o rd e r [ " id " ] , ) ,
^^^^^^^^^^^^^^^
).fe tcha ll()
^
s q l i t e 3 .O p e r a t i o 
n a l E r r o r : n o s u c h c 
o l u m n : r e f u n d _ r e q 
u i r e d _ c e n t s
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 3 s
FAILED (errors=1)
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
12 / 25
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
12/25

13 / 25
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
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
13/25

14 / 25
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
FAILED (errors=1)
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
e x is t in g = s e l f .c o n 
n .e x e c u te (
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
14/25

15 / 25
  " S E L E C T 1 F R O M p a 
ym e n t s W H E R E e v e n t 
_ id = ? " ,
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
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-c"from 
tillpointimportdb;c=db.connect();print([r['name']forr
inc.execute('PRAGMA 
table_info(payments)')])"
['id ', 'o rde r_ id ', 'even 
t_ id ', 'am oun t_cen ts ',
're fund_ requ ired_cen ts ', 
'rece ived_a t']
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
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
15/25

16 / 25
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
p r e v io u s _ p a id = s e l 
f .p a id _ c e n t s ( o r d e 
r [ " id " ] )
am oun t= even t["am oun t_cen 
ts"]
re fund_ requ ired =m ax (
0,
p re v io u s _ p a id + am o u 
n t - o rd e r [ " to ta l_ c e 
n ts " ]
)-max(0,previous_paid 
-order["total_cents"])
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
16/25

17 / 25
  se lf.conn .execu te (
"""INSERT INTOpayments
(o rde r_ id ,even t_ id ,am 
oun t_cen ts ,
re fund_ requ ired_cen ts , 
rece ived_a t)
VALUES (?,?,?,?,?)""",
(
order["id"],
event["id"],
am o u n t ,
re fund_ requ ired ,
db .to_ iso (now o rdb .u tcnow 
()),
),
),
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
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
17/25

18 / 25
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
o rde r= se lf.conn .execu te (
"SELECT *FROM ordersWHERE id= 
?",
( e v e n t [ " o r d e r _ id 
" ] , )
) . fe tc h o n e ( )
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
p r e v io u s _ p a id = s e l 
f .p a id _ c e n t s ( o r d e 
r [ " id " ] )
am oun t= even t["am oun t_cen 
ts"]
re fund_ requ ired =m ax (
0,
p re v io u s _ p a id + am o u 
n t - o rd e r [ " to ta l_ c e 
n ts " ]
)-max(0,previous_paid 
-order["total_cents"])
se lf.conn .execu te (
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
18/25

19 / 25
  """INSERT INTOpayments
(o rde r_ id ,even t_ id ,am 
oun t_cen ts ,
re fund_ requ ired_cen ts , 
rece ived_a t)
VALUES (?,?,?,?,?)""",
(
order["id"],
event["id"],
am o u n t ,
re fund_ requ ired ,
db .to_ iso (now o rdb .u tcnow 
()),
),
)
iforder["status"]== "pend 
ing"and
se lf.pa 
id_cents(order["id"])>= 
order["tota l_cents"]:
se lf.conn .execu te (
"UPDATEordersSETstatus= 
'paid'WHERE id=?",
(o rd e r [ " id " ] , ) ,
)
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
ChatGPT
You
--------------------
R a n 1 te s t in 0 .0 0 2 s
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
19/25

20 / 25
  OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
-----------------------------------------------------------------
-----
Ran13 tests in0.008s
OK
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
_ c e n t s ( s e l f , o r d e 
r _ id ) :
row = se lf.conn .execu te (
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-c"from 
tillpointimportdb;c=db.connect();print([r['name']forr
inc.execute('PRAGMA 
table_info(payments)')])"
['id ', 'o rde r_ id ', 'even 
t_ id ', 'am oun t_cen ts ',
're fund_ requ ired_cen ts ', 
'rece ived_a t']
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ s e c o n d _ p a y m 
e n t _ i s _ f l a g g
ed_for_refund -v
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund ) ...ok
-----------------------------------------------------------------
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
     
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
20/25

21 / 25
 -----
R a n 1 te s t in 0 .0 0 2 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest-v
te s t_ c a n c e l_ p a id _ o 
rd e r_ re s to c k s
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_cance l_pa 
id_o rde r_ res toc
ks) ...ok
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
tes t_coupon_ reduces_ taxab 
le_am oun t
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
reduces_ taxab le_
am o u n t ) . . . o k
tes t_coupon_ takes_ ten_pe 
rcen t
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
takes_ ten_pe rce
n t) ...ok
test_da ily_sa les
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s ) . . . o k
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e) ...ok
te s t_ d u p l ic a te _ p a 
ym e n t_ e v e n t_ is _ ig n 
o re d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d u p l i c a t e _ 
p a y m e n t _ e v e n t
_ is_ igno red ) ...ok
test_order_totals_w ith_tax
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_o rde r_ to 
ta ls_w ith_ tax )
...ok
te s t_ o u t_ o f_ s to c k
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_ou t_o f_s 
tock ) ...ok
tes t_paym en t_m a rks_o rde 
r_pa id
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ p a y m e n t _ m a 
r k s _ o r d e r _ p a
id ) . . . o k
te s t_ p r ic e _ c h a n g e
(tests.test_orders.O 
rderDeskTest.test_price_change) 
...ok
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund ) ...ok
tes t_s ta le_ca ta 
log_cache_does_no t_ove rse ll
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
21/25

22 / 25
  (tes ts .tes t_o rde rs .O 
rde rD eskTes t.tes t_s ta 
le_ca ta log_cache_does
_no t_ove rse ll) ...ok
-----------------------------------------------------------------
-----
Ran13 tests in0.008s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
s ta tu s - - s h o r t
M tes ts /tes t_o rde rs .py
M t i l lp o in t /d b .p y
M t i l lp o in t /p a ym e n 
ts .p y
?? .DS_Store
? ? s e s s io n _ lo g s / .D 
S _ S to re
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
ChatGPT
You
vent_id,amount_cents,received_at)VALUES 
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
"SELECTCOALESCE(SUM 
(amount_cents),0)ASpaid
FROM 
paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
    
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
22/25

23 / 25
 -c"from 
tillpointimportdb;c=db.connect();print([r['name']forr
inc.execute('PRAGMA 
table_info(payments)')])"
['id ', 'o rde r_ id ', 'even 
t_ id ', 'am oun t_cen ts ',
're fund_ requ ired_cen ts ', 
'rece ived_a t']
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest
t e s t s . t e s t _ o r d e r 
s .O r d e r D e s k T e s t . 
t e s t _ s e c o n d _ p a y m 
e n t _ i s _ f l a g g
ed_for_refund -v
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund ) ...ok
-----------------------------------------------------------------
-----
R a n 1 te s t in 0 .0 0 2 s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
python3
-m unittest-v
te s t_ c a n c e l_ p a id _ o 
rd e r_ re s to c k s
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_cance l_pa 
id_o rde r_ res toc
ks) ...ok
tes t_cance l_pend ing_o rde r_ 
res tocks
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ c a n c e l _ p e n 
d i n g _ o r d e r _ r e
stocks) ...ok
tes t_coupon_ reduces_ taxab 
le_am oun t
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
reduces_ taxab le_
am o u n t ) . . . o k
tes t_coupon_ takes_ ten_pe 
rcen t
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_coupon_ 
takes_ ten_pe rce
n t) ...ok
test_da ily_sa les
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s ) . . . o k
t e s t _ d a i l y _ s a l e s 
_ i n d i a _ t im e z o n e
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d a i l y _ s a l e 
s _ i n d i a _ t im e z o n
e) ...ok
te s t_ d u p l ic a te _ p a 
ym e n t_ e v e n t_ is _ ig n 
o re d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ d u p l i c a t e _ 
p a y m e n t _ e v e n t
_ is_ igno red ) ...ok
test_order_totals_w ith_tax
Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
   
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
23/25

(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_o rde r_ to 
ta ls_w ith_ tax )
...ok
te s t_ o u t_ o f_ s to c k
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_ou t_o f_s 
tock ) ...ok
tes t_paym en t_m a rks_o rde 
r_pa id
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ p a y m e n t _ m a 
r k s _ o r d e r _ p a
id ) . . . o k
te s t_ p r ic e _ c h a n g e
(tests.test_orders.O 
rderDeskTest.test_price_change) 
...ok
te s t_ s e c o n d _ p a ym e 
n t_ is _ f la g g e d _ fo r_ 
re fu n d
( t e s t s . t e s t _ o r d e 
r s .O r d e r D e s k T e s t 
. t e s t _ s e c o n d _ p a y 
m e n t _ i s _ f l a g g
ed_ fo r_ re fund ) ...ok
tes t_s ta le_ca ta 
log_cache_does_no t_ove rse ll
(tes ts .tes t_o rde rs .O rde 
rD eskTes t.tes t_s ta le_ca ta 
log_cache_does
_no t_ove rse ll) ...ok
-----------------------------------------------------------------
-----
Ran13 tests in0.008s
OK
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
s ta tu s - - s h o r t
M tes ts /tes t_o rde rs .py
M t i llpo in t /d b .p y
M t i llpo in t /p a ym en ts 
.py
?? .DS_Store
? ? s e s s io n _ lo g s / .D 
S _ S to re
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
gitadd
tests/test_orders.py 
tillpoint/db.py 
tillpoint/payments.py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% 
git
comm it-m 
"Flagduplicatepaymentsforrefund"
[m a i n 4 a 0 a 1 f c ] F l a 
g d u p l i c a t e p a y m e n 
t s f o r r e f u n d
3 fileschanged,57 
insertions(+),4deletions(-)
d e e p t h i@ D e e p t h i s 
- M a c B o o k - A i r t i l l 
p o i n t _ a s s i g n m e n t 
%
Worked for7s
ChatGPT
24 / 25
    Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
24/25

You
25 / 25
  d e f c o n n e c t ( p a t h 
= " :m e m o r y : " ) :
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
ChatGPT
   Takeyourcuriosity further
S c a n to g e t th e C h a tG 
P T a p p
https://chatgpt.com/c/6b026ac4-3be8-83ee-b346-0972787f6523
25/25

