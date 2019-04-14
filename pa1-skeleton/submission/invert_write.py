class BSBIIndex(BSBIIndex):
    def invert_write(self, td_pairs, index):
        """Inverts td_pairs into postings_lists and writes them to the given index
        
        Parameters
        ----------
        td_pairs: List[Tuple[Int, Int]]
            List of termID-docID pairs
        index: InvertedIndexWriter
            Inverted index on disk corresponding to the block       
        """
        
        ### Begin your code
        #requirements: The block is then inverted and written to disk. Inversion involves two steps. 
        #First, we sort the termID-docID pairs. 
        #Next, we collect all termID-docID pairs with the same termID into a postings list, where a posting is simply a docID. 
        #The result, an inverted index for the block we have just read, is then written to disk.
        
        #expected output: (term_id,[doc_id1, doc_id2])
        ls = []
        posting = {}
        
        #posting_list=[]
        
        #sort the td_pairs
        sorted_td_pairs = sorted(td_pairs, key=lambda tup:(tup[0], tup[1]))

        for i in sorted_td_pairs:
            termID = i[0]
            docID = i[1]
            
            try:
                ls = posting[termID]
                ls.append(docID)
                posting[termID] = ls
            except:
                posting[termID] = [docID]
            
            
            
        #write to disk
        for term in posting:
            index.append(term,posting[term])
        
        ### End your code
