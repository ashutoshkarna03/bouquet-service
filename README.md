# Bouquet Service

This project is a command-line application that simulates a simplified bouquet production process for a flower business. It reads bouquet design specifications and a stream of incoming flowers, and outputs bouquets as soon as enough flowers are available to fulfill any design.

---

## Problem Statement

- Flowers of different species and sizes arrive individually at the facility.
- Bouquets are produced according to design specifications.
- The application must output a bouquet as soon as enough flowers have been provided to satisfy any design.

---

## Input/Output Specifications

- **Input:**  
  1. One or more bouquet design lines (see format below), each on its own line.  
  2. An empty line.  
  3. A stream of individual flowers, one per line.

- **Output:**  
  - Each time a bouquet can be made for any design, print it in the specified format (see below).

---

## Data Specifications

- **Flower:**  
  - Species: single lowercase letter (`a`-`z`)
  - Size: single uppercase letter (`L` or `S`)
  - Example: `rL` (large rose)

- **Design:**  
  - Format:  
    `...`
  - Example: `AL1d2r3t5` means design "A", large flowers, up to 1 "d", 2 "r", 3 "t", total 5 flowers

- **Bouquet (Output):**  
  - Format:  
    `...`
  - Example: `AL1d2r2t`

- **Rules:**  
  - Each bouquet must use all and only the species in the design (at least 1 of each, up to the max per species).
  - The sum of flower quantities must equal the design's total.

---

## Example

**Input:**

```
AS2a2b3
BL2a2

aL
bS
aS
bS
aS
aL
aS
bS
```

**Output:**
```
AS1a2b
BL2a
AS2a1b
```

---

## Approach to the solution

1. **Parse Designs:**
Read all bouquet design lines from input until the empty line, extracting the design name, flower size, required species, their max quantities, and the total bouquet size.

2. **Track Incoming Flowers:**
For each flower line after the empty line, update an inventory (organized by size and species) to count available flowers.

3. **Check for Bouquet Creation:**
After each flower arrival, check every design to see if enough flowers are available (correct size, required species, at least 1 and at most the max per species, sum equals design total).

4. **Produce Bouquets:**
When a design can be fulfilled, select the combination of flowers (using a greedy or systematic approach), output the bouquet in the required format, and remove those flowers from inventory.

5. **Repeat Until Input Ends:**
Continue processing incoming flowers and producing bouquets as soon as possible until all input is consumed.

6. **Standard Input/Output:**
The program reads from standard input and writes to standard output, as required by the challenge.

7. **Dockerization:**
The solution includes a Dockerfile so it can be built and run in a containerized environment as specified in the requirements.

---

## Project Structure

```
.
├── bouquet.py          # Main application script
├── requirements.txt    # Python dependencies (pytest for testing)
├── Dockerfile          # For containerized execution
├── test_bouquet.py     # Pytest test cases
└── README.md           # This file
```

---

## How to Run

### 1. **Install Locally**

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the program with input from a file:
```
python bouquet.py < input.txt
```
Note: you can also output it in a file: python bouquet.py < input.txt > output.txt

---

### 2. **Run with Docker**

Build the Docker image:
```
docker build -t bouquet-service .
```

Run the container, piping in your input:
```
docker run -i bouquet-service < input.txt
```

---

### 3. **Run Tests**

To run the test suite (requires pytest):
```
pytest test_bouquet.py
```

---

## Files

- `bouquet.py` — Main application logic.
- `requirements.txt` — Project dependencies (`pytest` for testing).
- `Dockerfile` — Containerizes the application for easy execution.
- `test_bouquet.py` — Automated test cases using pytest.
- `README.md` — Project documentation and instructions.

---
