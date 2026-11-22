ChatGPT
G o o d ! re c e iv e d .✅
catalog.py
S tep 2 :C a ta log ana lys is
I f o u n d t w o im p o r t a n t a r e a s t o i n v e s t i g a t e .
1.Inventory issue
reserve()
1 / 35
  t i l lp o in
  In
:
product = self.get_product(sku)
if product.stock < qty:
    raise OutOfStock(sku, qty, product.stock)
self.conn.execute(
    "UPDATE products SET stock = stock - ? WHERE sku = ?",
    (qty, sku)
)
Thestock ischecked firstandupdatedseparately.
Iftwoworkerscheckstocksimultaneously,bothm ightsee thesameavailablequantityand
bothdeductstock.This isapotentialrootcauseofReport5.
2 .Read cache
self._cache
s t o r e s p r o d u c t i n f o rm a t i o n s e p a r a t e l y i n e a c h p r o c e s s . D i f f e r e n t w o r k e r s m a y
haveoutdatedstock information.
W e n e e d t e s t s t o c o n f i rm b o t h b e h a v i o u r s b e f o r e f i x i n g t h e m .
N e x t f i le :
orders.py
Open :
     Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
1/35

2 / 35
  tillpoint → orders.py
P a s te th e c om p le te c o d e h e re .
This file isparticularly importantforReport2becauseweneed tounderstandwhenstock is
reservedandwhen itisreleasedaftercancellationorabandonedcheckout.
Progress:4 filesreceived.Let'scontinue.💻
You
"""Productcatalogw ithaper-processreadcache."""
from dataclasses importdataclass
c la s s O u tO fS to c k (E x c e p t io n ) :
de f__ in it__ (se lf,sku ,w an ted ,ava ilab le ):
super().__init__(f"{sku}:wanted {wanted},{available}
a v a i la b le " )
se lf.sku ,se lf.w an ted ,se lf.ava ilab le = sku ,w an ted ,ava ilab le
c la s s U n k n ow n P ro d u c t (E x c e p t io n ) :
pass
@ d a ta c la s s ( f ro z e n = T ru e )
c la s s P ro d u c t :
sku :str
n am e : s t r
p r ic e _ c e n t s : in t
s to c k : in t
c la s s C a ta lo g :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
self._cache= {}
d e f a d d _ p r o d u c t ( s e l f , s k u , n am e , p r ic e _ c e n t s , s t o c k = 0 ) :
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
    https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
2/35

3 / 35
 se lf.conn .execu te (
"INSERT INTOproducts(sku,name,price_cents,stock)
VALUES (?,?,?,?)",
(s k u , n am e , p r ic e _ c e n ts , s to c k ) ,
)
se lf._cache .pop (sku ,N one )
de fge t_p roduc t(se lf,sku ):
p roduc t= se lf._cache .ge t(sku )
i f p ro d u c t is N o n e :
row = se lf.conn .execu te ("SELECT * FROM p roduc ts
W H E R E s k u = ? " , ( s k u , ) ) . fe tc h o n e ( )
if row is N o n e:
ra is e U n k n ow n P ro d u c t (s k u )
p ro d u c t = P ro d u c t ( row [ " s k u " ] , row [ " n am e " ] ,
row ["price_cents"],row ["stock"])
se lf._cache [sku ]= p roduc t
returnproduct
d e f u p d a t e _ p r ic e ( s e l f , s k u , p r ic e _ c e n t s ) :
i f p r ic e _ c e n t s < 0 :
r a is e V a lu e E r ro r ( " p r ic e m u s t n o t b e n e g a t iv e " )
c u r = s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T p r ic e _ c e n ts
= ?W H E R E s k u = ? " , (p r ic e _ c e n ts , s k u ) )
ifcu r.row coun t== 0 :
ra is e U n k n ow n P ro d u c t (s k u )
se lf._cache .pop (sku ,N one )
de f rese rve (se lf,sku ,q ty ):
" " " T a k e q t y u n i t s o u t o f s t o c k , o r r a i s e O u tO f S t o c k . " " "
p roduc t= se lf.ge t_p roduc t(sku )
if p ro d u c t .s to c k < q ty :
r a i s e O u tO f S t o c k ( s k u , q t y , p r o d u c t . s t o c k )
s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T s to c k = s to c k - ?
W H E R E s k u = ? " , (q ty , s k u ) )
se lf._cache .pop (sku ,N one )
d e f r e le a s e ( s e l f , s k u , q t y ) :
"""Putqtyunitsback intostock."""
s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T s to c k = s to c k + ?
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
3/35

W H E R E s k u = ? " , (q ty , s k u ) )
se lf._cache .pop (sku ,N one )
ChatGPT
K e e r th i , id i s am e
catalog.py
codemallivachindi.Noproblem .😊
C a t a l o g a n a l y s i s l o im p o r t a n t p o i n t s :
1. lo s to c k c h e c k a n d s to c k d e d u c t io n s e p a ra te o p e ra t io n s g a u n n a y i .
reserve()
Concurrentworkersvallaoverselling jarigepossibilityundi.
2. per-processkabatti,d ifferentworkersdaggarastockvaluesstalegaundochu.
_cache
3. lostock increasechestunnam ,butstock lim itsvalidation ledu.
release()
Ivipotentialissuesmaatrame;testsand remaining fileschusaka finalrootcausesconfirm
cheddam .
N e x t : o p e n c h e s i c om p le te c o d e p a s te c h e y y i . n i
tillpoint/orders.py
catalog.py ippudu ed itcheyyaku .
You
a s s a lm a n a g o a l e n t i
ChatGPT
ManamaingoalentianteDeepKlarityBackend InternshipAssessmentcompletechesi,
workingprojectnicorrectgasubm itcheyyadam .
Manam buildcheyyalsinanewprojectkaadu.Already ichinaTillpointapplication lo6bugs
identifychesi,fixchesi,tests thoprovecheyyali.
A s s ig nm e n t lo 6 p ro b lem s
# Problem Managoal
1 Revenue and paym en tm ism a tch Paym en tca lcu la tions co rrec tcheyya li
2 Stockwronggadisplayavvadam Productstockaccuracyfixcheyyali
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
4 / 35
                  https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
4/35

5 / 35
   3 Coupon + taxw rong ca lcu la tion Tax ca lcu la tion co rrec tcheyya li
  4 I n d i a r e p o r t s p r e v i o u s d a y T im e z o n e / d a t e i s s u e f i x c h e y y a l i
chup inchadam
5 Multipleworkersvallaoverselling Concurrentstockupdatessafecheyyali
6 Customerdoublepayment Duplicategenuinepaymentskiproperhandling implement
cheyya li
M anam fo llow avva ls ina p rocess
1 . E x is t in g c o d e u n d e rs ta n d c h e y y a l i .
2.Eachbugkirootcause identifycheyyali.
3.Bug reproducecheyyali.
4.Fix implementcheyyali.
5.Prathifixkiautomated regression testwritecheyyali.
6.PrathifixkiseparateG itcomm itcheyyali.
7 . com p le te cheyya li.
NOTES.md
8 . C h a tG P T c o n v e r s a t io n n i lo s a v e c h e y y a l i .
session_logs/
9.CompleteprojectniZIPchesisubm itcheyyali.
ImportantAssignmentloAIsession logski70marks,codeki30marks.Kabattimanam
chesinaworkand reasoningnihonestgadocumentcheyyali.
Ippudum anam ekkada unnam ?
server.py
— reviewed
README.md
— reviewed
db.py
— reviewed
catalog.py
— reviewed
orders.py
— next
Mana immediatetarget:Firstexistingcodemotham understandcheskundam .Tarvatha
bugsnionebyone fixcheddam .Appudu random gacodechangecheyyalsinaavasaram
undadu .
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
               https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
5/35

You
ippudu nenu ca ta log lo code rayaa
ChatGPT
Ledu . Ippudu
catalog.py
lo code change cheyyaku .
6 / 35
   Firstexisting filesanniinspectcheddam .Rootcauseconfirm ayyaka,exactcodeekkada
c h a n g e c h e y y a lo n e n u s t e p - b y - s t e p c h e p t h a n u .
orders.py
 Ippudu
You
o p e n c h e s i c om p le te c o d e p a s te c h e y y i .
 """Productcatalogw ithaper-processreadcache."""
from dataclasses importdataclass
c la s s O u tO fS to c k (E x c e p t io n ) :
de f__ in it__ (se lf,sku ,w an ted ,ava ilab le ):
super().__init__(f"{sku}:wanted {wanted},{available}
a v a i la b le " )
se lf.sku ,se lf.w an ted ,se lf.ava ilab le = sku ,w an ted ,ava ilab le
c la s s U n k n ow n P ro d u c t (E x c e p t io n ) :
pass
@ d a ta c la s s ( f ro z e n = T ru e )
c la s s P ro d u c t :
sku :str
n am e : s t r
p r ic e _ c e n t s : in t
s to c k : in t
c la s s C a ta lo g :
de f__ in it__ (se lf,conn ):
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
6/35

7 / 35
 se lf.conn = conn
self._cache= {}
d e f a d d _ p r o d u c t ( s e l f , s k u , n am e , p r ic e _ c e n t s , s t o c k = 0 ) :
se lf.conn .execu te (
"INSERT INTOproducts(sku,name,price_cents,stock)
VALUES (?,?,?,?)",
(s k u , n am e , p r ic e _ c e n ts , s to c k ) ,
)
se lf._cache .pop (sku ,N one )
de fge t_p roduc t(se lf,sku ):
p roduc t= se lf._cache .ge t(sku )
i f p ro d u c t is N o n e :
row = se lf.conn .execu te ("SELECT * FROM p roduc ts
W H E R E s k u = ? " , ( s k u , ) ) . fe tc h o n e ( )
if row is N o n e:
ra is e U n k n ow n P ro d u c t (s k u )
p ro d u c t = P ro d u c t ( row [ " s k u " ] , row [ " n am e " ] ,
row ["price_cents"],row ["stock"])
se lf._cache [sku ]= p roduc t
returnproduct
d e f u p d a t e _ p r ic e ( s e l f , s k u , p r ic e _ c e n t s ) :
i f p r ic e _ c e n t s < 0 :
r a is e V a lu e E r ro r ( " p r ic e m u s t n o t b e n e g a t iv e " )
c u r = s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T p r ic e _ c e n ts
= ?W H E R E s k u = ? " , (p r ic e _ c e n ts , s k u ) )
ifcu r.row coun t== 0 :
ra is e U n k n ow n P ro d u c t (s k u )
se lf._cache .pop (sku ,N one )
de f rese rve (se lf,sku ,q ty ):
" " " T a k e q t y u n i t s o u t o f s t o c k , o r r a i s e O u tO f S t o c k . " " "
p roduc t= se lf.ge t_p roduc t(sku )
if p ro d u c t .s to c k < q ty :
r a i s e O u tO f S t o c k ( s k u , q t y , p r o d u c t . s t o c k )
s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T s to c k = s to c k - ?
W H E R E s k u = ? " , (q ty , s k u ) )
se lf._cache .pop (sku ,N one )
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
7/35

id h i a n th a c o r re c t a n a
ChatGPT
Avunu ,nuvvu pas te ches ina
g a k a n ip is to n d i .
catalog.py
8 / 35
  d e f r e le a s e ( s e l f , s k u , q t y ) :
"""Putqtyunitsback intostock."""
s e l f .c o n n .e x e c u te ( "U P D A T E p ro d u c ts S E T s to c k = s to c k + ?
W H E R E s k u = ? " , (q ty , s k u ) )
se lf._cache .pop (sku ,N one )
 codecompletegaundi.Syntax-w isekudacorrect
Kaaniassignmentprakaram codecorrectaniconfirm cheyyalem .Indulopotentialbugs
unnay i:
1. lostockcheckanddeductionseparatega jarugutunnayi— concurrent
reserve()
w o rke rs va lla ove rse lling avvachu .
2 . pe r-p rocess kaba tt id iffe ren tw o rke rs dagga ra ou tda ted s tock undochu .
_cache
3. loquantityvalidation ledu.
release()
Ippudu ee code lo em change cheyyaku .
Next
orders.py
opencheyyi.Completecodepastecheyyi.Rootcauseconfirm chesi
tarvatha fixstartcheddam .
You
"""Creating,cancellingand listingorders."""
f r o m . im p o r t d b , p r i c i n g
from .catalog importCatalog
c la s s O rd e rE r ro r (E x c e p t io n ) :
pass
c lassO rde rs :
d e f _ _ in i t _ _ ( s e l f , c o n n , c a t a lo g = N o n e ) :
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
        https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
8/35

9 / 35
 se lf.conn = conn
se lf.ca ta log = ca ta log o rC a ta log (conn )
defcreate(se lf,custom er, item s,reg ion="NONE",
c o u p o n _ c o d e = N o n e , n ow = N o n e ) :
"""items:listof(sku,qty).Reservesstock,redeems the
c o u p o n a n d s to re s th e o rd e r , a l l o r n o th in g ." " "
ifno t item s :
raiseOrderError("anorderneedsatleastone item")
ifany(qty<=0 for_,qty in items):
raiseO rderError("quantitiesmustbepositive")
self.conn.execute("BEGIN IMMEDIATE")
try:
coupon = se lf._coupon (coupon_code )
priced= [(sku,qty,
self.catalog.get_product(sku).price_cents)forsku,qty in items]
totals=pricing.price_order([(price,qty)for_,qty,price in
p r ic e d ] , re g io n , c o u p o n )
forsku,qty,_ inpriced:
se lf.ca ta log .rese rve (sku ,q ty )
ifcoupon isnotNone:
s e l f .c o n n .e x e c u te ( "U P D A T E c o u p o n s S E T u s e s = u s e s +
1W H E R E c o d e = ? " , (c o u p o n _ c o d e , ) )
cu r= se lf.conn .execu te (
"INSERT INTOorders(customer,region,coupon,
sub to ta l_cen ts ,d iscoun t_cen ts , tax_cen ts ,"
"total_cents,created_at)VALUES (?,?,?,?,?,?,?,?)",
(c u s tom e r , re g io n , c o u p o n _ c o d e ,
totals["subtotal_cents"],totals["d iscount_cents"],
to ta ls [ " ta x _ c e n ts " ] , to ta ls [ " to ta l_ c e n ts " ] ,
db .to_ iso (now o rdb .u tcnow ())),
)
order_id=cur.lastrow id
se lf.conn .execu tem any (
"INSERT INTOorder_items(order_id,sku,qty,
unit_price_cents)VALUES (?,?,?,?)",
[(order_id,sku,qty,price)forsku,qty,price inpriced],
)
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
9/35

10 / 35
 se lf.conn .execu te ("RO LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id )
d e f c a n c e l ( s e l f , o r d e r _ id ) :
"""Cancelanorderthathasnotshipped.Itsstockand its
coupon use go back ."""
o rde r= se lf.ge t(o rde r_ id )
iforder["status"]== "cance lled":
re tu rn o rd e r
iforder["status"]== "sh ipped":
ra is e O rd e rE r ro r ( " a s h ip p e d o rd e r c a n n o t b e c a n c e l le d " )
self.conn.execute("BEGIN IMMEDIATE")
try:
i f o r d e r [ " s t a t u s " ] = = " p a id " :
fo r i tem in o rd e r [ " i tem s " ] :
self.catalog.release(item ["sku"],item ["qty"])
i f o rd e r [ " c o u p o n " ] :
s e l f .c o n n .e x e c u te ( "U P D A T E c o u p o n s S E T u s e s = u s e s -
1W H E R E c o d e = ? A N D u s e s > 0 " , (o rd e r [ " c o u p o n " ] , ) )
self.conn.execute("UPDATEordersSET status=
'cancelled'WHERE id=?",(order_id,))
self.conn.execute("COMM IT")
e x c e p t E x c e p t io n :
se lf.conn .execu te ("RO LLBACK ")
ra ise
re tu rn se lf.ge t(o rde r_ id )
d e f s h ip ( s e l f , o r d e r _ id ) :
o rde r= se lf.ge t(o rde r_ id )
iforder["status"] != "pa id":
r a i s e O r d e r E r r o r ( " o n l y a p a id o r d e r c a n s h ip " )
self.conn.execute("UPDATEordersSETstatus= 'shipped'
WHERE id=?",(order_id,))
re tu rn se lf.ge t(o rde r_ id )
d e f g e t ( s e l f , o r d e r _ id ) :
row=self.conn.execute("SELECT*FROM ordersWHERE id
= ? " , ( o r d e r _ id , ) ) . f e t c h o n e ( )
if row is N o n e :
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
10/35

ra iseO rde rE rro r(f"no o rde r {o rde r_ id }")
o rd e r = d ic t ( row )
order["items"]= [dict(r)forrinself.conn.execute(
"SELECTsku,qty,unit_price_centsFROM order_items
WHEREorder_id=?ORDERBY row id",(order_id,))]
re tu rn o rd e r
d e f l is t_ fo r ( s e l f , c u s tom e r , p a g e = 1 , p e r_ p a g e = 2 0 ) :
row s = se lf.conn .execu te (
"SELECT idFROM ordersWHEREcustomer=?ORDERBY
c r e a t e d _ a t D E S C , i d D E S C L IM I T ? O F F S E T ? " ,
(c u s tom e r , p e r_ p a g e , (p a g e - 1 ) * p e r_ p a g e ) ,
).fe tcha ll()
return [self.get(r["id"])forr in rows]
def_coupon(se lf,code):
ifcode isNone:
re tu rn N o n e
row=self.conn.execute("SELECT*FROM couponsWHERE
code= ?",(code,)).fetchone()
if row is N o n e :
raisepricing.CouponRejected(f"unknowncoupon {code}")
re tu rn row
ChatGPT
Exce llen t! code rece ived . Ippudu im po rtan tobse rva tions unnay i.
orders.py
orders.py
ana lys is
1.Stock reservation
self.conn.execute("BEGIN IMMEDIATE")
Good :O rdercreation transaction startchestond i.SQL ite lo
w r i te s n i s e r ia l iz e c h e y y a d a n ik i h e lp c h e s tu n d i .
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
BEGIN IMMEDIATE
11 / 35
     concurrent
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
11/35

2 .Abandoned checkou t
O rde rc rea te ches inappude s tock rese rve ches tunna ru :
self.catalog.reserve(sku, qty)
Pendingorderskistockreleaseavuthundo ledo investigatecheyyali.Report2kiidi
im p o r t a n t .
3 .Coupon usage
Couponusage incrementchestunnaru,cancellation lodecrementchestunnaru.Coupon
lim itsandconcurrentusageni thokalipiinspectcheyyali.
pricing.py
4 . C a n c e l la t io n
Orderstatuschecktransactionstartavvakamundu jarugutondi.Concurrent
cancellation/paymentsituations lopossible raceundochu.
N e x t f i le :
payments.py
payments.py
o p e n c h e s i c om p le te c o d e p a s te c h e y y i .
I d i R e p o r t s 1 a n d 6 k i v e r y im p o r t a n t :
P a ym e n t re c e iv e d am o u n t v s o rd e r to ta l
Dup licatewebhookevents
C u s tom e r g e n u in e ly tw ic e p a y c h e s in a p p u d u h a n d l in g
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
12 / 35
  So, lo raceconditionpossibilityundanicheppina,ordercreationcontextloee
catalog.py
t r a n s a c t i o n p r o t e c t i o n k u d a c o n s i d e r c h e y y a l i . F i n a l r o o t c a u s e n i t e s t s t h o c o n f i rm
cheddam .
 K a a n i o rd e r c a n c e l a y in a p p u d e s to c k re le a s e c h e s tu n n a ru , a d i k u d a
m aa tram e .
paid
s ta tu s k i
       https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
12/35

13 / 35
 Rem inder:Ippativarakucodeeditcheyyaku.Firstallfiles inspectchesi,tarvatha fixesand
testsonebyonecheddam .
You
" " " P a ym e n t p r o v id e r w e b h o o k s . T h e p r o v id e r r e t r ie s a d e l iv e r y
untilitgetsa2xx,soeventscan repeat."""
from .importdb
c la s s P a ym e n tE r ro r (E x c e p t io n ) :
pass
c la s s P a ym e n ts :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
d e f h a n d le _ e v e n t ( s e l f , e v e n t , n o w = N o n e ) :
" " " e v e n t : d ic t ( id , ty p e , o rd e r_ id , am o u n t_ c e n ts ) . R e tu rn s th e
o rd e r 's s ta tu s a f te r th e e v e n t ." " "
i f e v e n t .g e t ( " t y p e " ) != " p a ym e n t . s u c c e e d e d " :
re tu rn N o n e
order=self.conn.execute("SELECT*FROM ordersWHERE
id = ? " , ( e v e n t [ " o r d e r _ id " ] , ) ) . f e t c h o n e ( )
i f o rd e r is N o n e :
ra ise Paym en tE rro r(f"paym en t fo runknow n o rde r
{e v e n t [ 'o rd e r_ id ' ] } " )
iforder["status"]== "cance lled":
raisePaymentError(f"order{order['id']} iscancelled")
se lf.conn .execu te (
"INSERT INTOpayments(order_id,event_id,
amount_cents,received_at)VALUES (?,?,?,?)",
(o rd e r [ " id " ] , e v e n t [ " id " ] , e v e n t [ " am o u n t_ c e n ts " ] ,
db .to_ iso (now o rdb .u tcnow ())),
)
iforder["status"]== "pend ing"and
se lf.pa id_cents(order["id"])>= order["tota l_cents"]:
self.conn.execute("UPDATEordersSETstatus= 'paid'
WHERE id=?",(order["id"],))
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
13/35

re tu rn "p a id "
re tu rn o rd e r [ " s ta tu s " ]
d e f p a id _ c e n t s ( s e l f , o r d e r _ id ) :
row = se lf.conn .execu te (
"SELECTCOALESCE(SUM (amount_cents),0)ASpaid
FROM paymentsWHEREorder_id=?",(order_id,)
) . fe tc h o n e ( )
re tu rn row ["p a id " ]
ChatGPT
Good! received.Thisfile isvery importantforReports1and6.
payments.py
Paym en ts ana lys is
Ifound threepotentialissues.
1 .D u p l ic a te w e b h o o k d e l iv e ry
INSERT INTO payments (order_id, event_id, amount_cents, received_at)
S am e e v e n t
id event_id mallireceiveayithe,anotherpaymentrecord insertavuthundi. ki
uniqueprotection ledu.
2 . P a ym e n t am o u n t v a l id a t io n
if order["status"] == "pending" and self.paid_cents(order["id"]) >=
order["total_cents"]:
paid
14 / 35
     O rde r to ta lkanna ekkuva am oun t rece ive ay ina ,o rde r
hand ling ledu .
3 .G e n u in e d o u b le p a ym e n t
a v u th u n d i . E x t ra am o u n t
Customersameorderkigenuinely twoseparatepaymentschesthe,rendu recordsstore
avu thay i.Ex tra paym en tn ie la hand le cheyya lo ass ignm en t lo dec is ion teesukova li.
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
14/35

15 / 35
  N e x t f i le :
pricing.py
O p e n a n d p a s te th e c om p le te c o d e .
tillpoint → pricing.py
IdiReport3— couponapplychesinappudu taxcalculation issue— investigatecheyyadaniki
avasaram .
Currentstatus:6 files lo5mainmodules inspectchestunnam .Inka fixesstartcheyyaledu.
You
" " "O rd e rm a th s : s u b to ta l , c o u p o n d is c o u n t , ta x , to ta l . In te g e r
cen ts th roughou t."""
#Salestax inbasispoints(1/100ofapercent)byregion.
TAX_BPS= {"NONE":0,"CA":725,"NY":888,"TX":625,"DE":
1900}
c la s s C o u p o n R e je c te d (E x c e p t io n ) :
pass
d e f s u b t o t a l ( l in e s ) :
"""lines: iterab leof(un it_price_cents,qty)."""
re tu rn s um (p r ic e * q ty fo r p r ic e , q ty in l in e s )
d e f d is c o u n t_ fo r (c o u p o n , s u b to ta l_ c e n ts ) :
"""Discountincentsforacouponrow (orNone)againsta
subtotal.Nevermore than thesubtotal."""
ifcoupon isNone:
re tu rn 0
ifsubtotal_cents<coupon["m in_subtotal_cents"]:
ra iseCouponRe jec ted (f"{coupon ['code ']}needs a sub to ta l
ofatleast{coupon['m in_subtotal_cents']}")
i f c o u p o n [ "m a x _ u s e s " ] is n o t N o n e a n d c o u p o n [ " u s e s " ] > =
c o u p o n [ "m a x _ u s e s " ] :
ra is e C o u p o n R e je c te d ( f " {c o u p o n [ 'c o d e ' ] } h a s b e e n u s e d
up")
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
     https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
15/35

16 / 35
  i f c o u p o n [ " k in d " ] = = " p e r c e n t " :
amount= round_half_up(subtotal_cents*coupon["value"],
100)
e lse :
am o u n t = c o u p o n [ " v a lu e " ]
returnm in(amount,subtotal_cents)
d e f ta x _ fo r ( ta x a b le _ c e n ts , re g io n ) :
i f r e g io n n o t in T A X _ B P S :
raiseValueError(f"unknown region {region!r}")
return round_half_up(taxable_cents*TAX_BPS[region],
10_000 )
defround_half_up(numerator,denom inator):
return(2*numerator+denom inator)//(2*denom inator)
d e f p r ic e _ o rd e r ( l in e s , re g io n , c o u p o n = N o n e ) :
"""Re tu rn d ic t(sub to ta l_cen ts ,d iscoun t_cen ts , tax_cen ts ,
to ta l_ c e n ts ) ." " "
s u b = s u b t o t a l ( l in e s )
tax= tax_for(sub,region)
d iscoun t= d iscoun t_ fo r(coupon ,sub )
return {
"sub to ta l_cen ts" :sub ,
"d iscount_cents":d iscount,
"tax_cents":tax,
"total_cents":sub-discount+ tax,
}
ChatGPT
Excellent! received.IkkadaReport3kiexactsuspicious logicdorikindi.
pricing.py
P r ic in g a n a ly s is
  price_order()
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
  In
:
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
16/35

sub = subtotal(lines)
tax = tax_for(sub, region)
discount = discount_for(coupon, sub)
Tax n id iscoun tapp ly cheyyakam unde ca lcu la te ches tunna ru .
E x p e c te d c a lc u la t io n :
1 .Sub to ta lca lcu la te cheyya li.
2 .C o u p o n d is c o u n t c a lc u la te c h e y y a l i .
3 .D iscoun tsub trac tches ina am oun tm eeda tax ca lcu la te cheyya li.
4 . F in a l to ta l c a lc u la te c h e y y a l i .
E x am p le :
S u b t o t a l = ₹ 1 ,0 0 0
C o u p o n d is c o u n t = ₹ 10 0
Tax rate= 10%
C u r r e n t lo g ic : ₹ 1 ,0 0 0 m e e d a t a x = ₹ 1 0 0 .
Expected logic:₹900meedatax=₹90.
So,Report3kistrongpotentialrootcause identifyayyindi.
N e x t f i le :
reports.py
t illpoint → reports.py
o p e n c h e s i c om p le te c o d e p a s te c h e y y i .
I d i R e p o r t 4 ( I n d i a t im e z o n e ) a n d R e p o r t 1 ( d a i l y r e v e n u e ) i n v e s t i g a t e c h e y y a d a n i k i im p o r t a n t .
Important:Inkacodeeditcheyyaku.Rootcausesconfirm chesi,testswritechesi,onebugat
a t im e f i x c h e d d a m .
You
"""Sa les repo rts fo r the shop ow ne r."""
from datetime importdatetime,timedelta,timezone
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
17 / 35
        https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
17/35

from .importdb
defday_bounds_utc(day,utc_offset_m inutes=0):
"""TheUTC instantsatwhichashop-localcalendardaystarts
a n d e n d s . d a y is 'Y Y Y Y -M M -D D ' ." " "
s t a r t = d a t e t im e . s t r p t im e ( d a y , "% Y -% m -
% d " ) . r e p l a c e ( t z i n f o = t im e z o n e . u t c )
start+= timedelta(m inutes=utc_offset_m inutes)
returndb.to_iso(start),db.to_iso(start+ timedelta(days=1))
defdaily_sales(conn,day,utc_offset_m inutes=0):
" " "M o n e y re c e iv e d o n o n e s h o p - lo c a l d a y , a n d h ow m a n y
orders itcame from ."""
start,end=day_bounds_utc(day,utc_offset_m inutes)
row = conn .execu te (
"SELECTCOALESCE(SUM (amount_cents),0)AS revenue,
C O U N T ( D I S T IN C T o r d e r _ i d ) A S o r d e r s "
"FROM paymentsWHERE received_at>=?AND
re c e iv e d _ a t < ? " ,
(start,end),
) . fe tc h o n e ( )
re tu rn {"day" :day ,"revenue_cen ts" : row ["revenue"],"o rde rs" :
row ["orders"]}
deftop_products(conn,lim it=5):
"""Bestsellersbyunits,countingorders thatwerepaidor
sh ipped ."""
row s = conn .execu te (
"SELECT i.sku,SUM (i.qty)ASunits,SUM (i.qty*
i.un it_p rice_cen ts)AS g ross_cen ts"
" F R O M o r d e r _ i t e m s i J O IN o r d e r s o O N o . i d = i . o r d e r _ i d "
"WHEREo.status IN ('paid','shipped')GROUPBY i.sku
O R D E R B Y u n i t s D E S C , i . s k u L IM I T ? " ,
(lim it,),
).fe tcha ll()
re tu rn [d ic t ( r ) fo r r in row s ]
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
18 / 35
    https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
18/35

ChatGPT
Good! received.IppuduReport4kiimportantissue identifycheddam .
reports.py
Repo rts ana lys is
  day_bounds_utc()
start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
start += timedelta(minutes=utc_offset_minutes)
Potentialissue:UTC+5:30shop-localdaystartniUTC timekiconvertcheyyalanteoffset
sub trac tcheyya li,add kaadu .
Forexample,India localm idnight(00:00 IST)=previousday18:30UTC.
So,currentlogicreversedirection loundi.Report4kistrongpotentialrootcause.
Mana inspectionstatus
F ile S ta tu s
se rve r.py Rev iew ed
d b .p y R ev iew e d
c a ta lo g .p y R ev iew e d
o rd e rs .p y Rev iew ed
p aym en ts .py R ev iew e d
p r ic in g .p y R ev iew e d
repo r ts .p y R ev iew e d
N e x t f i le :
api.py
t illpoint → api.py
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
19 / 35
    In
:
                o p e n c h e s i c om p le te c o d e p a s te c h e y y i .
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
19/35

T a rv a th a te s ts fo ld e r in s p e c t c h e s i , 6 p ro b lem s k i e x is t in g te s ts a n d re p ro d u c t io n s te p s
checkcheddam .
R em em b e r : Ip p a t iv a r a k u o r ig in a l c o d e e d i t c h e y y a le d u . F i r s t d ia g n o s is c om p le t e c h e s i , t e s t s
thoeach fixverifychestham .
You
"""A tinyJSONAPIovertheorderdesk.handle()isthewhole
surface;server.pyputs itonasocket."""
im p o r t j s o n
im p o r t r e
f r o m . im p o r t p r i c i n g , r e p o r t s
from .catalog importCatalog,OutOfStock,UnknownProduct
f r o m . o r d e r s im p o r t O r d e r E r r o r , O r d e r s
from .paym en ts im p o r t P a ym en tE rro r,Paym en ts
c la s s A p p :
de f__ in it__ (se lf,conn ):
se lf.conn = conn
se lf.ca ta log = C a ta log (conn )
se lf.o rde rs = O rde rs (conn ,se lf.ca ta log )
s e l f .p a ym e n t s = P a ym e n t s ( c o n n )
d e f h a n d le ( s e l f ,m e th o d , p a th , b o d y = N o n e ) :
"""Returns (status,payload)."""
body = body o r {}
try:
ifmethod== "POST"andpath== "/orders":
o rde r= se lf.o rde rs .c rea te (
body["customer"],[(i["sku"],i["qty"])for iin
body["item s"]],
reg ion=body.get("reg ion","NONE"),
c o u p o n _ c o d e = b o d y .g e t ( " c o u p o n " ) )
return201,order
m = re.fullmatch(r"/orders/(\d+)",path)
ifmethod=="GET"andm :
return200,self.orders.get(int(m .group(1)))
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
20 / 35
     https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
20/35

21 / 35
  m = re.fullmatch(r"/orders/(\d+)/cancel",path)
ifmethod=="POST"andm :
return200,self.orders.cancel(int(m .group(1)))
m = re.fullmatch(r"/products/([\w-]+)",path)
ifmethod=="GET"andm :
p=self.catalog.get_product(m .group(1))
re tu rn 2 0 0 , { " s k u " : p .s k u , " n am e " : p .n am e ,
"p r ic e _ c e n ts " : p .p r ic e _ c e n ts , " s to c k " : p .s to c k }
ifmethod=="PUT"andm :
self.catalog.update_price(m .group(1),
b o d y [ " p r ic e _ c e n t s " ] )
return200,{"sku":m .group(1),"price_cents":
b o d y [ " p r ic e _ c e n t s " ] }
ifmethod== "POST"andpath== "/webhooks/payments":
re tu rn 200 , {"s ta tus" :
se lf.paym en ts .hand le_even t(body )}
m = re.fullmatch(r"/reports/daily/(\d{4}-\d{2}-\d{2})",path)
ifmethod=="GET"andm :
return200,reports.daily_sales(self.conn,m .group(1),
int(body.get("utc_offset_m inutes",0)))
re tu rn 4 0 4 , { " e r ro r " : " n o t fo u n d " }
e x c e p t (U n k n ow n P ro d u c t ,O rd e rE r ro r ) a s e :
re tu rn 404 , {"e rro r" :s tr(e )}
e x c e p t (O u tO fS to c k , p r ic in g .C o u p o n R e je c te d , P a ym e n tE r ro r )
as e :
re tu rn 409 , {"e rro r" :s tr(e )}
excep t (KeyE rro r,Va lueE rro r,TypeE rro r)as e :
return400,{"error":f"bad request:{e}"}
d e f d um p s (p a y lo a d ) :
return json.dumps(payload,sort_keys=True)
ChatGPT
E x c e l le n t ! received.Manaapplicationcode inspectionalmostcomplete.✅
api.py
AP Iana lys is
A P I l o a l l im p o r t a n t m o d u l e s c o n n e c t a y y a y i :
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
    https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
21/35

22 / 35
  O rders→
Orders
P roduc ts→
Catalog
P a ym e n t s →
Payments
D a ily repo rts→
reports.daily_sales
Oneobservation:paymentwebhookresponsealwaysHTTP200 istundiwhen
handle_event()
succeeds .Paym en t log ic n i lo fix cheyya li.
payments.py
Nextstep:Existing tests inspectcheddam
VSCode lo left-sideExploreropencheyyi.
1 . fo ld e r e x p a n d c h e y y i .
tests
2 . A n d u lo u n n a f i le n am e s c h o o d u .
3 . S c re e n s h o t p am p u o r f irs t te s t f i le c om p le te c o d e p a s te c h e y y i .
E n d u k u ? E x is t in g t e s t s n i u n d e r s t a n d c h e s i , a s s ig nm e n t lo a d ig in a r e g r e s s io n t e s t s a l r e a d y
unnaya leda an icheck cheddam .
Tarvathamanam :
6bugsreproducechestham .
C o r r e c t f i x e s im p l e m e n t c h e s t h a m .
Each fixkitestrunchestham .
SeparateG itcomm itscreatechestham .
NOTES.md session_logs/
, ,finalZIPpreparechestham .
Ippuducodechangecheyyaku.Firsttests inspectcheddam .
You
artham kalaaexploreopenchesa
ChatGPT
P a r l e d h u . S im p l e g a c h e p t h a n u . 😊
VSCode lo leftsideExploreropenchesavkada?
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
            https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
22/35

Ippuduakkadaprojectfiles listkanipistundi.
23 / 35
  1 . a n e fo ld e r k o s am c h o o d u .
tests
2. pakkanasmallarrow (▶)untundi.
tests
3 . A a a r row m e e d a c l ic k c h e y y i .
4 . L o p a la u n n a f i le n am e s k a n ip is ta y i .
    O k a q u e s t io n : N e e E x p lo r e r lo
You
ChatGPT
tests
Screenshotchusanu.👍 Ippudu issueartham ayyindi.
a n e fo ld e r k a n ip is to n d h a ?
  N e e V S C o d e E x p lo r e r lo
api.py
tillpoint
folderopenundi.AnduloPython fileskanipistunnayi:
    Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
23/35

24 / 35
      catalog.py
    db.py
    orders.py
    payments.py
    pricing.py
    reports.py
Kaani folderkanipinchatledu. , kudaeeview lo levu.
tests
server.py README.md
Ippudu ee s tep cheyy i
        1.VSCode topmenu loFileclickcheyyi.
2 .O p e n F o ld e r c l ic k c h e y y i .
3 . A s s ig nm e n t p ro je c t u n n a o u te r fo ld e r s e le c t c h e y y i—
p a re n t fo ld e r .
4 .O p e n c l ic k c h e y y i .
Correctprojectstructure ilaundali:
project-folder/
├── README.md
├── server.py
├── tillpoint/
│   ├── catalog.py
│   ├── orders.py
│ └── ...
└── tests/
tillpoint
 O p e n c h e s a k a E x p lo r e r s c r e e n s h o t p am p u . A p p u d u n e x t s t e p c h e p t h a n u .
You
open chesa
ChatGPT
S u p e r !👍
p a c k a g e fo ld e r k i
    Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
24/35

IppuduVSCode left-sideExplorerloprojectfolderskanipistunnaya?
tests
a n e fo ld e r u n d a c h o o d u .
Unte,pakkanaunnaarrow (▶)clickcheyyi.
Lopa la unna file nam es naaku cheppu .
tests
folderkanipinchakapothescreenshotpampu.ఒ  stepgaveldham .
You
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t % l s
C A N D ID A T E _ B R IE F .m d R E A D M E .m d s e s s io n _ lo g s
t i l lp o in t
N O T E S .m d s e r v e r . p y t e s t s
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t %
ChatGPT
Perfect!🎉 Correctprojectfolderopenayyindi.Manarequiredfoldersanniunnayi.
tillpoint_assignment/
├── CANDIDATE_BRIEF.md
├── README.md
├── NOTES.md
├── server.py
├── session_logs/
├── tillpoint/
└── tests/
N e x t s in g le s te p :
Term inalloeecommand typecheyyi:
ls tests
En te rp ress ches ivach ina ou tpu t ikkada pas te cheyy i.
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
25 / 35
       https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
25/35

You
d e e p t h i@ D e e p t h i s - M acBoo k-A ir til lpo in t_ass ignm en t% ls tests
__ in it__ .py tes t_o rde rs .py
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t %
ChatGPT
G o o d ! fo ld e r lo c u r re n t ly tw o f i le s u n n a y i :
tests
    __init__.py
    test_orders.py
Ippuduexisting tests inspectcheddam .
Term inalloeecommandruncheyyi:
cat tests/test_orders.py
V a c h in a c om p le te o u tp u t ik k a d a p a s te c h e y y i .
Existing testsem coverchestunnayochusi,m issing regression tests identifycheddam .
You
d e ept h i@ D e e p t h is-M acBoo k-A ir til lpo in t_ass ignm en t% ls
C A N D ID A T E _ B R IE F .m d R E A D M E .m d s e s s io n _ lo g s
t i l lp o in t
NOTES.md server.py tests
d e ept h i@ D e e p t h is-M acBoo k-A ir til lpo in t_ass ignm en t% ls tests
__ in it__ .py tes t_o rde rs .py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% cat
tes ts /tes t_o rde rs .py
im p o r t u n i t t e s t
from datetime importdatetime,timezone
f r o m t i l l p o i n t im p o r t d b , r e p o r t s
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
26 / 35
 Existing tests loem unnayo firstcheckcheddam .
        https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
26/35

27 / 35
 f r o m t i l l p o i n t . a p i im p o r t A p p
from tillpoint.catalog importOutOfStock
c lassO rderDeskTest(un ittest.TestCase):
d e f s e tU p ( s e l f ) :
se lf.conn = db .connec t()
se lf.app = App (se lf.conn )
s e l f . a p p . c a t a l o g . a d d _ p r o d u c t ( "M U G " , "M u g " , 1 2 0 0 ,
stock=10)
se lf.app .ca ta log .add_p roduc t("TEE","T-sh irt",2500 ,
stock=3)
self.conn.execute("INSERT INTOcoupons(code,kind,value)
VALUES ('TEN ','percent',10)")
deftest_order_totals_w ith_tax(self):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 2 ) , ( " T E E " , 1 ) ] ,
reg ion="CA")
se lf.asse rtEqua l(o rde r["sub to ta l_cen ts"],4900 )
se lf.asse rtEqua l(o rde r["tax_cen ts"],355 )
se lf.asse rtEqua l(o rde r["to ta l_cen ts"],5255 )
s e l f . a s s e r t E q u a l ( s e l f . a p p . c a t a l o g . g e t _ p r o d u c t ( "M U G " ) . s t o c k , 8 )
de f tes t_coupon_ takes_ ten_pe rcen t(se lf):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] ,
coupon_code="TEN ")
se lf.asse rtEqua l(o rde r["d iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde r["to ta l_cen ts"],1080 )
d e f te s t_ o u t_ o f_ s to c k ( s e l f ) :
w ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te ("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app .cata log .get_product("TEE").stock,
3)
de f tes t_paym en t_m a rks_o rde r_pa id (se lf):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app .hand le ("PO ST ",
" /w e b h o o k s / p a y m e n t s " , {
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
27/35

" id " : " e v t _ 1 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o r d e r [ " id " ] , " am o u n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l ( ( s t a t u s , p a y lo a d [ " s t a t u s " ] ) , ( 2 0 0 , " p a id " ) )
d e f t e s t _ c a n c e l_ p a id _ o r d e r _ r e s t o c k s ( s e l f ) :
order= se lf.app .orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand le_even t(
{ " id " : " e v t _ 2 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o rd e r [ " id " ] , " am o u n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance l(order["id"])
se lf.assertEqua l(se lf.app .cata log .get_product("TEE").stock,
3)
d e f te s t_ d a i ly _ s a le s ( s e l f ) :
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 2 5 , 3 , 1 0 , 1 2 , 0 , t z i n f o = t im e z o n e . u t c )
se lf.app .paym en ts .hand le_even t(
{ " id " : " e v t _ 3 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o r d e r [ " id " ] , " am o u n t _ c e n t s " : 1 2 0 0 } , n o w = n o o n )
s e lf .a s s e r tE q u a l( re p o r ts .d a i ly_ s a le s (s e lf .c o n n , "2 0 2 5 -0 3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 ,
"orders":1})
d e f t e s t _ p r ic e _ c h a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( " P U T " , " / p r o d u c t s /M U G " , { " p r i c e _ c e n t s " :
1500})
s e l f . a s s e r t E q u a l ( s e l f . a p p . c a t a l o g . g e t _ p r o d u c t ( "M U G " ) . p r i c e _ c e n t
s,1500)
i f _ _ n am e _ _ = = " _ _m a in _ _ " :
u n i t t e s t .m a i n ( )
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t %
ChatGPT
S u p e r ! E x is t in g
test_orders.py
c om p le te c o d e v a c h in d i .👍
28 / 35
     Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
28/35

Existing tests loem coverchestunnaru?
Currently7 testsunnayi:
1 .O rd e r to ta l a n d ta x
2.10% coupondiscount
3 . O u t - o f - s t o c k v a l id a t io n
4 . P a ym e n tm a rk s o rd e r a s p a id
5.Paidordercancellationand restocking
6 .D a ily sa les repo rt
7 . P ro d u c t p r ic e u p d a te
Important:Assignmentlounna6 reportedproblemskidedicated regression testsee file lo
levu.Manam addcheyyali.
N e x t s t e p : B a s e l in e t e s t s r u n c h e d d am
Mundhuexistingapplication testspassavuthunnaya ledacheckcheyyali.
Term inalloeecommandcopy-pastecheyyi:
python3 -m unittest discover -s tests -v
En te rp ress cheyy i.
V a c h in a c om p le te o u tp u t p a s te c h e y y i .
Ippuducodeeditcheyyoddu.Firstoriginalprojectcondition recordcheddam .
You
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t % l s
C A N D ID A T E _ B R IE F .m d R E A D M E .m d s e s s io n _ lo g s
t i l lp o in t
NOTES.md server.py tests
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t % l s t e s t s
__ in it__ .py tes t_o rde rs .py
deepthi@Deepthis-MacBook-Airtillpoint_assignment% cat
tes ts /tes t_o rde rs .py
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
29 / 35
     https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
29/35

im p o r t u n i t t e s t
from datetime importdatetime,timezone
from t i l lpo in t im p o r t d b , re ports
from t i l lpo i n t . a p i im p o rtApp
from tillpoint.catalog importOutOfStock
c lassO rderDeskTest(un ittest.TestCase):
d e f s e tU p ( s e l f ) :
se lf.conn = db .connec t()
se lf.app = App (se lf.conn )
s e l f . a p p . c a t a l o g . a d d _ p r o d u c t ( "M U G " , "M u g " , 1 2 0 0 ,
stock=10)
se lf.app .ca ta log .add_p roduc t("TEE","T-sh irt",2500 ,
stock=3)
self.conn.execute("INSERT INTOcoupons(code,kind,value)
VALUES ('TEN ','percent',10)")
deftest_order_totals_w ith_tax(self):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 2 ) , ( " T E E " , 1 ) ] ,
reg ion="CA")
se lf.asse rtEqua l(o rde r["sub to ta l_cen ts"],4900 )
se lf.asse rtEqua l(o rde r["tax_cen ts"],355 )
se lf.asse rtEqua l(o rde r["to ta l_cen ts"],5255 )
s e l f . a s s e r t E q u a l ( s e l f . a p p . c a t a l o g . g e t _ p r o d u c t ( "M U G " ) . s t o c k , 8 )
de f tes t_coupon_ takes_ ten_pe rcen t(se lf):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] ,
coupon_code="TEN ")
se lf.asse rtEqua l(o rde r["d iscoun t_cen ts"],120 )
se lf.asse rtEqua l(o rde r["to ta l_cen ts"],1080 )
d e f te s t_ o u t_ o f_ s to c k ( s e l f ) :
w ithself.assertRaises(OutOfStock):
se lf.app .o rde rs .c rea te ("ana", [("TEE",4 )])
se lf.assertEqua l(se lf.app .cata log .get_product("TEE").stock,
3)
30 / 35
    Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
30/35

31 / 35
 de f tes t_paym en t_m a rks_o rde r_pa id (se lf):
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] )
s ta tus ,pay load = se lf.app .hand le ("PO ST ",
" /w e b h o o k s / p a y m e n t s " , {
" id " : " e v t _ 1 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o r d e r [ " id " ] , " am o u n t _ c e n t s " : 1 2 0 0 } )
s e l f . a s s e r t E q u a l ( ( s t a t u s , p a y lo a d [ " s t a t u s " ] ) , ( 2 0 0 , " p a id " ) )
d e f t e s t _ c a n c e l_ p a id _ o r d e r _ r e s t o c k s ( s e l f ) :
order= se lf.app .orders.create("ana",[("TEE",2)])
se lf.app .paym en ts .hand le_even t(
{ " id " : " e v t _ 2 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o rd e r [ " id " ] , " am o u n t_ c e n ts " : 5 0 0 0 } )
se lf.app .orders.cance l(order["id"])
se lf.assertEqua l(se lf.app .cata log .get_product("TEE").stock,
3)
d e f te s t_ d a i ly _ s a le s ( s e l f ) :
o r d e r = s e l f . a p p . o r d e r s . c r e a t e ( " a n a " , [ ( "M U G " , 1 ) ] )
n o o n = d a t e t im e ( 2 0 2 5 , 3 , 1 0 , 1 2 , 0 , t z i n f o = t im e z o n e . u t c )
se lf.app .paym en ts .hand le_even t(
{ " id " : " e v t _ 3 " , " t y p e " : " p a ym e n t . s u c c e e d e d " , " o r d e r _ id " :
o r d e r [ " id " ] , " am o u n t _ c e n t s " : 1 2 0 0 } , n o w = n o o n )
s e lf .a s s e r tE q u a l( re p o r ts .d a i ly_ s a le s (s e lf .c o n n , "2 0 2 5 -0 3 -
10"),
{"day":"2025-03-10","revenue_cents":1200 ,
"orders":1})
d e f t e s t _ p r ic e _ c h a n g e ( s e l f ) :
s e l f . a p p . h a n d l e ( " P U T " , " / p r o d u c t s /M U G " , { " p r i c e _ c e n t s " :
1500})
s e l f . a s s e r t E q u a l ( s e l f . a p p . c a t a l o g . g e t _ p r o d u c t ( "M U G " ) . p r i c e _ c e n t
s,1500)
i f _ _ n am e _ _ = = " _ _m a in _ _ " :
u n i t t e s t .m a i n ( )
deepthi@Deepthis-MacBook-Airtillpoint_assignment% python3
-m un ittestd iscover-s tests -v
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
31/35

32 / 35
  te s t_ c a n c e l_ p a id _ o rd e r_ re s to c k s
( t e s t _ o r d e r s .O r d e r D e s k T e s t . t e s t _ c a n c e l _ p a i d _ o r d e r _ r e s t o c k s ) . . .
ok
tes t_coupon_ takes_ ten_pe rcen t
(tes t_o rde rs .O rde rD eskTes t.tes t_coupon_ takes_ ten_pe rcen t)
...ok
t e s t _ d a i l y _ s a l e s ( t e s t _ o r d e r s .O r d e r D e s k T e s t . t e s t _ d a i l y _ s a l e s ) . . .
ok
test_order_totals_w ith_tax
(test_orders.OrderDeskTest.test_order_totals_w ith_tax)...ok
te s t_ o u t_ o f_ s to c k
(tes t_o rde rs .O rde rD eskTes t.tes t_ou t_o f_s tock ) ...ok
tes t_paym en t_m a rks_o rde r_pa id
( t e s t _ o r d e r s .O r d e r D e s k T e s t . t e s t _ p a y m e n t _ m a r k s _ o r d e r _ p a i d )
...ok
te s t_ p r ic e _ c h a n g e
(test_orders.O rderDeskTest.test_price_change) ...ok
-----------------------------------------------------------------
-----
Ran7 tests in0.006s
OK
d e e p t h i@ D e e p t h i s - M a c B o o k - A i r t i l l p o i n t _ a s s i g n m e n t %
ChatGPT
Excellent!🎉 Baselinetestsannipassayyayi.
7 /7 T e s ts P a s s e d
I d i e n d u k u im p o r t a n t ?
Originalprojectloexisting testspassavuthunnayi.Kaaniassignmentlo reportchesina6
bugsniee testsproperlycheckcheyyatledu.
Mananextgoal:Bugnireproducechesetestfirstwritecheyyali.Aatestoriginalcode lo
fa ilavva li.F ix chesaka pass avva li.
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
    https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
32/35

33 / 35
 Ip p u d u f i r s t b u g : C o u p o n + T a x
 pricing.py
lo taxdiscountapplycheyyakamundecalculateavuthondianiidentifychesam .
E x am p le :
S u b t o t a l : ₹ 1 ,0 0 0
Coupon :10%
T a x : 10%
Expected tax=₹90,not₹100.
N e x t s in g le s te p
Term inalloeecommand runcheyyi:
cat CANDIDATE_BRIEF.md
C om p le te o u tp u t p a s te c h e y y i .
Assignmentloexactrequirementschusi,firstbugkiregression testpreparecheddam .
Ip p u d u e x is t in g c o d e n i e d i t c h e y y a k u .
You
ChatGPT
Pasted text(2026...
D o c um e n t
  K e e r th i , c o n te n t v a c h in d i .A s s ig nm e n t re q u irem e n ts c le a r g a u n n a y i .
CANDIDATE_BRIEF.md
Oka importantpoint:Assessmentloneeownunderstanding,questions,decisions,
verificationki70marks.Andukenenucodematrame ivvakunda,prathibugendukuvachindo
n e e k u e x p la in c h e s th u p ro c e e d a v u th a n u .
M a n a im m e d i a t e p r i o r i t i e s
1.Bug reproducecheyyali.
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
   https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
33/35

34 / 35
 2 .O r ig in a l c o d e lo te s t fa i l a v v a d am c h o o d a l i .
3 . R o o t c a u s e f ix c h e y y a l i .
4.Testpassavvadam verifycheyyali.
5.SeparateG itcomm itcreatecheyyali.
Firstbugnistartcheddam :Coupon+Tax
pricing.py
lo a l r e a d y s u s p ic io u s lo g ic id e n t i f y c h e s am . K a a n i f i r s t r e g r e s s io n t e s t w r i t e
ches ip rove cheyya li.
Ip p u d u o k a q u e s t io n :
FirstReport3 (Coupon+Tax)fixcheddama? Idirelativelysimple,testthoeasyga
unde rs tand chesukovachu .
Yes
You
okay
ChatGPT
Okay.FirstReport3–Coupon+Taxstartcheddam .Existingcodeniippudechange
cheyyaku .
S te p 1 : T e s t f i le o p e n c h e y y i
VSCode lo
tests/test_orders.py
open cheyy i.
Fileending lo, methodkimundhueetestaddcheyyi:
test_price_change()
    def test_coupon_reduces_taxable_amount(self):
        order = self.app.orders.create(
            "ana",
            [("MUG", 1)],
            region="CA",
            coupon_code="TEN"
)
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
 anicheppu.Appudu firsttestnistep-by-stepcreatecheddam .
      https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
34/35

        self.assertEqual(order["subtotal_cents"], 1200)
        self.assertEqual(order["discount_cents"], 120)
        self.assertEqual(order["tax_cents"], 78)
        self.assertEqual(order["total_cents"], 1158)
Whyexpected tax=78?
P ro d u c t p r ic e = 12 0 0 c e n ts
C o u p o n d is c o u n t = 1 2 0 c e n t s
Taxab le am oun t= 1080 cen ts
CA tax=7.25%
Tax = 78 cen ts (rounded )
S te p 2 : T e s t ru n c h e y y i
Term inallo:
python3 -m unittest
tests.test_orders.OrderDeskTest.test_coupon_reduces_taxable_amount -v
Expected resu lt:FA IL
Originalcode taxnidiscountapplycheyyakamundhucalculatechesthundikabattitestfail
avva li.
Testoutputpastecheyyi.Appudunextstep lo fixchestham .
Ifyouw an t, Ican :
Add regression testtoverifycoupondiscountaffectstaxableamountcorrectly
R u n th e n ew c o u p o n + ta x re g re s s io n te s t a n d s h a re th e fa i lu re o u tp u t
G u id e m e to f ix ta x c a lc u la t io n to a p p ly c o u p o n d is c o u n t b e fo re ta x
Takeyourcuriosity further
S c a n to g e t th e C h a tG P T a p p
35 / 35
      https://chatgpt.com/share/6b02785b-fe84-83ee-880c-ca95fca8bd04
35/35
