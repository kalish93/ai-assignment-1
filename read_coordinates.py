def read_coordinates(file_path):
    coordinates = {}
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(' ')
            parts = [part for part in parts if part != '']
            print(parts)

            if len(parts)  == 4:
                city = parts[0] + " " + parts[1]
                latitude = float(parts[2])
                longitude = float(parts[3])
                coordinates[city] = (latitude, longitude)
            if len(parts) == 3:
                city = parts[0].strip() 
                latitude = float(parts[1])
                longitude = float(parts[2])
                coordinates[city] = (latitude, longitude)
    return coordinates

file_path = 'city_locations.txt'
city_coordinates = read_coordinates(file_path)
print("City coordinates:", city_coordinates) 