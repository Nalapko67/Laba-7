import math

class Figure:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    def get_type(self):
        return "Figure"

    def volume(self):
        return 0.0

    def display(self):
        print(f"Type: {self.get_type()}, Position: ({self._x}, {self._y}, {self._z})")

    def edit(self):
        self._x = float(input("Enter new X: "))
        self._y = float(input("Enter new Y: "))
        self._z = float(input("Enter new Z: "))


class Cone(Figure):
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=0.0, height=0.0):
        super().__init__(x, y, z)
        self._radius = radius
        self._height = height

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_type(self):
        return "Cone"

    def volume(self):
        return (1.0 / 3.0) * math.pi * (self._radius ** 2) * self._height

    def display(self):
        print(f"Type: Cone, Position: ({self._x}, {self._y}, {self._z}), Radius: {self._radius}, Height: {self._height}, Volume: {self.volume():.2f}")

    def edit(self):
        super().edit()
        self._radius = float(input("Enter new Radius: "))
        self._height = float(input("Enter new Height: "))


class Cylinder(Figure):
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=0.0, height=0.0):
        super().__init__(x, y, z)
        self._radius = radius
        self._height = height

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_type(self):
        return "Cylinder"

    def volume(self):
        return math.pi * (self._radius ** 2) * self._height

    def display(self):
        print(f"Type: Cylinder, Position: ({self._x}, {self._y}, {self._z}), Radius: {self._radius}, Height: {self._height}, Volume: {self.volume():.2f}")

    def edit(self):
        super().edit()
        self._radius = float(input("Enter new Radius: "))
        self._height = float(input("Enter new Height: "))


class Sphere(Figure):
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=0.0):
        super().__init__(x, y, z)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_type(self):
        return "Sphere"

    def volume(self):
        return (4.0 / 3.0) * math.pi * (self._radius ** 3)

    def display(self):
        print(f"Type: Sphere, Position: ({self._x}, {self._y}, {self._z}), Radius: {self._radius}, Volume: {self.volume():.2f}")

    def edit(self):
        super().edit()
        self._radius = float(input("Enter new Radius: "))


class CulinaryContainerManager:
    def __init__(self):
        self._records = []

    def add_record(self, figure):
        self._records.append(figure)

    def display_all(self):
        if not self._records:
            print("No records found.")
            return
        for idx, item in enumerate(self._records):
            print(f"[{idx}] ", end="")
            item.display()

    def search_by_type(self, target_type):
        found = False
        for item in self._records:
            if item.get_type().lower() == target_type.lower():
                item.display()
                found = True
        if not found:
            print(f"No records found for type: {target_type}")

    def search_by_min_volume(self, min_vol):
        found = False
        for item in self._records:
            if item.volume() >= min_vol:
                item.display()
                found = True
        if not found:
            print(f"No records found with volume >= {min_vol}")

    def edit_record(self, index):
        if 0 <= index < len(self._records):
            print(f"Editing record [{index}]:")
            self._records[index].edit()
            print("Record updated successfully.")
        else:
            print("Invalid index.")


def main():
    manager = CulinaryContainerManager()

    c1 = Cylinder(0, 0, 0, 10, 20)
    s1 = Sphere(1, 1, 0, 5)
    cn1 = Cone(2, 2, 0, 8, 15)

    manager.add_record(c1)
    manager.add_record(s1)
    manager.add_record(cn1)

    print("--- All Culinary Containers ---")
    manager.display_all()

    print("\n--- Search by Type (Cylinder) ---")
    manager.search_by_type("Cylinder")

    print("\n--- Search by Min Volume (1000) ---")
    manager.search_by_min_volume(1000)

    print("\n--- Editing Record [0] ---")
    manager.edit_record(0)

    print("\n--- All Records After Edit ---")
    manager.display_all()


if __name__ == "__main__":
    main()