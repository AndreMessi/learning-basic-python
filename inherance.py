class indux:
  parret_attr = 100

  def __init__(self):
    print("memanggil konstruktor indux")
  
  def parrent_method(self):
    print("memanggil metode indux")

  def set_attr(self,attr):
    indux.parret_attr = attr

  def get_attr(self):
    print("atribut inducx",indux.parret_attr)

#mendefinisikan class anak
class anak(indux):
  def __init__(self):
    print("memanggil konstruktor anak")

  def child_method(self):
    print("memanggil method anak")
    
c = anak()
c.child_method()
c.parrent_method()
c.set_attr(200)
c.get_attr()