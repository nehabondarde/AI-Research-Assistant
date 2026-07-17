from src.summarizer import generate_summary

text = """
Artificial Intelligence is transforming healthcare.

Machine learning helps doctors detect diseases earlier.

Deep learning is widely used in medical image analysis.

The paper concludes that AI can improve diagnosis accuracy.
"""

print(generate_summary(text))