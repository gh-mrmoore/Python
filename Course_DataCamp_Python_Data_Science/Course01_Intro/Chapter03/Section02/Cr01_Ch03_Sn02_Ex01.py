# Add a label to Deshaun's plot
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label="Deshaun")

# Officer Aditya
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Officer Mengfei
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display plot
plt.show()