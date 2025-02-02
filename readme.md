# OS Scheduling Algorithms Simulator


This project implements three popular page replacement (scheduling) algorithms used in operating systems:

- **LRU (Least Recently Used)**
- **FIFO (First In, First Out)**
- **Clock Algorithm**

---

## Introduction

Efficient memory management is a cornerstone of modern operating systems. When system memory is limited, **page replacement algorithms** determine which pages to remove, ensuring that the most critical data stays accessible. This repository provides implementations of three key algorithms:

1. **LRU (Least Recently Used):** Evicts the page that has not been used for the longest period.
2. **FIFO (First In, First Out):** Removes pages in the order they were added, regardless of usage frequency.
3. **Clock Algorithm:** Uses a circular buffer (the "clock") with a reference bit for each page, approximating LRU with less overhead.

---

## Algorithms Overview

### LRU (Least Recently Used)

**Concept:**  
LRU is based on the idea that pages used recently will likely be used again soon. Conversely, pages not used for a long time are candidates for removal.

**How It Works:**  
- Each page has a timestamp or is maintained in an ordered data structure.
- When a page is accessed, its timestamp is updated.
- On a page fault, the algorithm removes the page with the oldest timestamp.

**Pros:**
- Highly effective when recent history is a good predictor of future accesses.

**Cons:**
- Can be expensive to implement if not using efficient data structures (e.g., linked lists, hash maps).

---

### FIFO (First In, First Out)

**Concept:**  
FIFO is one of the simplest page replacement algorithms. It removes the oldest page in memory—i.e., the page that entered first.

**How It Works:**  
- Pages are queued in the order they arrive.
- When a new page must be loaded, the page at the front of the queue is removed.

**Pros:**
- Simple and easy to implement.

**Cons:**
- May remove pages that are still in active use, leading to suboptimal performance (known as the "Belady’s anomaly").

---

### Clock Algorithm

**Concept:**  
Also known as the “Second Chance” algorithm, the Clock algorithm is an efficient approximation of LRU.

**How It Works:**  
- Pages are arranged in a circular buffer (imagine a clock face).
- Each page has an associated reference bit that is set when the page is accessed.
- A “clock hand” sweeps through the pages:
  - If a page’s reference bit is **0**, it is replaced.
  - If the reference bit is **1**, it is cleared, and the clock hand moves on.
  
**Pros:**
- Reduces the overhead of maintaining a full LRU list while still approximating its behavior.

**Cons:**
- The approximation may not always be as effective as true LRU, depending on the workload.


