from src.rag import rag_answer

text = """
Artificial Intelligence helps doctors detect diseases.

Machine Learning is a branch of AI.

Deep Learning is used in image recognition.

Neural networks are widely used in computer vision.
"""

question = "What is Deep Learning used for?"

answer = rag_answer(text, question)

print(answer)