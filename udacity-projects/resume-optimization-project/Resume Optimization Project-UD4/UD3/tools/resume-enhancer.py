#!/usr/bin/env python3
"""
AI-Powered Resume Enhancement Tool
Enhances resume content while maintaining authenticity
"""

import re
import json
from typing import Dict, List, Tuple
import argparse

class ResumeEnhancer:
    def __init__(self):
        self.action_verb_synonyms = {
            'managed': ['oversaw', 'directed', 'supervised', 'administered', 'governed'],
            'led': ['guided', 'mentored', 'coached', 'inspired', 'motivated'],
            'developed': ['created', 'built', 'designed', 'constructed', 'established'],
            'implemented': ['executed', 'deployed', 'launched', 'rolled out', 'put in place'],
            'improved': ['enhanced', 'optimized', 'refined', 'upgraded', 'streamlined'],
            'increased': ['grew', 'expanded', 'boosted', 'elevated', 'raised'],
            'reduced': ['decreased', 'minimized', 'cut', 'lowered', 'trimmed'],
            'analyzed': ['examined', 'evaluated', 'assessed', 'reviewed', 'inspected'],
            'coordinated': ['organized', 'arranged', 'managed', 'facilitated', 'orchestrated']
        }
        
        self.impact_words = [
            'significantly', 'substantially', 'dramatically', 'considerably',
            'notably', 'remarkably', 'effectively', 'efficiently', 'successfully'
        ]
        
        self.quantifiable_metrics = [
            'percentage', 'dollar amount', 'time saved', 'efficiency gain',
            'customer satisfaction', 'team size', 'project count', 'revenue'
        ]

    def enhance_action_verbs(self, text: str) -> Dict:
        """Enhance action verbs with stronger alternatives"""
        enhancements = []
        enhanced_text = text
        
        for verb, synonyms in self.action_verb_synonyms.items():
            # Find instances of the verb at the beginning of bullet points
            pattern = r'^•\s*' + verb + r'\s'
            matches = re.findall(pattern, enhanced_text, re.MULTILINE)
            
            if matches:
                # Suggest stronger alternatives
                suggestions = [synonym.capitalize() for synonym in synonyms[:3]]
                enhancements.append({
                    'original_verb': verb.capitalize(),
                    'suggestions': suggestions,
                    'occurrences': len(matches)
                })
        
        return {
            'enhancements': enhancements,
            'original_text': text,
            'enhanced_text': enhanced_text
        }

    def add_quantifiable_metrics(self, text: str) -> Dict:
        """Suggest quantifiable metrics for achievements"""
        suggestions = []
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip().startswith('•'):
                # Check if line already has metrics
                has_metrics = bool(re.search(r'\d+[%$]', line))
                
                if not has_metrics:
                    # Suggest types of metrics to add
                    suggestions.append({
                        'line_number': i + 1,
                        'line_content': line.strip(),
                        'suggested_metrics': [
                            'Add percentage improvement (e.g., "increased by 25%")',
                            'Add dollar amount (e.g., "$50,000 in revenue")',
                            'Add time saved (e.g., "reduced processing time by 3 hours")',
                            'Add team size (e.g., "team of 10 people")',
                            'Add project count (e.g., "5 major projects")'
                        ]
                    })
        
        return {
            'metric_suggestions': suggestions,
            'lines_without_metrics': len(suggestions)
        }

    def improve_impact_language(self, text: str) -> Dict:
        """Add impact-focused language to achievements"""
        improvements = []
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip().startswith('•'):
                # Check for impact words
                has_impact = any(word in line.lower() for word in self.impact_words)
                
                if not has_impact:
                    improvements.append({
                        'line_number': i + 1,
                        'line_content': line.strip(),
                        'suggested_impact_words': self.impact_words[:5],
                        'enhanced_examples': [
                            line.replace('• ', '• Significantly '),
                            line.replace('• ', '• Successfully '),
                            line.replace('• ', '• Effectively ')
                        ]
                    })
        
        return {
            'impact_improvements': improvements,
            'lines_needing_impact': len(improvements)
        }

    def optimize_for_keywords(self, text: str, target_keywords: List[str]) -> Dict:
        """Optimize text for target keywords"""
        current_text_lower = text.lower()
        optimization_suggestions = []
        
        for keyword in target_keywords:
            keyword_lower = keyword.lower()
            
            if keyword_lower not in current_text_lower:
                # Find relevant sections to add keyword
                sections = ['experience', 'skills', 'summary', 'projects']
                
                for section in sections:
                    if section in current_text_lower:
                        optimization_suggestions.append({
                            'keyword': keyword,
                            'suggested_section': section,
                            'suggestion': f"Consider adding '{keyword}' to your {section} section"
                        })
                        break
        
        # Check keyword density
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        keyword_count = sum(1 for keyword in target_keywords if keyword.lower() in current_text_lower)
        keyword_density = (keyword_count / len(words)) * 100 if words else 0
        
        return {
            'optimization_suggestions': optimization_suggestions,
            'keyword_density': round(keyword_density, 2),
            'target_keywords': target_keywords,
            'current_keywords': [kw for kw in target_keywords if kw.lower() in current_text_lower]
        }

    def enhance_professional_summary(self, summary: str) -> Dict:
        """Enhance professional summary section"""
        enhancements = []
        
        # Check summary length
        if len(summary.split()) < 15:
            enhancements.append("Summary is too short. Consider expanding to 15-30 words.")
        elif len(summary.split()) > 50:
            enhancements.append("Summary is too long. Consider condensing to 15-30 words.")
        
        # Check for key elements
        elements_to_check = {
            'years of experience': r'\d+\+?\s*years?',
            'key skills': r'(expert|skilled|proficient|experienced)',
            'career goal': r'(seeking|looking for|interested in)',
            'achievement': r'(achieved|accomplished|successful)'
        }
        
        for element, pattern in elements_to_check.items():
            if not re.search(pattern, summary, re.IGNORECASE):
                enhancements.append(f"Consider adding {element} to your summary")
        
        # Suggest improvements
        suggested_improvements = []
        
        if not re.search(r'\d+', summary):
            suggested_improvements.append("Add years of experience")
        
        if not any(skill in summary.lower() for skill in ['expert', 'skilled', 'proficient']):
            suggested_improvements.append("Highlight key skills")
        
        return {
            'enhancements': enhancements,
            'suggested_improvements': suggested_improvements,
            'word_count': len(summary.split()),
            'character_count': len(summary)
        }

    def improve_readability(self, text: str) -> Dict:
        """Improve readability while maintaining professionalism"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        readability_issues = []
        
        for i, sentence in enumerate(sentences):
            # Check sentence length
            words = sentence.split()
            if len(words) > 25:
                readability_issues.append({
                    'sentence_number': i + 1,
                    'issue': 'Sentence too long',
                    'sentence': sentence,
                    'word_count': len(words),
                    'suggestion': 'Consider breaking this into shorter sentences'
                })
            elif len(words) < 5:
                readability_issues.append({
                    'sentence_number': i + 1,
                    'issue': 'Sentence too short',
                    'sentence': sentence,
                    'word_count': len(words),
                    'suggestion': 'Consider expanding this sentence'
                })
        
        # Check for passive voice
        passive_indicators = ['was', 'were', 'been', 'being', 'is', 'are', 'am']
        passive_sentences = []
        
        for i, sentence in enumerate(sentences):
            if any(indicator in sentence.lower() for indicator in passive_indicators):
                if 'by' in sentence.lower():  # Likely passive voice
                    passive_sentences.append({
                        'sentence_number': i + 1,
                        'sentence': sentence,
                        'suggestion': 'Consider using active voice'
                    })
        
        return {
            'readability_issues': readability_issues,
            'passive_voice_sentences': passive_sentences,
            'total_sentences': len(sentences),
            'avg_sentence_length': sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        }

    def generate_enhanced_resume(self, original_text: str, enhancements: Dict) -> str:
        """Generate enhanced version of resume"""
        enhanced_text = original_text
        
        # Apply action verb enhancements
        if 'action_verbs' in enhancements:
            for enhancement in enhancements['action_verbs']['enhancements']:
                original_verb = enhancement['original_verb'].lower()
                if enhancement['suggestions']:
                    new_verb = enhancement['suggestions'][0].lower()
                    enhanced_text = re.sub(
                        r'^•\s*' + original_verb + r'\s',
                        r'• ' + new_verb + ' ',
                        enhanced_text,
                        flags=re.MULTILINE
                    )
        
        return enhanced_text

    def create_enhancement_report(self, original_text: str, target_keywords: List[str] = None) -> Dict:
        """Create comprehensive enhancement report"""
        report = {
            'original_text': original_text,
            'enhancements': {},
            'overall_score': 0,
            'recommendations': []
        }
        
        # Analyze action verbs
        action_verb_analysis = self.enhance_action_verbs(original_text)
        report['enhancements']['action_verbs'] = action_verb_analysis
        
        # Analyze quantifiable metrics
        metrics_analysis = self.add_quantifiable_metrics(original_text)
        report['enhancements']['metrics'] = metrics_analysis
        
        # Analyze impact language
        impact_analysis = self.improve_impact_language(original_text)
        report['enhancements']['impact'] = impact_analysis
        
        # Analyze readability
        readability_analysis = self.improve_readability(original_text)
        report['enhancements']['readability'] = readability_analysis
        
        # Keyword optimization (if keywords provided)
        if target_keywords:
            keyword_analysis = self.optimize_for_keywords(original_text, target_keywords)
            report['enhancements']['keywords'] = keyword_analysis
        
        # Calculate overall enhancement score
        score = 100
        score -= len(action_verb_analysis['enhancements']) * 5
        score -= metrics_analysis['lines_without_metrics'] * 10
        score -= impact_analysis['lines_needing_impact'] * 5
        score -= len(readability_analysis['readability_issues']) * 3
        
        report['overall_score'] = max(0, score)
        
        # Generate recommendations
        if metrics_analysis['lines_without_metrics'] > 0:
            report['recommendations'].append("Add quantifiable metrics to demonstrate impact")
        
        if impact_analysis['lines_needing_impact'] > 0:
            report['recommendations'].append("Use stronger impact language to highlight achievements")
        
        if len(action_verb_analysis['enhancements']) > 0:
            report['recommendations'].append("Enhance action verbs for stronger impact")
        
        return report

def main():
    parser = argparse.ArgumentParser(description='Enhance resume with AI-powered suggestions')
    parser.add_argument('--resume', type=str, required=True, help='Path to resume file')
    parser.add_argument('--keywords', type=str, nargs='+', help='Target keywords for optimization')
    parser.add_argument('--output', type=str, help='Output JSON file for enhancement report')
    parser.add_argument('--enhanced', type=str, help='Output file for enhanced resume text')
    
    args = parser.parse_args()
    
    enhancer = ResumeEnhancer()
    
    # Read resume file
    try:
        with open(args.resume, 'r', encoding='utf-8') as f:
            resume_text = f.read()
    except Exception as e:
        print(f"Error reading resume file: {e}")
        return
    
    # Generate enhancement report
    report = enhancer.create_enhancement_report(resume_text, args.keywords)
    
    # Save enhancement report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"Enhancement report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2))
    
    # Save enhanced resume
    if args.enhanced:
        enhanced_text = enhancer.generate_enhanced_resume(resume_text, report['enhancements'])
        with open(args.enhanced, 'w', encoding='utf-8') as f:
            f.write(enhanced_text)
        print(f"Enhanced resume saved to {args.enhanced}")

if __name__ == "__main__":
    main()
