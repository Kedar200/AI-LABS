import random
import math
import matplotlib.pyplot as plt

# Function to calculate the total distance of a tour


def total_distance(tour, distances):
    total = 0
    for i in range(len(tour)):
        total += distances[tour[i - 1]][tour[i]]
    return total

# Function to generate a random initial tour


def initial_tour(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

# Function to generate a neighboring solution by swapping two cities


def perturb_tour(tour):
    i, j = sorted(random.sample(range(len(tour)), 2))
    tour[i:j + 1] = reversed(tour[i:j + 1])
    return tour

# Simulated annealing algorithm


def simulated_annealing(distances, max_iterations, initial_temperature, cooling_rate):
    num_cities = len(distances)
    current_tour = initial_tour(num_cities)
    current_distance = total_distance(current_tour, distances)
    best_tour = current_tour[:]
    best_distance = current_distance

    temperature = initial_temperature

    for iteration in range(max_iterations):
        new_tour = perturb_tour(current_tour)
        new_distance = total_distance(new_tour, distances)

        # Calculate acceptance probability
        if new_distance < current_distance or random.random() < math.exp(
                (current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance

            # Update the best tour if needed
            if current_distance < best_distance:
                best_tour = current_tour[:]
                best_distance = current_distance

        # Cool down the temperature
        temperature *= cooling_rate

    return best_tour, best_distance

# Read .tsp file and extract city coordinates


def read_tsp_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    coordinates = []
    for line in lines:
        if line.strip().isdigit():
            break
        if line.strip().isdigit() or line.strip() == 'EOF':
            continue
        parts = line.strip().split()
        coordinates.append((float(parts[1]), float(parts[2])))

    return coordinates

# Calculate distances between cities


def calculate_distances(coordinates):
    num_cities = len(coordinates)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distances[i][j] = distances[j][i] = math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 +
                                                          (coordinates[i][1] - coordinates[j][1]) ** 2)
    return distances


# Example .tsp file path
tsp_file_path = 'xqg237.tsp'

# Read .tsp file and extract city coordinates
coordinates = read_tsp_file(tsp_file_path)

# Calculate distances between cities
distances = calculate_distances(coordinates)

# Parameters for simulated annealing
max_iterations = 10000
initial_temperature = 100.0
cooling_rate = 0.99

# Perform simulated annealing
best_tour, best_distance = simulated_annealing(
    distances, max_iterations, initial_temperature, cooling_rate)

# Visualization
plt.figure(figsize=(8, 6))
for i in range(len(coordinates)):
    plt.scatter(coordinates[i][0], coordinates[i][1], c='blue', s=100)
    plt.annotate(i, (coordinates[i][0], coordinates[i][1]), fontsize=12)

for i in range(len(best_tour) - 1):
    plt.plot([coordinates[best_tour[i]][0], coordinates[best_tour[i + 1]][0]],
             [coordinates[best_tour[i]][1], coordinates[best_tour[i + 1]][1]], c='red')
plt.plot([coordinates[best_tour[-1]][0], coordinates[best_tour[0]][0]],
         [coordinates[best_tour[-1]][1], coordinates[best_tour[0]][1]], c='red')

plt.title("Traveling Salesman Problem - Best Tour")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.grid(True)
plt.show()

print("Best Tour:", best_tour)
print("Best Distance:", best_distance)
