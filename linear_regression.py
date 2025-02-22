#Regression linéaire

X = [12, 13, 15, 20, 22, 23, 30, 40, 45]  # Engrais en kilogrammes
Y = [12, 13, 14, 19, 22, 24, 31, 39, 44]  # Rendement en dollars

# 1. Calcul des moyennes
xbar = sum(X) / len(X)
ybar = sum(Y) / len(Y)

# 2. Calcul des écarts
x_xbar = [x - xbar for x in X]
y_ybar = [y - ybar for y in Y]

# 3. Covariance de X et Y
Cov_X_Y = sum(x * y for x, y in zip(x_xbar, y_ybar)) / len(X)

# 4. Variance de X
Var_X = sum(x**2 for x in x_xbar) / len(X)

# 5. Coefficients de la droite de régression
a = Cov_X_Y / Var_X
b = ybar - (a * xbar)

# 6. Prédictions Y
prevision_Y = [a * x + b for x in X]

# 7. Affichage des résultats
print(f"Equation de la droite  de moindre carrée: Y = {a:.2f}X + {b:.2f}")
print("Prévisions :", prevision_Y)

sum_error  = sum(y - yprevision for y , yprevision in zip(Y, prevision_Y))
print(sum_error)

# 8. prédiction avec un input
x_input = float(input("Entrez la quantité d'engrais (kg) : "))
y_prediction = a * x_input + b

print(f"Pour {x_input} kg d'engrais, la prédiction du rendement est de {y_prediction:.2f} $")
