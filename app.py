from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os
# Initialize Flask with the current directory as the templates folder.
app = Flask(__name__, template_folder='.', static_folder='.')

# Initialize the Gemini client with your API key.
client = genai.Client(api_key=os.environ['apikey'])

# List of YouTube video ideas related to AI/ML.
YOUTUBE_TOPICS = [
    "Introduction to Artificial Intelligence",
    "Deep Learning Basics",
    "Machine Learning in Healthcare",
    "Understanding Neural Networks",
    "Natural Language Processing Explained",
    "AI Ethics and Bias",
    "Reinforcement Learning Overview",
    "Generative AI Techniques",
    "Computer Vision in Real World",
    "AI in Robotics",
    "Machine Learning for Finance",
    "Data Science Pipelines",
    "The Future of AI",
    "AI and Automation",
    "Practical Machine Learning Projects"
]

def generate_script(topic):
    # Build a prompt that instructs Gemini to generate a detailed YouTube video script.
    prompt = (
        f"Generate a detailed YouTube video script about the topic: '{topic}'. "
        "Include an engaging introduction, a comprehensive explanation of the main points, "
        "and a concise conclusion. Make sure the content is informative and accessible for viewers interested in AI/ML. and strictly only output the script no extra uncessary text"
    )
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt],
            config=types.GenerateContentConfig(
                max_output_tokens=800,
                temperature=0.1
            )
        )
        return response.text
    except Exception as e:
        return f"Error generating script: {str(e)}"

@app.route('/')
def index():
    # Render the index.html file (located in the root).
    return render_template('index.html', topics=YOUTUBE_TOPICS)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data.get('topic')
    if not topic:
        return jsonify({'error': 'No topic provided'}), 400

    script = generate_script(topic)
    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(debug=True)