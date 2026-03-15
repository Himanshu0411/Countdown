# Countdown
# 🎉 New Year Countdown (Python)

A simple Python program that creates a countdown timer and prints **"Happy New Year"** when the countdown finishes.

## 📌 Features

* Takes countdown number from user
* Counts down every second
* Prints a celebration message at the end
* Beginner-friendly Python project

## 🖥️ Code

```python
import time

count = int(input("Enter the counter num: "))

print("\nCountdown starts now:")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("🎉 Happy New Year 🎉")
```

## ▶️ How to Run

1. Install Python (if not installed).
2. Save the file as `countdown.py`
3. Run the program:

```bash
python countdown.py
```

4. Enter the countdown number and watch the timer start.

## 📷 Example Output

```
Enter the counter num: 5

Countdown starts now:
5
4
3
2
1

🎉 Happy New Year 🎉
```

## 📚 Technologies Used

* Python
* time module

## 🙌 Author

⭐ If you like this project, consider giving it a star on GitHub!
