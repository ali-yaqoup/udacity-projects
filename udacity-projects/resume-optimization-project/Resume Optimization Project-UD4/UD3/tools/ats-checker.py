#!/usr/bin/env python3
"""
ATS Resume Checker Tool
Validates resume formatting and content for ATS compatibility
"""

import re
import json
from typing import Dict, List, Tuple
import argparse

class ATSChecker:
    def __init__(self):
        self.ats_friendly_fonts = {
            'arial', 'calibri', 'cambria', 'georgia', 'times new roman', 
            'verdana', 'helvetica', 'courier new', 'tahoma'
        }
        
        self.required_sections = {
            'contact', 'experience', 'education', 'skills'
        }
        
        self.forbidden_elements = [
            'tables', 'columns', 'text boxes', 'headers', 'footers',
            'images', 'graphics', 'logos', 'charts', 'colors'
        ]

    def check_formatting(self, resume_text: str) -> Dict:
        """Check ATS-friendly formatting"""
        checks = {
            'font_issues': [],
            'formatting_issues': [],
            'structure_issues': [],
            'content_issues': []
        }
        
        # Check for common formatting problems
        lines = resume_text.split('\n')
        
        # Check for consistent line endings and spacing
        for i, line in enumerate(lines):
            # Check for tab characters (ATS systems prefer spaces)
            if '\t' in line:
                checks['formatting_issues'].append(f"Line {i+1}: Contains tab characters")
            
            # Check for excessive whitespace
            if line.strip() == '' and i > 0 and lines[i-1].strip() == '':
                checks['formatting_issues'].append(f"Line {i+1}: Consecutive empty lines")
            
            # Check for unusual characters
            unusual_chars = re.findall(r'[^\w\s\-\.\,\;\:\!\?\@\#\$\%\&\*\(\)\[\]\{\}\/\\\|\+\=\~\`]', line)
            if unusual_chars:
                checks['formatting_issues'].append(f"Line {i+1}: Contains unusual characters: {set(unusual_chars)}")
        
        # Check section structure
        section_headers = self._identify_section_headers(resume_text)
        missing_sections = self.required_sections - set(section_headers.keys())
        
        for missing in missing_sections:
            checks['structure_issues'].append(f"Missing required section: {missing}")
        
        # Check for proper contact information
        contact_info = self._validate_contact_info(resume_text)
        if not contact_info['valid']:
            checks['content_issues'].extend(contact_info['issues'])
        
        return checks

    def _identify_section_headers(self, text: str) -> Dict[str, int]:
        """Identify section headers and their positions"""
        common_headers = {
            'contact': ['contact', 'contact information', 'name', 'personal'],
            'experience': ['experience', 'work experience', 'professional experience', 'employment', 'career'],
            'education': ['education', 'academic', 'university', 'college', 'degree'],
            'skills': ['skills', 'technical skills', 'competencies', 'expertise', 'abilities'],
            'summary': ['summary', 'professional summary', 'objective', 'profile'],
            'projects': ['projects', 'project experience', 'portfolio'],
            'certifications': ['certifications', 'certificates', 'credentials'],
            'awards': ['awards', 'honors', 'recognition']
        }
        
        section_headers = {}
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.strip().lower()
            
            for section, variations in common_headers.items():
                for variation in variations:
                    if variation in line_lower and len(line.strip()) < 50:  # Reasonable header length
                        if section not in section_headers:
                            section_headers[section] = i + 1
                        break
        
        return section_headers

    def _validate_contact_info(self, text: str) -> Dict:
        """Validate contact information completeness"""
        issues = []
        
        # Check for email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.search(email_pattern, text):
            issues.append("Missing email address")
        
        # Check for phone number
        phone_patterns = [
            r'\(\d{3}\)\s*\d{3}[-.\s]?\d{4}',  # (123) 456-7890
            r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',   # 123-456-7890
            r'\d{10}',                           # 1234567890
        ]
        
        has_phone = any(re.search(pattern, text) for pattern in phone_patterns)
        if not has_phone:
            issues.append("Missing phone number")
        
        # Check for LinkedIn
        if 'linkedin.com' not in text.lower():
            issues.append("Missing LinkedIn profile (recommended)")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues
        }

    def check_keyword_optimization(self, resume_text: str, job_description: str = None) -> Dict:
        """Check keyword optimization"""
        analysis = {
            'keyword_density': 0,
            'action_verbs': [],
            'quantified_achievements': 0,
            'missing_keywords': [],
            'recommendations': []
        }
        
        # Extract action verbs
        action_verbs = [
            'managed', 'led', 'developed', 'created', 'implemented', 'designed',
            'coordinated', 'achieved', 'improved', 'increased', 'reduced', 'optimized',
            'launched', 'built', 'maintained', 'supported', 'trained', 'mentored'
        ]
        
        found_verbs = []
        for verb in action_verbs:
            if re.search(r'\b' + verb + r'\b', resume_text, re.IGNORECASE):
                found_verbs.append(verb)
        
        analysis['action_verbs'] = found_verbs
        
        # Check for quantified achievements
        quantified_patterns = [
            r'\d+%',  # Percentages
            r'\$\d+',  # Dollar amounts
            r'\d+\s*(?:customers?|clients?|users?|employees?)',  # People metrics
            r'\d+\s*(?:projects?|products?|features?)',  # Project metrics
        ]
        
        total_quantified = sum(len(re.findall(pattern, resume_text, re.IGNORECASE)) for pattern in quantified_patterns)
        analysis['quantified_achievements'] = total_quantified
        
        # Generate recommendations
        if len(found_verbs) < 5:
            analysis['recommendations'].append("Add more action verbs to bullet points")
        
        if total_quantified < 3:
            analysis['recommendations'].append("Include more quantified achievements with specific metrics")
        
        # If job description provided, check keyword alignment
        if job_description:
            job_keywords = self._extract_keywords(job_description)
            resume_keywords = self._extract_keywords(resume_text)
            
            missing_keywords = job_keywords - resume_keywords
            analysis['missing_keywords'] = list(missing_keywords)[:10]  # Top 10 missing
            
            if len(missing_keywords) > 5:
                analysis['recommendations'].append(f"Consider adding these keywords: {', '.join(list(missing_keywords)[:5])}")
        
        return analysis

    def _extract_keywords(self, text: str) -> set:
        """Extract keywords from text"""
        # Remove common stop words
        stop_words = {
            'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
        }
        
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        keywords = {word for word in words if word not in stop_words}
        
        return keywords

    def check_readability(self, text: str) -> Dict:
        """Check readability for ATS optimization"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        if len(sentences) == 0 or len(words) == 0:
            return {
                'word_count': 0,
                'sentence_count': 0,
                'avg_sentence_length': 0,
                'reading_level': 'Unknown',
                'ats_friendly': False
            }
        
        avg_sentence_length = len(words) / len(sentences)
        
        # Simplified reading level assessment
        if avg_sentence_length <= 15:
            reading_level = '8th Grade'
            ats_friendly = True
        elif avg_sentence_length <= 20:
            reading_level = '10th Grade'
            ats_friendly = True
        elif avg_sentence_length <= 25:
            reading_level = '12th Grade'
            ats_friendly = True
        else:
            reading_level = 'College Level'
            ats_friendly = False
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length': round(avg_sentence_length, 1),
            'reading_level': reading_level,
            'ats_friendly': ats_friendly
        }

    def generate_ats_score(self, formatting_check: Dict, keyword_check: Dict, readability_check: Dict) -> Dict:
        """Generate overall ATS compatibility score"""
        score = 100
        issues = []
        
        # Formatting issues (-10 points each)
        formatting_issues = len(formatting_check['formatting_issues']) + len(formatting_check['structure_issues']) + len(formatting_check['content_issues'])
        score -= formatting_issues * 10
        if formatting_issues > 0:
            issues.append(f"Formatting issues detected: {formatting_issues}")
        
        # Keyword optimization (-5 points per missing recommendation)
        score -= len(keyword_check['recommendations']) * 5
        if keyword_check['recommendations']:
            issues.append(f"Keyword optimization needed: {len(keyword_check['recommendations'])} recommendations")
        
        # Readability (-15 points if not ATS-friendly)
        if not readability_check['ats_friendly']:
            score -= 15
            issues.append("Reading level not optimal for ATS")
        
        score = max(0, score)  # Ensure score doesn't go below 0
        
        # Determine grade
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        return {
            'score': score,
            'grade': grade,
            'issues': issues,
            'ats_ready': score >= 80
        }

def main():
    parser = argparse.ArgumentParser(description='Check resume ATS compatibility')
    parser.add_argument('--resume', type=str, required=True, help='Path to resume file')
    parser.add_argument('--job', type=str, help='Path to job description file (optional)')
    parser.add_argument('--output', type=str, help='Output JSON file for results')
    
    args = parser.parse_args()
    
    checker = ATSChecker()
    
    # Read resume file
    try:
        with open(args.resume, 'r', encoding='utf-8') as f:
            resume_text = f.read()
    except Exception as e:
        print(f"Error reading resume file: {e}")
        return
    
    job_text = None
    if args.job:
        try:
            with open(args.job, 'r', encoding='utf-8') as f:
                job_text = f.read()
        except Exception as e:
            print(f"Error reading job description file: {e}")
    
    # Perform checks
    formatting_check = checker.check_formatting(resume_text)
    keyword_check = checker.check_keyword_optimization(resume_text, job_text)
    readability_check = checker.check_readability(resume_text)
    ats_score = checker.generate_ats_score(formatting_check, keyword_check, readability_check)
    
    results = {
        'ats_score': ats_score,
        'formatting_check': formatting_check,
        'keyword_optimization': keyword_check,
        'readability_analysis': readability_check
    }
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"ATS analysis saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
