#!/usr/bin/env python3
"""
Resume Keyword Analyzer Tool
Analyzes job descriptions and resumes for keyword optimization
"""

import re
import json
from collections import Counter
from typing import Dict, List, Set, Tuple
import argparse

class KeywordAnalyzer:
    def __init__(self):
        # Common action verbs for resumes
        self.action_verbs = {
            'managed', 'led', 'developed', 'created', 'implemented', 'designed',
            'coordinated', 'achieved', 'improved', 'increased', 'reduced', 'optimized',
            'launched', 'built', 'maintained', 'supported', 'trained', 'mentored',
            'collaborated', 'communicated', 'presented', 'analyzed', 'researched',
            'documented', 'tested', 'deployed', 'monitored', 'troubleshooted'
        }
        
        # Common technical skills categories
        self.tech_categories = {
            'programming_languages': ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin'],
            'web_technologies': ['html', 'css', 'react', 'angular', 'vue', 'nodejs', 'django', 'flask', 'spring'],
            'databases': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle', 'sqlite'],
            'cloud_platforms': ['aws', 'azure', 'gcp', 'heroku', 'digitalocean'],
            'tools_software': ['git', 'docker', 'kubernetes', 'jenkins', 'jira', 'slack', 'vscode', 'intellij']
        }
        
        # Common qualifications and certifications
        self.qualifications = {
            'bachelor', 'master', 'phd', 'degree', 'certification', 'pmp', 'cfa', 'cpa',
            'aws certified', 'google certified', 'microsoft certified', 'scrum master'
        }

    def extract_keywords(self, text: str) -> Dict[str, int]:
        """Extract and count keywords from text"""
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter out common stop words
        stop_words = {
            'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }
        
        filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
        word_count = Counter(filtered_words)
        
        return dict(word_count)

    def identify_job_requirements(self, job_description: str) -> Dict[str, List[str]]:
        """Identify specific job requirements from description"""
        requirements = {
            'skills': [],
            'qualifications': [],
            'experience': [],
            'responsibilities': []
        }
        
        # Extract skills (look for technical terms and action verbs)
        words = self.extract_keywords(job_description)
        for word, count in words.items():
            if word in self.action_verbs or any(word in skills for skills in self.tech_categories.values()):
                requirements['skills'].append(word)
        
        # Extract qualifications
        text_lower = job_description.lower()
        for qual in self.qualifications:
            if qual in text_lower:
                requirements['qualifications'].append(qual)
        
        # Extract experience requirements
        experience_patterns = [
            r'(\d+)\+?\s*years?',
            r'(\d+)\s*-\s*(\d+)\s*years?',
            r'entry\s*level',
            r'mid\s*level',
            r'senior\s*level',
            r'junior',
            r'lead',
            r'principal'
        ]
        
        for pattern in experience_patterns:
            matches = re.findall(pattern, text_lower)
            if matches:
                requirements['experience'].extend(matches)
        
        return requirements

    def analyze_resume_alignment(self, resume_text: str, job_description: str) -> Dict:
        """Analyze how well resume aligns with job description"""
        job_keywords = self.extract_keywords(job_description)
        resume_keywords = self.extract_keywords(resume_text)
        
        # Calculate keyword overlap
        job_words = set(job_keywords.keys())
        resume_words = set(resume_keywords.keys())
        
        overlap = job_words.intersection(resume_words)
        missing_keywords = job_words.difference(resume_words)
        
        # Calculate alignment percentage
        alignment_percentage = (len(overlap) / len(job_words)) * 100 if job_words else 0
        
        # Identify action verbs in resume
        resume_action_verbs = [word for word in resume_words if word in self.action_verbs]
        
        # Check for quantified achievements
        quantified_patterns = [
            r'\d+%',
            r'\$\d+',
            r'\d+\s*(?:customers?|clients?|users?|employees?|team members?)',
            r'\d+\s*(?:projects?|products?|features?)',
            r'\d+\s*(?:years?|months?|weeks?|days?)'
        ]
        
        quantified_count = sum(len(re.findall(pattern, resume_text.lower())) for pattern in quantified_patterns)
        
        return {
            'alignment_percentage': round(alignment_percentage, 2),
            'shared_keywords': list(overlap),
            'missing_keywords': list(missing_keywords),
            'resume_action_verbs': resume_action_verbs,
            'quantified_achievements': quantified_count,
            'job_keyword_count': len(job_words),
            'resume_keyword_count': len(resume_words)
        }

    def generate_optimization_suggestions(self, analysis_result: Dict) -> List[str]:
        """Generate suggestions for resume optimization"""
        suggestions = []
        
        # Alignment suggestions
        if analysis_result['alignment_percentage'] < 70:
            suggestions.append(f"Low alignment ({analysis_result['alignment_percentage']}%). Consider adding these missing keywords: {', '.join(analysis_result['missing_keywords'][:10])}")
        
        # Action verb suggestions
        if len(analysis_result['resume_action_verbs']) < 5:
            suggestions.append("Add more action verbs to your bullet points. Consider: Managed, Developed, Led, Created, Implemented")
        
        # Quantification suggestions
        if analysis_result['quantified_achievements'] < 3:
            suggestions.append("Add more quantified achievements. Include numbers, percentages, and specific metrics")
        
        # Keyword density suggestions
        if analysis_result['resume_keyword_count'] < 50:
            suggestions.append("Resume appears to have low keyword density. Consider expanding descriptions with relevant keywords")
        
        return suggestions

    def analyze_readability(self, text: str) -> Dict:
        """Basic readability analysis"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        syllables = sum(self._count_syllables(word) for word in words)
        
        # Flesch Reading Ease Score (simplified)
        if len(sentences) > 0 and len(words) > 0:
            avg_sentence_length = len(words) / len(sentences)
            avg_syllables_per_word = syllables / len(words)
            flesch_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        else:
            flesch_score = 0
        
        reading_level = self._flesch_to_grade_level(flesch_score)
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
            'flesch_score': round(flesch_score, 2),
            'reading_level': reading_level,
            'ats_friendly': 8 <= reading_level <= 12  # ATS prefers 8-12 grade level
        }

    def _count_syllables(self, word: str) -> int:
        """Simple syllable counting"""
        word = word.lower()
        vowels = "aeiouy"
        syllable_count = 0
        prev_char_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_char_was_vowel:
                syllable_count += 1
            prev_char_was_vowel = is_vowel
        
        # Adjust for silent 'e'
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1
        
        return max(1, syllable_count)

    def _flesch_to_grade_level(self, flesch_score: float) -> int:
        """Convert Flesch score to approximate grade level"""
        if flesch_score >= 90:
            return 5
        elif flesch_score >= 80:
            return 6
        elif flesch_score >= 70:
            return 7
        elif flesch_score >= 60:
            return 8
        elif flesch_score >= 50:
            return 9
        elif flesch_score >= 40:
            return 10
        elif flesch_score >= 30:
            return 11
        elif flesch_score >= 20:
            return 12
        else:
            return 13

def main():
    parser = argparse.ArgumentParser(description='Analyze resume and job description keywords')
    parser.add_argument('--resume', type=str, help='Path to resume file')
    parser.add_argument('--job', type=str, help='Path to job description file')
    parser.add_argument('--output', type=str, help='Output JSON file for results')
    
    args = parser.parse_args()
    
    analyzer = KeywordAnalyzer()
    
    if args.resume and args.job:
        # Read files
        with open(args.resume, 'r', encoding='utf-8') as f:
            resume_text = f.read()
        
        with open(args.job, 'r', encoding='utf-8') as f:
            job_text = f.read()
        
        # Perform analysis
        alignment = analyzer.analyze_resume_alignment(resume_text, job_text)
        job_requirements = analyzer.identify_job_requirements(job_text)
        resume_readability = analyzer.analyze_readability(resume_text)
        suggestions = analyzer.generate_optimization_suggestions(alignment)
        
        results = {
            'job_requirements': job_requirements,
            'alignment_analysis': alignment,
            'readability_analysis': resume_readability,
            'optimization_suggestions': suggestions
        }
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"Analysis saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))
    else:
        print("Please provide both --resume and --job arguments")

if __name__ == "__main__":
    main()
