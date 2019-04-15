
import heapq
class BSBIIndex(BSBIIndex):
    def merge(self, indices, merged_index):
        """Merges multiple inverted indices into a single index
        
        Parameters
        ----------
        indices: List[InvertedIndexIterator]
            A list of InvertedIndexIterator objects, each representing an
            iterable inverted index for a block
        merged_index: InvertedIndexWriter
            An instance of InvertedIndexWriter object into which each merged 
            postings list is written out one at a time
        """
        ### Begin your code
        '''
        ls = []
        posting = {}
        for merged_item in heapq.merge(*indices, key=lambda x: x[0]):
            termID = merged_item[0]
            docIDs = merged_item[1]
            try:
                ls = posting[termID]
                #ls = ls + docIDs
                [ls.append(i) for i in docIDs]
                posting[termID] = list(set(ls))
            except:
                posting[termID] = list(set(docIDs))
            

        print(posting)
        for term in posting:
            merged_index.append(term,posting[term])
        '''
        prev_termID = None
        prev_docID = []
        posting_list = []
        #sorted_td_pairs = sorted(td_pairs, key=lambda tup:(tup[0], tup[1]))
        for merged_item in heapq.merge(*indices, key=lambda x: x[0]):
            termID = merged_item[0]
            docID = merged_item[1]
            if prev_termID == None:
                [prev_docID.append(i) for i in docID]
                prev_termID = termID
            elif termID == prev_termID:
                [prev_docID.append(i) for i in docID]
            else:
                prev_docID = sorted(list(set(prev_docID)))
                posting_list.append((prev_termID, prev_docID))
                prev_termID = termID
                prev_docID = docID

        prev_docID = sorted(list(set(prev_docID)))
        posting_list.append((prev_termID, prev_docID))

        for i in posting_list:
            print(i[0], i[1])
            merged_index.append(i[0],i[1])        
            
            
        ### End your code
