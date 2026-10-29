# CRISPR-Cas9 gRNA & PAM Scanner

A precision bioinformatics Python tool designed to scan raw DNA sequences for SpCas9 PAM sites (`NGG`), extract upstream 20-nt guide RNAs (gRNAs), and evaluate their laboratory viability using standard molecular biology criteria.

---

## Biological Overview & Mechanism

The **CRISPR-Cas9** system is an RNA-guided genome editing platform derived from bacterial adaptive immunity:
1. **PAM Recognition:** The *Streptococcus pyogenes* Cas9 (SpCas9) endonuclease strictly requires a Protospacer Adjacent Motif (PAM) with the sequence **`5'-NGG-3'`** on the non-target DNA strand to initiate binding and unwinding.
2. **Target Specificity (gRNA):** Upstream of the PAM site, a **20-nucleotide spacer** directs Cas9 to introduce a targeted double-strand break (DSB).
3. **On-Target Viability:** Successful editing requires optimal gRNA design:
   * **GC-Content Balance:** An optimal range of **40% – 60%** ensures stable binding without excessive off-target risks or secondary hairpins.
   * **Absence of Poly-T Tracts:** Consecutive thymines (`TTTT`) act as premature transcription termination signals for RNA Polymerase III during intracellular gRNA expression.

---

## Features

- **Automated Motif Detection:** Scans full genomic sequences for canonical SpCas9 PAM sites (`[ATGC]GG`) using optimized regular expressions.
- **Spacer Extraction:** Automatically isolates the upstream 20-nt candidate gRNA sequences.
- **Dual Biological Filtering:**
  - Calculates GC content percentage.
  - Detects inhibitory poly-T tracts (`TTTT`).
- **Structured Output:** Formats candidates into a clear comparative matrix displaying target position, PAM sequence, GC%, approval status, and biological evaluation notes.

---

## Target Quality Matrix

| Status | Criterion | Biological Rationale |
| :--- | :--- | :--- |
| **Optimal** | 40% ≤ GC% ≤ 60%, No Poly-T | Ideal binding affinity; low structural secondary interference. |
| **High GC** | GC% > 60% | Elevated risk of off-target activity and internal secondary hairpins. |
| **Low GC** | GC% < 40% | Weak target binding and reduced cleavage efficiency. |
| **Poly-T** | Contains `TTTT` | Premature transcription termination via RNA Pol III. |

---

## Installation & Usage

### Prerequisites
- Python 3.8 or higher. No external libraries required (uses standard library modules: `re`).

### Running the Tool
Clone this repository or download the script, then execute:

```bash
python crispr_scanner.py