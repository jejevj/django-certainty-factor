# INI ADALAH CONTOH PERHITUNGAN, BELUM IMPLEMENTASI DI WEB
def filter_nonzero_values(list_p1, list_cf):
    list_p1_filtered = []
    list_cf_filtered = []

    for p1, cf in zip(list_p1, list_cf):
        if p1 != '0':
            list_p1_filtered.append(p1)
            list_cf_filtered.append(cf)

    return list_p1_filtered, list_cf_filtered

# List nilai P1 dan CF dari user
list_p1 = ['0.8', '0.7', '0.6', '0.7', '0.6', '0.6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
list_p2 = ['0.5', '0.4', '0.3', '0.4', '0.3', '0.4', '0.8', '0.7 ', '0.8', '0.6', '0.7 ', '0.8', '0', '0', '0', '0', '0']
list_p3 = ['0.2', '0.1', '0.1', '0.2', '0.1', '0.2', '0.4', '0.3', '0.5', '0.3', '0.4', '0.5', '0.8', '0.8', '0.9', '0.9', '0.9']
list_cf = ['1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0']

# Filter nilai 0
filtered_p1, filtered_cf1 = filter_nonzero_values(list_p1, list_cf)
filtered_p2, filtered_cf2 = filter_nonzero_values(list_p2, list_cf)
filtered_p3, filtered_cf3 = filter_nonzero_values(list_p3, list_cf)

# Tampilkan list_p1 dan list_cf yang sudah dihapus elemen yang memiliki nilai 0
print("List P1 setelah penghapusan nilai 0:", filtered_p1)
print("List CF setelah penghapusan nilai 0:", filtered_cf1)
print("")
print("List P2 setelah penghapusan nilai 0:", filtered_p2)
print("List CF setelah penghapusan nilai 0:", filtered_cf2)
print("")
print("List P3 setelah penghapusan nilai 0:", filtered_p3)
print("List CF setelah penghapusan nilai 0:", filtered_cf3)

def calculate_cf(condition, expert_cf, user_cf):
    return expert_cf * user_cf if condition == "Depresi Ringan" else 0

def combine_cf(cf, previous_cf, iteration):
    return previous_cf + cf * (1 - previous_cf) if iteration > 1 else cf

def calculate_combined_cf(list_pakar, list_user):
    combined_cf = 0

    for i in range(len(list_pakar)):
        expert_cf = float(list_pakar[i])
        user_cf = float(list_user[i])
        cf = calculate_cf("Depresi Ringan", expert_cf, user_cf)

        combined_cf = combine_cf(cf, combined_cf, i + 2)

    return combined_cf


combined_cf1 = calculate_combined_cf(filtered_p1, filtered_cf1)
percentage_cf1 = combined_cf1 * 100
combined_cf2 = calculate_combined_cf(filtered_p2, filtered_cf2)
percentage_cf2 = combined_cf2 * 100
combined_cf3 = calculate_combined_cf(filtered_p3, filtered_cf3)
percentage_cf3 = combined_cf3 * 100

print(percentage_cf1)
print(percentage_cf2)
print(percentage_cf3)