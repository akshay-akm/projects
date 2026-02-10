# Farm Equipment Recommendation System

# Rule base
rules = [
    {
        "conditions": {
            "crop": "wheat",
            "soil": "clay",
            "irrigation": "yes",
            "farm_size": "large",
            "mechanized": "yes"
        },
        "recommendation": "Tractor"
    },
    {
        "conditions": {
            "crop": "rice",
            "soil": "loam",
            "irrigation": "yes",
            "farm_size": "medium",
            "mechanized": "no"
        },
        "recommendation": "Power Tiller"
    },
    {
        "conditions": {
            "crop": "sugarcane",
            "soil": "sandy",
            "irrigation": "no",
            "farm_size": "small",
            "mechanized": "no"
        },
        "recommendation": "Hand Tools"
    },
    {
        "conditions": {
            "irrigation": "yes",
            "farm_size": "small",
            "mechanized": "no"
        },
        "recommendation": "Sprayer"
    },
]

# Ask user for input (facts)
def get_user_input():
    print("Please provide the following details:")
    facts = {
        "crop": input("Crop type (wheat, rice, sugarcane): ").lower(),
        "soil": input("Soil type (clay, loam, sandy): ").lower(),
        "irrigation": input("Irrigation available? (yes/no): ").lower(),
        "farm_size": input("Farm size (small, medium, large): ").lower(),
        "mechanized": input("Mechanized? (yes/no): ").lower()
    }
    return facts

# Forward chaining inference
def forward_chaining(facts):
    for rule in rules:
        if all(facts.get(k) == v for k, v in rule["conditions"].items()):
            return rule["recommendation"]
    return "Manual Labor"

# Main function
def main():
    facts = get_user_input()
    recommendation = forward_chaining(facts)
    print("\n✅ Recommended Equipment:", recommendation)

if __name__ == "__main__":
    main()
