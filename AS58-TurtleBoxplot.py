import turtle

def box(median,uq,lq,maxx,minn):
  
  t=turtle.Turtle()
  t.speed(0)
  t.lt(90)
  t.forward(100)
  t.back(50)
  t.rt(90)
  t.forward(lq-minn)
  t.lt(90)
  t.fd(50)
  t.lt(180)
  t.fd(100)
  t.lt(90)
  t.fd(uq-lq)
  t.lt(180)
  t.fd(uq-median)
  t.rt(90)
  t.fd(100)
  t.lt(90)
  t.fd(median-lq)
  t.rt(180)
  t.fd(uq-lq)
  t.rt(90)
  t.fd(100)
  t.lt(180)
  t.fd(50)
  t.rt(90)
  t.fd(maxx-uq)
  t.lt(90)
  t.fd(50)
  t.lt(180)
  t.fd(100)

box(100,190,50,250,2)
