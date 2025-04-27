def perfume_customisation_survey():
    print("\n✨ Welcome to the Perfume Customisation Survey ✨\n")

    answers = {}

    # Personal Information
    name = input("What is your name? ").strip()
    gender = input("What is your gender? (Male / Female / Non-binary / Prefer not to say / Other): ").strip().title()

    answers['name'] = name
    answers['gender'] = gender

    # Basic Information
    print("\n-- Basic Information --")
    age = input("What is your age group?\n(A: Under 18 / B: 18-25 / C: 26-40 / D: 41-60 / E: Over 60): ").strip().upper()
    occupation = input("What is your occupation?\n(A: Student / B: Working Professional / C: Outdoor Worker / D: Artist / E: Retired / F: Other): ").strip().upper()

    answers['age'] = age
    answers['occupation'] = occupation

    # Scenario
    print("\n-- Perfume Usage Scenario --")
    scenario = input("When do you want to wear this perfume?\n(A: Daily / B: Special Events / C: Romantic Moments / D: Relaxation / E: Adventure): ").strip().upper()
    answers['scenario'] = scenario

    # Vibe based on Scenario
    print("\n-- Vibe Selection --")
    if scenario == 'A':
        vibe = input("Choose a vibe:\n(A: Fresh & Clean / B: Subtle & Elegant / C: Energetic & Bright): ").strip().upper()
    elif scenario == 'B':
        vibe = input("Choose a vibe:\n(A: Bold & Glamorous / B: Rich & Mysterious / C: Luxurious & Warm): ").strip().upper()
    elif scenario == 'C':
        vibe = input("Choose a vibe:\n(A: Soft & Sweet / B: Sensual & Deep / C: Dreamy & Romantic): ").strip().upper()
    elif scenario == 'D':
        vibe = input("Choose a vibe:\n(A: Light & Airy / B: Cozy & Comforting / C: Soft Floral): ").strip().upper()
    elif scenario == 'E':
        vibe = input("Choose a vibe:\n(A: Vibrant & Playful / B: Earthy & Natural / C: Free-Spirited & Bright): ").strip().upper()
    else:
        vibe = 'Unknown'

    answers['vibe'] = vibe

    # Scent Family based on Vibe
    print("\n-- Scent Family Selection --")
    vibe_mapping = {
        'A': ['Citrus', 'Aquatic', 'Green'],
        'B': ['Woody', 'Spicy', 'Amber'],
        'C': ['Floral', 'Sweet', 'Gourmand']
    }

    scent_family_options = vibe_mapping.get(vibe, ['Floral', 'Woody', 'Fruity'])
    scent_family = input(f"Choose a scent family from: {', '.join(scent_family_options)}: ").strip().title()
    answers['scent_family'] = scent_family

    # Longevity
    print("\n-- Longevity Preference --")
    longevity = input("How long do you want the scent to last?\n(A: Light 2-4hrs / B: Medium 6-8hrs / C: Strong 10+hrs): ").strip().upper()
    answers['longevity'] = longevity

    # Perfume Recommendation Logic
    print("\n\U0001F49C Finding your perfect perfumes...\n")

    recommendation = "No match found."

    # Expanded Matching
    matching_conditions = {
        ('A', 'A', 'A', 'A', 'Citrus'): "Clinique Happy, Marc Jacobs Daisy Eau So Fresh",
        ('A', 'A', 'B', 'A', 'Floral'): "Ariana Grande Cloud Pink, Miss Dior Blooming Bouquet",
        ('A', 'A', 'C', 'A', 'Fruity'): "Escada Candy Love, Victoria's Secret Tease",
        ('A', 'A', 'D', 'A', 'Aquatic'): "Bath and Body Works Sea Island Cotton, Dolce & Gabbana Light Blue",
        ('A', 'A', 'E', 'A', 'Fruity'): "Escada Sorbetto Rosso, Hollister Wave for Her",
        ('A', 'A', 'A', 'C', 'Green'): "Moschino Toy 2 Bubble Gum, Gucci Flora Gorgeous Jasmine",
        ('A', 'A', 'B', 'C', 'Sweet'): "YSL Mon Paris Eau de Toilette, Vera Wang Princess",
        ('B', 'B', 'B', 'A', 'Amber'): "YSL Libre Intense, Carolina Herrera Good Girl",
        ('C', 'B', 'A', 'B', 'Woody'): "Chanel Coco Mademoiselle EDT, Hermès Terre d’Hermès",
        ('B', 'D', 'C', 'C', 'Floral'): "Maison Margiela Replica Bubble Bath, Chanel Chance Eau Tendre",
        ('E', 'E', 'D', 'B', 'Vanilla'): "Guerlain Mon Guerlain, Prada L’Homme Intense",
        ('D', 'D', 'E', 'A', 'Fruity'): "Dolce & Gabbana Dolce Garden, Mancera Holidays",
        ('B', 'B', 'A', 'C', 'Green'): "Chanel Chance Eau Fraîche, Hermès Un Jardin Sur Le Nil",
        ('C', 'B', 'C', 'B', 'Spicy'): "Tom Ford Black Orchid, Lancôme La Nuit Trésor"
    }

    key = (age, occupation, scenario, vibe, scent_family)
    if key in matching_conditions:
        recommendation = f"Recommended Perfumes: {matching_conditions[key]}"
    else:
        # Fallback recommendation based on scent family
        fallback_recommendations = {
            'Floral': "Chloe Eau de Parfum, Gucci Bloom",
            'Woody': "Tom Ford Oud Wood, Le Labo Another 13",
            'Citrus': "Dior Eau Sauvage, Jo Malone Lime Basil & Mandarin",
            'Fruity': "Escada Cherry in the Air, Ariana Grande Sweet Like Candy",
            'Sweet': "Kayali Vanilla 28, Viktor & Rolf Bonbon",
            'Amber': "YSL Black Opium, Givenchy L'Interdit"
        }
        recommendation = f"Fallback Perfumes: {fallback_recommendations.get(scent_family, 'No fallback available')}"

    # Output results
    print(f"\n🎀 Hello {name}! Here are your perfume recommendations 🎀")
    print(f"Gender: {gender}")
    print(f"{recommendation}")

    print("\nSummary of your answers:")
    for key, value in answers.items():
        print(f"{key.capitalize()}: {value}")

    print("\n✨ Thank you for using the survey! Data collected by Ivy.H ✨")

# Run the survey
if __name__ == "__main__":
    perfume_customisation_survey()