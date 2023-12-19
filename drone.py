class Drone:
    def __init__(self, start_gps, name):
        self.gps = start_gps
        self.name = name
        self.speed = 40
        self.angular_speed = 5  # Угловая скорость
        self.capasity = 100
        self.pitch, self.roll, self.yaw = 0, 0, 0  # тангаж, крен, курс
        self.stop_altitude, self.stop_time, self.stop_dist = 500, 25, 5

    def move(self, kp, coord_dest, dt):
        distance = self.gps.distance_to(coord_dest)
        if distance < 1:
            print("Мы на месте")
        else:
            u_x, u_y = self.calc(kp, coord_dest)
            self.gps.x += u_x * self.speed * dt
            self.gps.y += u_y * self.speed * dt

    def calc(self, kp, coord_dest):
        u_x = kp * (coord_dest.x - self.gps.x)
        u_y = kp * (coord_dest.y - self.gps.y)
        return u_x, u_y
