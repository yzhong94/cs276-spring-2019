class InvertedIndexWriter(InvertedIndex):
    """"""
    def __enter__(self):
        self.index_file = open(self.index_file_path, 'wb+')              
        return self

    def append(self, term, postings_list):
        """Appends the term and postings_list to end of the index file.
        
        This function does three things, 
        1. Encodes the postings_list using self.postings_encoding
        2. Stores metadata (postings_begin_position, 
                            number_of_postings_in_list,
                            length_of_postings_list_in_bytes)
        3. Appends the bytestream to the index file on disk

        Hint: You might find it helpful to read the Python I/O docs
        (https://docs.python.org/3/tutorial/inputoutput.html) for
        information about appending to the end of a file.
        
        Parameters
        ----------
        term:
            term or termID is the unique identifier for the term
        postings_list: List[Int]
            List of docIDs where the term appears
        """
        ### Begin your code
        file = open(self.index_file_path, 'ab+')
        self.terms.append(term)
        
        #step 1
        encoded_posting_list = self.postings_encoding.encode(postings_list)
        
        #step 2
        postings_begin_position = file.tell()
        number_of_postings_in_list = len(postings_list)
        length_of_postings_list_in_bytes =  len(encoded_posting_list)
                
        self.postings_dict[term] = (postings_begin_position,number_of_postings_in_list,length_of_postings_list_in_bytes)  
        
        #step3
        file.write(encoded_posting_list)

        ### End your code
