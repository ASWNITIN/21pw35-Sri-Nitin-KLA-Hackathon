import math

def wafer_to_cartesian(r, theta):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    wafer_diameter = float(lines[0].split(':')[1].strip())
    die_size_x, die_size_y = map(float, lines[1].split(':')[1].strip().split('x'))
    die_shift_x, die_shift_y = map(int, lines[2].split(':')[1].strip()[1:-1].split(','))  # Extract dieshift vector
    ref_die_center_x, ref_die_center_y = map(float, lines[3].split(':')[1].strip()[1:-1].split(','))

    # Assume the coordinates of the center of the wafer using die shift vector and reference die measurement
    wafer_center_x = ref_die_center_x - 0
    wafer_center_y = ref_die_center_y - 0
    return wafer_diameter, die_size_x, die_size_y, die_shift_x, die_shift_y, wafer_center_x, wafer_center_y

def is_partially_inside_wafer(llc_x, llc_y, die_size_x, die_size_y, wafer_diameter):
    # Check if any corner of the die is within the wafer circumference
    corners = [
        (llc_x - die_size_x / 2, llc_y - die_size_y / 2),  # Lower left corner
        (llc_x + die_size_x / 2, llc_y - die_size_y / 2),  # Lower right corner
        (llc_x - die_size_x / 2, llc_y + die_size_y / 2),  # Upper left corner
        (llc_x + die_size_x / 2, llc_y + die_size_y / 2)   # Upper right corner
    ]

    for corner_x, corner_y in corners:
        if math.sqrt(corner_x**2 + corner_y**2) <= wafer_diameter / 2:
            return True

    return False

def generate_output(wafer_diameter, die_size_x, die_size_y, die_shift_x, die_shift_y, wafer_center_x, wafer_center_y):
    output_lines = []

    # Calculate lower left corner coordinate and die index for each die within the wafer circumference
    for i in range(int(-wafer_diameter / (2 * die_size_x)), int(wafer_diameter / (2 * die_size_x)) + 2):
        for j in range(int(-wafer_diameter / (2 * die_size_y)), int(wafer_diameter / (2 * die_size_y)) + 2):
            llc_x = i * die_size_x + wafer_center_x
            llc_y = j * die_size_y + wafer_center_y

            # Check if any part of the die is within the wafer circumference
            if is_partially_inside_wafer(llc_x, llc_y, die_size_x, die_size_y, wafer_diameter):
                lower_left_x = llc_x - die_size_x / 2  # Calculate lower left x coordinate
                lower_left_y = llc_y - die_size_y / 2  # Calculate lower left y coordinate

                die_index = f'({i},{j})'
                output_lines.append(f'{die_index}:{lower_left_x:.4f},{lower_left_y:.4f}')

    return output_lines

def write_output(output_lines, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(output_lines))

if __name__ == '__main__':
    input_file_path = 'Milestone2/Input/Testcase4.txt'
    output_file_path = 'Milestone2/Output/tc4output.txt'  # Specify the desired output file path

    # Parse input parameters
    wafer_diameter, die_size_x, die_size_y, die_shift_x, die_shift_y, wafer_center_x, wafer_center_y = parse_input(input_file_path)

    output_lines = generate_output(wafer_diameter, die_size_x, die_size_y, die_shift_x, die_shift_y, wafer_center_x, wafer_center_y)

    # Write output to file
    write_output(output_lines, output_file_path)
