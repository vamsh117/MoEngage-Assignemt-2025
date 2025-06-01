def get_analysis_prompt(content):
    return f"""
You are an expert documentation reviewer.

Below is an article from MoEngage documentation. Analyze it based on the following criteria:

1. **Readability for a Marketer**: Is it easy for a non-technical marketer to understand? Provide reasoning.
2. **Structure and Flow**: Are headings, lists, and paragraphs structured well?
3. **Completeness of Information and Examples**: Are there enough details and relevant examples?
4. **Adherence to Style Guidelines**: Based on Microsoft Style Guide — clarity, tone, and action-oriented language.

Return your response in this JSON format:

{{
    "url": "<URL>",
    "readability": {{
        "assessment": "",
        "suggestions": []
    }},
    "structure": {{
        "assessment": "",
        "suggestions": []
    }},
    "completeness": {{
        "assessment": "",
        "suggestions": []
    }},
    "style": {{
        "assessment": "",
        "suggestions": []
    }}
}}

Here is the article content:
\"\"\"
{content}
\"\"\"
"""
