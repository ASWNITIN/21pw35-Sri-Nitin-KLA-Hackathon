import math

def generate_bare_wafer_map(diameter, num_points, angle_deg):
    points = []
    angle_rad = math.radians(angle_deg)
    x = diameter / 2 * math.cos(angle_rad)
    y = diameter / 2 * math.sin(angle_rad)

    step_sizex = (2*x) / (num_points - 1)
    step_sizey = (2*y) / (num_points - 1)

    for i in range(num_points):
        current_pointx = -x + i * step_sizex
        current_pointy = -y + i * step_sizey
        points.append((current_pointx,current_pointy))

    return points

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    diameter = float(lines[0].split(":")[1].strip())
    num_points = int(lines[1].split(":")[1].strip())
    angle = float(lines[2].split(":")[1].strip())
    return diameter, num_points, angle

# Example usage:
file_path = 'Milestone1/Input/Testcase4.txt'
wafer_diameter, num_points, angle = read_input_from_file(file_path)
result = generate_bare_wafer_map(wafer_diameter, num_points, angle)

output_file_path = 'Milestone1/Output/tc4output.txt'
with open(output_file_path, 'w') as file:
    for point in result:
        x = int(point[0]) if point[0].is_integer() else round(point[0], 4)
        y = int(point[1]) if point[1].is_integer() else round(point[1], 4)
        file.write(f"({x}, {y})\n")

print("Output written to:", output_file_path)
