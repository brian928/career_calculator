import matplotlib.pyplot as plt

def career_projection(college_years, college_cost_per_year,
                      starting_salary, annual_raise,
                      working_years):
    """
    Returns year-by-year net earnings after factoring in
    college costs, salary growth, and working years.
    """
    earnings = []
    total = 0

    # College years = negative earnings (costs)
    for _ in range(college_years):
        total -= college_cost_per_year
        earnings.append(total)

    # Career years = salary grows each year
    salary = starting_salary
    for _ in range(working_years):
        total += salary
        earnings.append(total)
        salary *= (1 + annual_raise)

    return earnings


def find_break_even(earningsA, earningsB):
    """
    Find the first year where Career B surpasses Career A.
    Returns (year, earningsB) or None if never.
    """
    for year in range(min(len(earningsA), len(earningsB))):
        if earningsB[year] >= earningsA[year]:
            return year, earningsB[year]
    return None


# Example career paths
careerA = {
    "name": "Food Scientist Master's Degree",
    "college_years": 2,
    "college_cost_per_year": 0,
    "starting_salary": 70000,
    "annual_raise": 0.03,   # 3%
    "working_years": 43
}

careerB = {
    "name": "Pharmacist Doctorate Degree",
    "college_years": 4,
    "college_cost_per_year": 25000,
    "starting_salary": 120000,
    "annual_raise": 0.03,    # 3%
    "working_years": 41
}

careerC = {
    "name": "MLS Degree",
    "college_years": 2,
    "college_cost_per_year": 12000,
    "starting_salary": 60000,
    "annual_raise": 0.03,    # 3%
    "working_years": 43
}

# Run projections
earningsA = career_projection(
    careerA["college_years"], careerA["college_cost_per_year"],
    careerA["starting_salary"], careerA["annual_raise"], careerA["working_years"]
)

earningsB = career_projection(
    careerB["college_years"], careerB["college_cost_per_year"],
    careerB["starting_salary"], careerB["annual_raise"], careerB["working_years"]
)

earningsC = career_projection(
    careerC["college_years"], careerC["college_cost_per_year"],
    careerC["starting_salary"], careerC["annual_raise"], careerC["working_years"]
)
# Find break-even point
break_even = find_break_even(earningsA, earningsB)

# --- Console Output ---
print("\n===== Career Earnings Summary =====")
print(f"{careerA['name']}: Final Net Earnings = ${earningsA[-1]:,.0f}")
print(f"{careerB['name']}: Final Net Earnings = ${earningsB[-1]:,.0f}")
print(f"{careerC['name']}: Final Net Earnings = ${earningsC[-1]:,.0f}")
if break_even:
    year, value = break_even
    print(f"Break-even: {careerB['name']} surpasses {careerA['name']} in Year {year} (Net: ${value:,.0f})")
else:
    print(f"No break-even point: {careerA['name']} always ahead")

# --- Graph Output ---
plt.figure(figsize=(10,6))
plt.plot(earningsA, label=f"{careerA['name']}", linewidth=2)
plt.plot(earningsB, label=f"{careerB['name']}", linewidth=2)
plt.plot(earningsC, label=f"{careerC['name']}", linewidth=2)

# Mark break-even if it exists
if break_even:
    year, value = break_even
    plt.scatter(year, value, color="red", zorder=5)
    plt.annotate(f"Break-even Year {year}\n(${value:,.0f})",
                 (year, value),
                 textcoords="offset points",
                 xytext=(20, -30),
                 arrowprops=dict(arrowstyle="->", color="red"))

plt.title("Career Earnings Comparison", fontsize=16)
plt.xlabel("Years (including college)", fontsize=12)
plt.ylabel("Cumulative Net Earnings ($)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()
