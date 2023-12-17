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


# Calculate combined CF
# combined_cf = calculate_combined_cf(listPakar, listUser)
# percentage_cf = combined_cf * 100

# Convert to percentage
# print("Combined CF (1/6) as Percentage:", percentage_cf, "%")
