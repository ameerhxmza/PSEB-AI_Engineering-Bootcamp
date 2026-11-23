# ==============================================================================
# Assignment 2 — NumPy Basics
# PSEB AI Engineering Bootcamp
# Trainee Name: Ameer Hamza
# Trainee ID: TRN-2026-001056
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# Exercise 1 — Array creation
# ------------------------------------------------------------------------------
print("=" * 60)
print("EXERCISE 1: ARRAY CREATION")
print("=" * 60)

arr = np.array([5, 10, 15, 20, 25])
print("Array:", arr)
print("Number of dimensions (ndim):", arr.ndim)
print("Shape of array:", arr.shape)
print("Total size (number of elements):", arr.size)
print("Data type (dtype):", arr.dtype)

# ------------------------------------------------------------------------------
# Exercise 2 — Indexing and slicing
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 2: INDEXING AND SLICING")
print("=" * 60)

values = np.array([12, 24, 36, 48, 60, 72, 84, 96])
print("Original values:", values)
print("1. First element:", values[0])
print("2. Last element:", values[-1])
print("3. Elements from index 2 to 4 (excluding 5):", values[2:5])
print("4. Every second element:", values[::2])
print("5. Reversed array:", values[::-1])

# ------------------------------------------------------------------------------
# Exercise 3 — 2D array
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 3: 2D ARRAY")
print("=" * 60)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("2D Array:\n", matrix)
print("\n1. Value 50:", matrix[1, 1])
print("2. Second row:", matrix[1])
print("3. Third column:", matrix[:, 2])
print("4. Sum of each row:", matrix.sum(axis=1))
print("5. Average of each column:", matrix.mean(axis=0))

# ------------------------------------------------------------------------------
# Exercise 4 — Filtering
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 4: FILTERING")
print("=" * 60)

ages = np.array([15, 22, 17, 30, 16, 25, 19])
print("Ages:", ages)
print("1. Ages >= 18:", ages[ages >= 18])
print("2. Ages < 18:", ages[ages < 18])
print("3. Ages between 18 and 25 (inclusive):", ages[(ages >= 18) & (ages <= 25)])

# ------------------------------------------------------------------------------
# Exercise 5 — Reshaping
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 5: RESHAPING")
print("=" * 60)

numbers = np.arange(1, 21)
print("Original 1D array (1 to 20):\n", numbers)
grid = numbers.reshape(4, 5)
print("\nReshaped 4x5 array:\n", grid)
print("\nFirst two rows:\n", grid[:2])

# ------------------------------------------------------------------------------
# Exercise 6 — Sales analysis
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 6: SALES ANALYSIS")
print("=" * 60)

sales = np.array([1200, 1500, 900, 1800, 2000, 1100, 1700])
print("Daily Sales:", sales)
print("1. Total sales:", sales.sum())
print("2. Average sales:", round(sales.mean(), 2))
print("3. Highest sales:", sales.max(), "| Lowest sales:", sales.min())
print("4. Sales greater than 1500:", sales[sales > 1500])
print("   Recorded on Days:", np.where(sales > 1500)[0] + 1)
print("5. Sales after 10% increase:", sales * 1.10)

# ------------------------------------------------------------------------------
# Exercise 7 — Student result system
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 7: STUDENT RESULT SYSTEM")
print("=" * 60)

marks = np.array([
    [75, 80, 85],   # Student 1
    [45, 60, 55],   # Student 2
    [90, 88, 92],   # Student 3
    [52, 50, 70]    # Student 4
])
print("Student Marks (Rows = Students, Columns = Subjects):\n", marks)
print("\n1. Total marks per student:", marks.sum(axis=1))
print("2. Average marks per student:", np.round(marks.mean(axis=1), 2))
print("3. Highest mark in each subject:", marks.max(axis=0))

passed_all = np.all(marks >= 50, axis=1)
print("4. Passed all subjects (marks >= 50):", passed_all)
print("   Students who scored at least 50 in all subjects: Students", list(np.where(passed_all)[0] + 1))

# ------------------------------------------------------------------------------
# Exercise 8 — Challenge: Temperature analysis
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXERCISE 8: TEMPERATURE ANALYSIS")
print("=" * 60)

temperatures = np.array([
    [32, 34, 36, 33, 31, 35, 37],  # Week 1
    [29, 30, 32, 35, 38, 36, 34],  # Week 2
    [33, 35, 37, 39, 40, 36, 32]   # Week 3
])
print("Temperatures (3 Weeks x 7 Days):\n", temperatures)
print("\n1. Average temperature per week:", np.round(temperatures.mean(axis=1), 2))
print("2. Average temperature per day (across 3 weeks):", np.round(temperatures.mean(axis=0), 2))
print("3. Highest temperature:", temperatures.max())
print("4. Temperatures above 35:", temperatures[temperatures > 35])

