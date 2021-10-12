import math

print_ri_file="TSO6211_03.12.14_XY"
f = open(print_ri_file,'r')

locator_name = "KomsomoRaduga"
plane_id = "ID= 5007"
#turn_angle=90
#iterations_number=5
turn_angle=5
iterations_number=5

x = 1
y = 1
x_2 = 1
y_2 = 1
angle = 1
angle_2 = 1
d_d_angle = 0
t = 0

for line in f:
    if line.__contains__(locator_name) and line.__contains__(plane_id):
        time = line[1:19]
        x = int(line[58:65])
        y = int(line[68:75])

        d_x = x_2 - x
        d_y = y_2 - y

        x_2 = x
        y_2 = y

        angle = int(math.degrees(math.atan(d_x / d_y)))
        d_angle = angle_2 - angle
        angle_2 = angle

        d_d_angle = d_d_angle + d_angle
        t = t + 1

        if abs(d_d_angle) >= turn_angle and t <= iterations_number:
            print ("There is a turn!!!")
            d_d_angle = 0
            t = 0

        h = int(line[78:83])

        print(line.strip())
        print("x="+str(x))
        print("y="+str(y))
        print("d_x=" + str(d_x))
        print("d_y=" + str(d_y))
        print("angle=" + str(angle))
        print("d_angle=" + str(d_angle))
        print("d_d_angle=" + str(abs(d_d_angle)))
        print("time=" + str(time))
        print("h="+str(h))


