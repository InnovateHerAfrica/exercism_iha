def cigar_party(cigars, is_weekend):
  if cigars in range(40, 61) or cigars >= 40 and is_weekend:
    return True
  else:
    return False
