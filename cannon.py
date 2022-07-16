Web VPython 3.2
a1 = arrow(axis = vec(10,0,0))
a2 = arrow(axis = vec(0,10,0))
a3 = arrow()
a3.axis = a1.axis + a2.axis
ball = sphere(make_trail = True)
p = label()
s = False
while True :
    p.text = ball.pos
    p.pos = ball.pos + vec(3,3,0)
    rate(100)
    k = keysdown()
    if 'right' in k :
        a3.axis.x += 0.1
    if 'left' in k :
        a3.axis.x -= 0.1
    if 'up' in k :
        a3.axis.y += 0.1
    if 'down' in k :
        a3.axis.y -= 0.1
        
    if ' ' in k :
        s = True
    if s == True :    
        ball.color -= vec(0,0.01,0)
        ball.radius += 0.01
        ball.v = a3.axis
        ball.pos = ball.pos + ball.v * 0.01
        if ball.pos.y <= 0 :
            label(text = '한글이좋아요')
            break
        else :
            ball.v.y = ball.v.y + -9.8 * 0.01
            
        
        
        
        
        
        
