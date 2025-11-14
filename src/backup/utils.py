    Format arXiv ID from year-month and paper ID
    
    Args:
        year_month: Year-month string (e.g., "2208")
        paper_id: Paper ID number
    
    Returns:
        Formatted arXiv ID (e.g., "2208.11941")
    Convert arXiv ID to folder name format
    
    Args:
        arxiv_id: arXiv ID (e.g., "2208.11941")
    
    Returns:
        Folder name (e.g., "2208-11941")
    Extract .tar.gz file or handle gzip-compressed LaTeX source
    
    Args:
        tar_path: Path to .tar.gz file
        extract_dir: Directory to extract to
    
    Returns:
        True if successful, False otherwise
    Remove figure environments and includegraphics commands from TeX content
    
    Args:
        tex_content: Original TeX file content
    
    Returns:
        TeX content with figures removed
    Remove common image file types from directory
    
    Args:
        directory: Directory to clean
    
    Returns:
        Number of files removed
    Find the main .tex file (contains \\documentclass)
    
    Args:
        tex_dir: Directory containing .tex files
    
    Returns:
        Path to main .tex file, or None if not found
    Find the .bib file (bibliography)
    
    Args:
        tex_dir: Directory containing .bib files
    
    Returns:
        Path to .bib file, or None if not found
    Clean version folder to keep ONLY:
    - 1 main .tex file (renamed to paper.tex)
    - 1 .bib file (renamed to references.bib)
    Remove ALL other files and subfolders
    
    Args:
        version_dir: Version directory path
    
    Returns:
        Dictionary with statistics
    Process all .tex files in directory to remove figures
    
    Args:
        tex_dir: Directory containing .tex files
    
    Returns:
        Dictionary with processing statistics
    Calculate total size of directory in bytes
    
    Args:
        directory: Directory path
    
    Returns:
        Total size in bytes
    Remove temporary files and directories
    
    Args:
        temp_dir: Temporary directory to clean
    Ensure directory exists, create if it doesn't
    
    Args:
        directory: Directory path