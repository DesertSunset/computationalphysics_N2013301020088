def z(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.0001
    sigma=10
    b=8/3
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
    return t,z,x,y


    
figure(figsize=(8,6))
plot(z(5)[0],z(5)[1],label="r=5",color="blue",linewidth=2,linestyle='-')
plot(z(10)[0],z(10)[1],label="r=10",color="red",linewidth=2,linestyle='-')
plot(z(25)[0],z(25)[1],label="r=25",color="green",linewidth=2,linestyle='-')
xlabel("t")
title("Lorenz model: z versus t")
ylabel("z")
grid(True)
legend(loc='best')
show()