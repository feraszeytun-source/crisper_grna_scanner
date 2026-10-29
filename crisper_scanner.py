import re

def calculate_gc(sequence):
    """Calculate GC percentage for a given nucleotide sequence."""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return round(((g_count + c_count) / len(sequence)) * 100, 2) if len(sequence) > 0 else 0

def find_crispr_targets(dna_sequence):
    """
    Scans a DNA sequence for SpCas9 PAM sites (NGG)
    and evaluates upstream 20-nt guide RNAs (gRNAs) using standard biological filters.
    """
    dna_sequence = dna_sequence.upper().strip()
    target_sites = []
    
    # Regular expression for SpCas9 PAM: any nucleotide followed by GG (?=[ATGC]GG)
    pam_pattern = re.compile(r'(?=([ATGC]GG))')
    
    for match in pam_pattern.finditer(dna_sequence):
        pam_start = match.start()
        pam_seq = dna_sequence[pam_start : pam_start + 3]
        
        # Ensure there are at least 20 nucleotides upstream for the gRNA
        if pam_start >= 20:
            grna_seq = dna_sequence[pam_start - 20 : pam_start]
            gc_content = calculate_gc(grna_seq)
            
            # Biological quality filtering
            has_poly_t = "TTTT" in grna_seq
            
            if has_poly_t:
                is_recommended = "No"
                note = "Poly-T (Early termination)"
            elif gc_content < 40:
                is_recommended = "No"
                note = "Low GC (<40%)"
            elif gc_content > 60:
                is_recommended = "No"
                note = "High GC (>60%)"
            else:
                is_recommended = "Yes"
                note = "Optimal"
            
            target_sites.append({
                "Position": pam_start,
                "gRNA (20nt)": grna_seq,
                "PAM": pam_seq,
                "GC%": gc_content,
                "Recommended": is_recommended,
                "Note": note
            })
            
    return target_sites

# Interactive input
sample_dna = input("Enter DNA sequence to scan for CRISPR targets: ")
results = find_crispr_targets(sample_dna)

# Display tabular output
print("\n" + "="*95)
print(f"{'Pos':<6} | {'gRNA Sequence (20-nt)':<25} | {'PAM':<5} | {'GC%':<6} | {'Status':<12} | {'Note'}")
print("="*95)

if not results:
    print("No valid SpCas9 target sites (20nt + NGG) found in this sequence.")
else:
    for target in results:
        print(f"{target['Position']:<6} | {target['gRNA (20nt)']:<25} | {target['PAM']:<5} | {target['GC%']:<6} | {target['Recommended']:<12} | {target['Note']}")

print("="*95)
print(f"Total potential targets evaluated: {len(results)}\n")