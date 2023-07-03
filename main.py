from flask import Flask, render_template, request
import openai

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    url = request.form['url']
    openai.api_key = request.form['api_key']
    response = openai.Completion.create(
      engine='text-davinci-003',
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
