import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000_0)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6),dpi=120)
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolors='none',s=1)
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('Do you want to make another walk?(y/n)')
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        continue
    else:
        print('?')
        break