from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    html = """
    <h1>First page</h1>
    <h2>Asosiy bo'lim</h2>
    <a href = "second/">second page >> </a><br>
    <a href = "pages/kompyuterlar">kompyuterlar page >> </a><br>
    <a href = "pages/telefonlar">telefonlar page >> </a>
    """
    return HttpResponse(html)

def second(request):
    html = """
    <h1>Second page</h1>
    <h2>Ikkionch bo'lim</h2>
    <a href = "../">  first page  </a>
    """
    return HttpResponse(html)


def pages(request,page):
    if page =="kompyuterlar":
        html = f"""
               <h1>{page}</h1>
        
        <p>Kompyuter (inglizcha: computer — „hisoblayman“) — oldindan berilgan qotoq boʻyicha ishlaydigan avtomatik qurilma. Elektron hisoblash mashinasi (EHM) bilan bir xildagi atama. Biroq, kompyuter hisoblash ishlarini bajarishdan tashqari uning funksiyasi ancha keng. EHMlarning rivojlanishida kompyuter ning bir necha avlodlarini koʻrsatish mumkin. Bu avlodlar element turlari, konstruktiv-texnologik xususiyatlari, mantiqiy tuzilishi, dastur taʼminoti, texnik tafsilotlari, texnikadan foydalanishning qulaylik darajasi bilan bir-biridan farq qiladi. Kompyuterning dastlabki avlodida (Ural-1, Minsk-2, BSEM-2) asosiy element elektron lampa boʻlgani uchun u juda katta joyni egallagan edi. Soʻngra bu lampa oʻrnida tranzistorlar ishlatilgan kompyuter (Razdan-2, M-220, Minsk-22 va boshqalar), integral mikrosxemalar ishlatilgan kompyuter (IBM-360, 1BM-370, (AQSh), YESEVM (Rossiya) va boshqalar, integratsiya darajasi katta boʻlgan integral sxemalar oʻrnatilgan shaxsiy kompyuterlar paydo boʻldi. Shaxsiy kompyuter (mikro va mikro EHM) tushunchasi XX asr 70-yillar oxiridan boshlab keng tarqala boshladi. Shaxsiy kompyuterning keyingi avlodlarida mikroelektron va biosxemalardan foydalanildi; ularning hajmi kitob kattaligidek hajmga kichraydi, massasi esa 3,5 kg gacha kamaydi. 1981-yil IBM shirkati shaxsiy kompyuterning yanada takomillashgan modellarini ishlab chiqara boshladi. Keyinchalik boshqa firmalar IBM bilan PC biriktirilgan kompyuterni, Apple shirkati esa Macintosh (talaffuzi: „Makintosh“) yoki oddiygina „maki“ deb ataladigan kompyuterni yaratishdi. XXI asr boshlarida dunyoda oʻnlab million shaxsiy kompyuterlar, 1 millionga yaqin EHM (shu jumladan, bir necha oʻn superEVM) boʻlgan. Kompyuterlar masalalarni yechishda foydalaniladigan komponentlar (tarkibiy qismlar) tarkibi va tavsifi jihatdan bir-biridan farq qiladi. Murakkab masalalarni yechishda kuchli qurilmalar oʻrnatilgan kompyuterdan, hujjatlarni bosishda harf bosish qurilmasi boʻlgan kompyuterdan foydalaniladi. Istalgan kompyuter tizimlar bloki, monitor va klaviaturadan iborat boʻladi.</p>
        <a href = "../">  main page  </a>
        """
    elif page == "telefonlar":
        html = f"""
                <h1>{page}</h1>

                <p>Telefon — tovush uzatish va qabul qilish uchun moʻljallangan telekommunikatsiyalar qurilmasidir. Odatda, tovushning mexanik energiyasini elektrik signallar energiyasiga aylantirish, masofadan uzatish va uni qaytadan tovushga aylantirish prinsipi bilan ishlaydi.

Telefon (tele... olis va fon un = olisun) — 1) elektr signallarini tovush signallariga aylantirib beradigan elektrakustik asbob. Elektromagnitli, elektrodinamik va pyezoelektr turlariga bo'linadi. Elektromagnitli T. eng keng tarqalgan. Uning asosiy elementlari doimiy magnit, chulgʻamli qutblar va membranadan iborat. Abonent "telefon qilganida" T. signalining oʻzgaruvchan elektr toki taʼsirida membrana tebranib, tovush hosil qiladi. T. telefon apparati, turli radiotexnika asboblari va boshqa qurilmalarda ishlatiladi; 2) telefon apparatining qisqa nomi; 3) telefon aloqasining qisqa nomi.</p>
                <a href = "../">  main page  </a>
                """

    else:
        html = f"""
        <h1>{page}</h1>
"""
    return HttpResponse(html)
