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
        
#         #expected output: (term_id,[doc_id1, doc_id2])
#         ls = []
#         posting = {}
        
#         #posting_list=[]
        
#         #sort the td_pairs
#         sorted_td_pairs = sorted(td_pairs, key=lambda tup:(tup[0], tup[1]))

#         for i in sorted_td_pairs:
#             termID = i[0]
#             docID = i[1]
            
#             try:
#                 ls = posting[termID]
#                 ls.append(docID)
#                 posting[termID] = list(set(ls))
                
#             except:
#                 posting[termID] = [docID]
            
        
            
#         #write to disk
#         for term in posting:
#             index.append(term,posting[term])
        
        posting_list = []
        sorted_td_pairs = sorted(td_pairs, key=lambda tup:(tup[0], tup[1]))
        
        prev_term = sorted_td_pairs[0][0]
        prev_doc = [sorted_td_pairs[0][1]]
        
        for i in range(1,len(sorted_td_pairs)):
            termID = sorted_td_pairs[i][0]
            docID = sorted_td_pairs[i][1]
            
            if termID == prev_term:
                prev_doc.append(docID)
            else:
                posting_list.append((prev_term,prev_doc))
                prev_doc = [docID]
                prev_term = termID
                
            if i == len(sorted_td_pairs) - 1:
                posting_list.append((prev_term,prev_doc))
        
        for i in posting_list:
            index.append(i[0],i[1])
        
        ### End your code
