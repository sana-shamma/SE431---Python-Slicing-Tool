# Slicing Tool 🛠️✨

Welcome to the **Slicing Tool** project, a Python-based utility designed to perform slicing on source code to identify variable dependencies and line numbers. This tool is specifically developed for the Software Maintenance and Evolution course, providing a practical approach to understanding and analyzing variable dependencies in Python code.

## Project Overview

This project implements a static slicing tool that focuses on variable dependencies in Python code. It serves as a valuable resource for software maintenance and evolution tasks, enabling developers and researchers to gain insights into variable relationships and dependencies within a given Python script. By analyzing variable dependencies, developers can better understand the impact of changes, identify potential issues, and make informed decisions during the software maintenance process.

### How It Works

1. **Reverse File Reading**: The tool starts by reversing the lines of the source code file, enabling the analysis of variable dependencies in a backward manner.
2. **Line Counting**: The tool counts the number of lines in the reversed file, providing insights into the code's size and complexity.
3. **User Input**: The user selects a variable from a predefined list to analyze, allowing targeted exploration of specific variables.
4. **Dependency Analysis**: The tool analyzes the source code in reverse to identify dependencies involving the selected variable. This analysis helps identify the variables that influence or are influenced by the selected variable, aiding in understanding the code's behavior and potential impacts during maintenance.
5. **Output**: The tool displays the identified variable dependencies and the corresponding line numbers, assisting developers in locating and understanding the relevant sections of the code.

### Usage Instructions

1. **Prepare Your Source Code**: Ensure your Python source code file (e.g., `fifo.py`) follows the tool's requirements, such as adhering to Python syntax and conventions.
2. **Run the Tool**: Execute the `Python-Slicing-Tool.py` script to launch the slicing tool.
3. **Select a Variable**: Choose a variable from the displayed list to perform the slicing analysis on that variable.
4. **View Results**: The tool will display the identified variable dependencies and their corresponding line numbers, aiding in understanding the interactions and potential impacts.

### Restrictions

To ensure accurate slicing results and compatibility with the tool, please observe the following restrictions:

- The code should be written in Python.
- Shorthand methods like `i += 1` are not supported.
- Unassigned variables are not supported; all variables must be initialized and assigned a value.
- Print statements are disregarded in the analysis.

## Authors ✍️

- Bassant Mahmoud
- Salwa Shamma
- Samah Shamma
- Sana Shamma
- Samah Channa 
---

**Happy slicing! ✂️**
