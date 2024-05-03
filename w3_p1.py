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


distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

max_iterations = 10000
initial_temperature = 100.0
cooling_rate = 0.90

# Perform simulated annealing
best_tour, best_distance = simulated_annealing(
    distances, max_iterations, initial_temperature, cooling_rate)

# Visualization
cities = len(distances)
x = [random.random() * 100 for _ in range(cities)]
y = [random.random() * 100 for _ in range(cities)]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', s=100)
for i, txt in enumerate(range(cities)):
    plt.annotate(txt, (x[i], y[i]), fontsize=12)

for i in range(cities - 1):
    plt.plot([x[best_tour[i]], x[best_tour[i + 1]]],
             [y[best_tour[i]], y[best_tour[i + 1]]], c='red')
plt.plot([x[best_tour[-1]], x[best_tour[0]]],
         [y[best_tour[-1]], y[best_tour[0]]], c='red')

plt.title("Traveling Salesman Problem - Best Tour")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.grid(True)
plt.show()

print("Best Tour:", best_tour)
print("Best Distance:", best_distance)
