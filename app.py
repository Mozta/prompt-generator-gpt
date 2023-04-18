import os
# from dotenv import load_dotenv
import openai
from flask import Flask, redirect, render_template, request, url_for

# load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))    
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt),
            temperature=0.6,
            max_tokens=500,
        )
        result = response.choices[0].text
        print(f"RESULT: {response.choices[0].text} \n")

        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(prompt):
    return """Act like a prompt engineering expert. Give me 3 examples of enginner prompts to generate content.

Prompt: How to increase customer satisfaction?
EngineerPrompt: Imagine you are the CEO of a company in [specific industry]. What measures would you implement to increase customer satisfaction and improve long-term profitability?
Prompt: Write a story where the character has to make decisions
EngineerPrompt: Write a short story in which a main character must make a difficult decision related to [specific theme]. What factors should they consider before making their decision?
Prompt: {}
EngineerPrompt:""".format(
        prompt.capitalize()
    )


if __name__ == '__main__':
    app.run(debug=True)
