class indux:
  def my_method(self):
    print("memanggil method indux")

class anak (indux):
  def child_method(self):
    print("memanggil method anak")

c = anak()
c.my_method()