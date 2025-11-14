# arxiv_scraper.py - Scraper để lấy papers từ arXiv
# MSSV: 23127240

import os
import time
import json
import logging
import arxiv
import requests
from typing import Dict, List, Optional, Tuple
from datetime import datetime

from utils import (
    format_arxiv_id, format_folder_name, extract_tar_gz,
    process_tex_files, clean_version_folder, ensure_dir, clean_temp_files
)
from config import ARXIV_API_DELAY, MAX_RETRIES, RETRY_DELAY

logger = logging.getLogger(__name__)

class ArxivScraper:
    # Class để scrape papers từ arXiv API
    
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.client = arxiv.Client()
        # Stats để track progress
        self.stats = {
            'papers_attempted': 0,
            'papers_successful': 0,
            'papers_failed': 0,
            'versions_downloaded': 0,
            'total_download_time': 0.0,
            'total_processing_time': 0.0
        }
    
    def get_paper_metadata(self, arxiv_id: str) -> Optional[Dict]:
        # Lấy metadata của 1 paper (title, authors, abstract, etc.)
        
        Returns:
            Metadata dictionary or None if failed
        Download source files for a specific version
        
        Args:
            arxiv_id: arXiv ID without version
            version: Version string (e.g., "v1")
            output_dir: Directory to save source
        
        Returns:
            Tuple of (success, tar_path, updated_date)
        Scrape a single paper with all versions
        
        Args:
            arxiv_id: arXiv ID (e.g., "2208.11941")
            paper_dir: Directory for this paper's data
        
        Returns:
            True if successful, False otherwise