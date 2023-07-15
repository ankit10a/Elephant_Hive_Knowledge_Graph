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
      prompt=f"Generate a knowledge graph for {url}.",
      max_tokens=200,
      temperature=0.5,
      n=1,
      stop=None,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    # Check if response.choices list is not empty before accessing elements
    if len(response.choices) > 0:
      graph = response.choices[0].text.strip()
      graph = graph.replace(": ", ":\n")
      graph = graph.replace("- ", "-\n")
      graph = graph.split("\n")
      # Create table rows
      table_rows = [{'element': item} for item in graph]

      return render_template(
        'result.html', rows=table_rows)  # Render the result.html template

  return "No graph generated."


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
