from flask import Flask, render_template, request
import openai

openai.api_key = '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'
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def process_url():
  url = request.form['url']

  response = openai.Completion.create(
    engine='davinci',
    prompt=f"Generate knowledge graph for {url}.",
    max_tokens=200,
    temperature=0.5,
    n=1,
    stop=None,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

  # Extract the graph from the API response
  graph = response.choices[0].text.strip()

  # Return the graph to be displayed in the graph container
  return graph


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
