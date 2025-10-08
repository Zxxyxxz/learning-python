import math
ad="name"
yas=12
yaski=13
virgullu_rakim=120007.9847838827428
yuz_d_yuz=1
yuz_d_eli=0.5
yuz_d_1=0.01

insan_dictionarisi = {"name": ad, "age":00,"loc":"mzitli"}
class Insan:
    def __init__(self,name, age):
        self.name = name
        self.age = age

insan_1 = Insan("ahmet", 22)

def kufur(isim):
    return f" {isim} seni kotu pis cani ...."


def f_str_1_tut():
   
    print(f"my name is {ad} and im {yas} rys old")
    try:
        print(f"lets try to add the string to an integer with f stirng {ad}+{yas}={ad+yas}")
    except TypeError:
        print(f"can do the addition in other words the concatenation with string to str but maybe we can by this {ad}+{str(yas)}={ad + str(yas)} {ad}+{str(yas)}={ad + str(yas)}")
        print(f"same addition with numbers is it conversion based? {yas}+{yaski}= {yas+yaski}")
        print(f"{yas+yaski=}")
        print(f"{yas+yaski}")
        print(f"simdi kufur etme fokn isyonu {ad} sahsina kufur edecek: {kufur(ad)}")
        print(f"within the curly brackets the oeprators also start working {(yas**yaski/yas)<yas*yaski=} ")
        print(f"\n we can also get it all uppercase with the func .upper and it beomes all caps from {ad} to {ad.upper()}")
        print(f"""now lets try some arrangemtent and num format {{ad:^10}} buna denk gelitor:
              \n {ad:^10}
              \n sonra bunun 10 katini {{ad:^100}} deneylim:
              \n{ad:^100}
              \n simdi buyuk kucuk {{ad:>100}} ve {{ad:<100}} deniyoruz
              \n {ad:>100}
              \n{ad:<100} \n go down 30 new lines :{")"*35}
              {"\n"*30} {"__________"*2} ok now number formatting{"__________"*2}
              \n lets format some deciamls mesela :.dan sonra istedeign decimal hanesini eklersen o kadar gorunu mesela {{virgullu_rakim:.2f}} bu bu sonucu veriyor
              \n {virgullu_rakim:.2f}
              \n or we can also make the big number more formated {{virgullu_rakim:,}} which look like this now
              \n {virgullu_rakim:,}
              \n and even maybe we can comine both o these {{virgullu_rakim:,.3f}} which ends up to be 
              \n {virgullu_rakim:,.3f}
              \n and even formatting some percentages{{yas:.1%}} being this:
              \n {yas:.1%}
              \n and more example is {{yuz_d_eli}} = {yuz_d_eli}, {{yuz_d_1}} = {yuz_d_1} , {{yuz_d_yuz}}= {yuz_d_yuz}
              \n bunlari percentage ya[mak icin {{yuz_d_1:.2%}} ve bu iluyor :{yuz_d_1:.2%}
              
              {"___asagi inin__"*8} {"\n"*10}
              simdi dictionary ile formatlama
              \n insan kalsindan {insan_1.name} {insan_1.age} yasinda bulunur
              """)
        
        


if __name__== "__main__":
    f_str_1_tut()
