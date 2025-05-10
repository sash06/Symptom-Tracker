# "Symptom Tracker"
# Health Checker: Blood Sugar and Blood Pressure

# --- Blood Sugar Check ---
blood_sugar = float(input("Enter your fasting blood sugar level (mg/dL): "))

if blood_sugar < 70:
    print("Blood Sugar: Low (Hypoglycemia)")
elif 70 <= blood_sugar <= 99:
    print("Blood Sugar: Normal")
elif 100 <= blood_sugar <= 125:
    print("Blood Sugar: Prediabetes")
elif blood_sugar >= 126:
    print("Blood Sugar: Diabetes")
else:
    print("Blood Sugar: Invalid input")

# --- Post-Meal Blood Sugar Check ---
post_sugar = float(input("Enter your blood sugar level 2 hours after eating (mg/dL): "))

if post_sugar < 70:
    print("Post-Meal Blood Sugar: Low (Hypoglycemia)")
elif 70 <= post_sugar < 140:
    print("Post-Meal Blood Sugar: Normal")
elif 140 <= post_sugar <= 199:
    print("Post-Meal Blood Sugar: Prediabetes")
elif post_sugar >= 200:
    print("Post-Meal Blood Sugar: Diabetes")
else:
    print("Post-Meal Blood Sugar: Invalid input")

# --- Blood Pressure Check ---
systolic = int(input("Enter your systolic BP (top number): "))
diastolic = int(input("Enter your diastolic BP (bottom number): "))

if systolic < 90 or diastolic < 60:
    print("Blood Pressure: Low (Hypotension)")
elif 90 <= systolic < 120 and 60 <= diastolic < 80:
    print("Blood Pressure: Normal")
elif 120 <= systolic < 130 and diastolic < 80:
    print("Blood Pressure: Elevated")
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    print("Blood Pressure: Hypertension Stage 1")
elif 140 <= systolic <= 179 or 90 <= diastolic <= 119:
    print("Blood Pressure: Hypertension Stage 2")
elif systolic >= 180 or diastolic >= 120:
    print("Blood Pressure: Hypertensive Crisis (Seek emergency care)")
else:
    print("Blood Pressure: Invalid input")
