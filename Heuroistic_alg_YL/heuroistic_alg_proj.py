import numpy as np
import random
import sys

NUM_CITIES = 11
CITY_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
CITY_MAP = {city: i for i, city in enumerate(CITY_NAMES)}
INV_CITY_MAP = {i: city for i, city in enumerate(CITY_NAMES)}

POPULATION_SIZE = 100
MAX_GENERATIONS = 500
ELITISM_RATE = 0.10 

TARGET_DISTANCE = 253
TARGET_RANGE = 5

PLACEHOLDER_MATRIX = np.array([
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],  
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],  
    [20, 15, 0, 15, 17, 28, 92, 9, 21, 29, 13],  
    [21, 29, 15, 0, 10, 12, 98, 12, 25, 30, 21],  
    [16, 28, 17, 10, 0, 16, 94, 9, 20, 24, 15],  
    [31, 40, 28, 12, 16, 0, 105, 25, 36, 38, 32],  
    [100, 72, 92, 98, 94, 105, 0, 90, 101, 109, 84], 
    [12, 21, 9, 12, 9, 25, 90, 0, 16, 28, 8],   
    [4, 29, 21, 25, 20, 36, 101, 16, 0, 35, 18],  
    [31, 41, 29, 30, 24, 38, 109, 28, 35, 0, 22],  
    [18, 12, 13, 21, 15, 32, 84, 8, 18, 22, 0]   
], dtype=float)

distance_matrix = PLACEHOLDER_MATRIX

def create_individual():
    individual = np.arange(NUM_CITIES)
    np.random.shuffle(individual)
    return individual

def create_initial_population():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(create_individual())
    return np.array(population)

def calculate_distance(individual):
    total_distance = 0.0
    for i in range(NUM_CITIES):
        current_city_idx = individual[i]
        next_city_idx = individual[0] if i == NUM_CITIES - 1 else individual[i + 1]
        total_distance += distance_matrix[current_city_idx, next_city_idx]
    return total_distance

def selection(ranked_population):
    tournament_size = 3
    selected_indices = np.random.choice(len(ranked_population), tournament_size, replace=False)
    tournament = [ranked_population[i] for i in selected_indices]
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]

def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        child = np.full(NUM_CITIES, -1, dtype=int)
        start, end = sorted(random.sample(range(NUM_CITIES), 2))
        child[start:end+1] = parent1[start:end+1]
        missing_genes = parent2[~np.isin(parent2, child)]
        child[child == -1] = missing_genes
        return child
    else:
        return parent1.copy()

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        pos1, pos2 = random.sample(range(NUM_CITIES), 2)
        individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual

def run_genetic_algorithm(c_rate, m_rate):
    population = create_initial_population()
    best_distance = np.inf
    best_path = np.array([])
    final_generation = MAX_GENERATIONS
    
    for generation in range(MAX_GENERATIONS):
        ranked_population = []
        for ind in population:
            distance = calculate_distance(ind)
            ranked_population.append([ind, distance])
            
        ranked_population.sort(key=lambda x: x[1])
        
        current_best_distance = ranked_population[0][1]
        
        if current_best_distance < best_distance:
            best_distance = current_best_distance
            best_path = ranked_population[0][0]
            
        if (TARGET_DISTANCE - TARGET_RANGE) <= best_distance <= (TARGET_DISTANCE + TARGET_RANGE):
            print(f"Durdurma koşulu {generation}. nesilde karşılandı (Mesafe: {best_distance:.2f} km)")
            final_generation = generation
            break
            
        new_population = []
        
        elite_count = int(POPULATION_SIZE * ELITISM_RATE)
        for i in range(elite_count):
            new_population.append(ranked_population[i][0]) 
            
        for _ in range(POPULATION_SIZE - elite_count):
            parent1 = selection(ranked_population)
            parent2 = selection(ranked_population)
            child = crossover(parent1, parent2, c_rate)
            child = mutate(child, m_rate)
            new_population.append(child)
            
        population = np.array(new_population)
        
    return best_path, best_distance, final_generation

def path_to_letters(path_indices):
    return [INV_CITY_MAP[idx] for idx in path_indices]

def run_experiments():
    crossover_rates = [0.85, 0.9, 0.95]
    mutation_rates = [0.1, 0.15, 0.2]
    
    results = []
    
    for c_rate in crossover_rates:
        for m_rate in mutation_rates:
            print(f"\n-- C-Rate={c_rate}, M-Rate={m_rate} --")
            path_indices, distance, gens = run_genetic_algorithm(c_rate, m_rate)
            path_letters = path_to_letters(path_indices)
            
            print(f"SONUÇ: En İyi Mesafe = {distance:.2f} km ({gens} nesil sonra)")
            print(f"En İyi Rota (Harf): {'-'.join(path_letters)}")
            
            results.append({
                "c_rate": c_rate,
                "m_rate": m_rate,
                "distance": distance,
                "path_indices": path_indices, 
                "generations": gens
            })
            
    best_overall_result = min(results, key=lambda x: x['distance'])
    best_path_letters = path_to_letters(best_overall_result['path_indices'])
    
    print("\n\n" + "="*50)
    print("--  TÜM DENEY SONUÇLARI --")
    print("="*50)
    print("| C-Rate | M-Rate | En İyi Mesafe (km) | Nesil Sayısı |")
    print("------------------------------")
    for res in results:
        print(f"| {res['c_rate']:<6} | {res['m_rate']:<6} | {res['distance']:<18.2f} | {res['generations']:<12} |")
    print("="*50)
    
    print("\n EN İYİ PERFORMANS GÖSTEREN PARAMETRELER")
    print(f"C-Rate: {best_overall_result['c_rate']}, M-Rate: {best_overall_result['m_rate']}")
    print(f"Elde edilen en iyi mesafe: {best_overall_result['distance']:.2f} km")
    print(f"Elde edilen en iyi rota: {'-'.join(best_path_letters)}")
    print(f"\nOptimal Çözüm (Hedef): {TARGET_DISTANCE} +/- {TARGET_RANGE} km")
    
    if (TARGET_DISTANCE - TARGET_RANGE) <= best_overall_result['distance'] <= (TARGET_DISTANCE + TARGET_RANGE):
        print("Karşılaştırma: Başarılı \n Bulunan en iyi çözüm, verilen optimal çözüm aralığındadır.")
    else:
        print(f"Karşılaştırma: Bulunan en iyi çözüm ({best_overall_result['distance']:.2f} km), optimal aralığa ({TARGET_DISTANCE - TARGET_RANGE} - {TARGET_DISTANCE + TARGET_RANGE} km) ulaşamadı.")

if __name__ == "__main__":
    run_experiments()