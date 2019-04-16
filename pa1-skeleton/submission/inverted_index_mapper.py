class InvertedIndexMapper(InvertedIndex):
    def __getitem__(self, key):
        return self._get_postings_list(key)
    
    def _get_postings_list(self, term):
        """Gets a postings list (of docIds) for `term`.
        
        This function should not iterate through the index file.
        I.e., it should only have to read the bytes from the index file
        corresponding to the postings list for the requested term.
        """
        ### Begin your code
        term_id = self.term_id_map.__getitem__(term)
        
        start_position_in_index_file, number_of_postings_in_list,length_in_bytes = self.postings_dict[term_ID]
        self.index_file.seek(start_position_in_index_file)
        posting_list = UncompressedPostings.decode(self.index_file.read(length_in_bytes))
        
        return posting_list
        ### End your code
