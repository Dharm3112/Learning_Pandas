# Learning Pandas 🐼

Welcome to the **Learning Pandas** repository\! This project documents my journey in mastering the Pandas library for data manipulation and analysis in Python. It contains a collection of organized examples and demos ranging from basic Series and DataFrames to more advanced operations like joining and concatenation.

## 📂 Repository Structure

The code is organized into folders based on the specific Pandas concept being demonstrated:

### 1\. Pandas DataFrame (`01_Pandas DataFrame`)

Basic examples of creating and manipulating DataFrames.

  * Creating DataFrames from dictionaries.
  * Custom indexing (`index=['RowA', ...]`).
  * Accessing data using `.loc` and `.iloc`.
  * Iterating over columns.

### 2\. DataFrame Attributes & Methods (`02_Pandas Dataframe Attribute And Methods`)

Exploring built-in attributes and methods to inspect DataFrames.

  * **Attributes:** `.dtypes`, `.ndim` (dimensions), `.size` (number of elements), `.shape` (tuple of rows/cols), `.index`, `.T` (Transpose).
  * **Methods:** `.head()` (first n rows), `.tail()` (last n rows).

### 3\. Joining DataFrames (`03_Pandas Join DataFrame`)

  * Demonstrations of joining two DataFrames using the `.join()` method.

### 4\. Concatenating DataFrames (`04_Pandas Concat Data Frame`)

  * Examples of combining DataFrames vertically using `pd.concat()`.

### 5\. Pandas Series (`05_Pandas Series`)

Introduction to the 1-dimensional Series data structure.

  * Creating Series from lists.
  * Using custom row labels/indexes.
  * Accessing values by label or position.

### 6\. Series Attributes & Methods (`06_Pandas Series Attribute Methods`)

Deep dive into Series inspection and manipulation.

  * **Attributes:** `.dtype`, `.ndim`, `.size`, `.name`, `.index`, `.hasnans` (checking for NaNs).
  * **Methods:** `.head()`, `.tail()`, `.info()` (summary).

### 7\. Combining Series (`07_Pandas Combine Series`)

  * Using the `.combine()` method with custom functions to merge data from two Series.

### 8\. Categorical Data (`08_Pandas Categorical Data`)

  * Working with memory-efficient `category` data types in both Series and DataFrames.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed along with the Pandas library.

```bash
pip install pandas
```

### How to Run

You can run any of the demo scripts individually to see the output. For example:

```bash
python "01_Pandas DataFrame/Pandas_DataFrame_Demo-1.py"
```

## 🛠 Tools Used

  * **Python**: Programming language.
  * **Pandas**: Data manipulation library.
  * **NumPy**: Used for numerical operations and `np.NaN`.
  * **PyCharm**: IDE (indicated by the `.idea` configuration files).

-----

*Created by [Dharm3112](https://www.google.com/search?q=https://github.com/Dharm3112)*
