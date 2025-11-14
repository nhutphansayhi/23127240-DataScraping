        Get references for a paper from Semantic Scholar
        
        Args:
            arxiv_id: arXiv ID (e.g., "2208.11941")
        
        Returns:
            List of reference dictionaries or None if failed
        Extract references that have arXiv IDs
        
        Args:
            references: List of reference dictionaries from Semantic Scholar
        
        Returns:
            Dictionary mapping arXiv IDs to metadata
        Scrape references for a paper and save to file
        
        Args:
            arxiv_id: arXiv ID (e.g., "2208.11941")
            output_path: Path to save references.json
        
        Returns:
            True if successful, False otherwise