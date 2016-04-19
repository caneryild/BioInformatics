def similarityOfProteins(protein1,protein2):
  lcs=largestCommonSubsequence(protein1,protein2)
        ' find the first of largest common subseqence in each of them
        'and compare them from the first index through last one 
        'and compare them from the first index of L.C.S. to the ends.
        'the reverse for 2 two steps are repeated from end to start and from end of lcs.'s to start.
        'Total of m*n*2 comparisions are made.
