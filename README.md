**TASK 5 – Data Analysis on CSV Files**

This project performs **data analysis and visualization** on a CSV file named **`sales_data.csv`** using **Pandas** and **Matplotlib**.

---

## 📁 **Project Structure**

```
task5/
│
├── analysis.py
├── sales_data.csv
└── README.md   
```

---

## 🚀 **How to Run the Project**

### **1. Install Dependencies**

Make sure Python is installed.
Then install required libraries:

```bash
pip install pandas matplotlib
```

---

### **2. Run the Script**

Navigate to your project folder:

```bash
cd task5
```

Run the analysis:

```bash
python analysis.py
```

---

## 📝 **What This Script Does**

### ✅ **Step 1: Load the CSV File**

Loads `sales_data.csv` into a Pandas DataFrame and prints the first 5 rows.

### ✅ **Step 2: Basic Data Insights**

Displays:

* Shape of the data
* Summary statistics
* Count of missing values

### ✅ **Step 3: GroupBy Operations**

Performs groupby on:

* **Region** → Total Sales
* **Product Category** → Total Sales
* **Sales Representative** → Total Sales

### ✅ **Step 4: Filtering**

Shows sales where **Sales_Amount > 8000**.

### ✅ **Step 5: Visualizations**

Creates bar charts for:

* Sales by Region
* Sales by Product Category
* Sales by Sales Representative

These charts will open automatically using Matplotlib.

---

## 📦 **Output**

When you run `analysis.py`, you will get:

* Console outputs (head, shape, statistics, groupby results)
* Graphs for each category
* A success message:
  **"✔ TASK COMPLETED SUCCESSFULLY!"**

---


