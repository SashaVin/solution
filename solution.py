class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_le_ext(self):
        if self.photo_le_name.count(".") == 1:
            return '.' + self.photo_le_name.split('.')[-1]
        else:
            return ''


class Car(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, carrying):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    def __repr__(self):
        return '{} {} {} {} {}'.format(str(self.car_type), str(self.brand), str(self.passenger_seats_count), str(self.photo_le_name), str(self.carrying))


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, body_length=0.0, body_width=0.0, body_height=0.0):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    def __repr__(self):
        if self.body_length == 0.0:
            return '{} {} {} {}'.format(str(self.car_type), str(self.brand), str(self.photo_le_name), str(self.carrying))
        else:
            return '{} {} {} {} {}'.format(str(self.car_type), str(self.brand), str(self.photo_le_name), str(self.carrying), str(self.body_length)+"x"+str(self.body_width)+"x"+str(self.body_height))


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra

    def __repr__(self):
        return '{} {} {} {} {}'.format(str(self.car_type), str(self.brand), str(self.photo_le_name), str(self.carrying), str(self.extra))


def get_car_list(filename):
    car_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        txt = f.readlines()
        for i in txt:
            if i.count(';') == 6:
                i = i.split(';')

                if i[0] == 'car':
                    a = Car(i[0], i[1], i[2], i[3], i[5])
                    car_list.append(a)

                if i[0] == 'truck':
                    if i[4] != '':
                        b = i[4].split('x')
                        a = Truck(i[0], i[1], i[3], i[5], float(b[0]), float(b[1]), float(b[2]))
                        car_list.append(a)
                    else:
                        a = Truck(i[0], i[1], i[3], i[5])
                        car_list.append(a)

                if i[0] == 'spec_machine':
                    a = Specmachine(i[0], i[1], i[3], i[5], i[6][:-2])
                    car_list.append(a)
    return car_list


def main():
    return get_car_list('solution.txt')


if __name__ == '__main__':
    print(main())
