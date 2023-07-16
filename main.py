from flask import Flask, render_template, request
import openai
import json
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import matplotlib

matplotlib.use('Agg')

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

    if len(response.choices) > 0:
      graph = response.choices[0].text.strip()
      graph = graph.replace(": ", ":\n")
      graph = graph.replace("- ", "-\n")
      graph = graph.split("\n")

    graph_data = convertGraphToTree(graph)

    # Generate the graph image
    plt.figure(figsize=(10, 6))
    nx.draw(graph_data, with_labels=True)

    # Convert the graph image to base64 format
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()

    return render_template('result.html',
                           graph_data=graph_data,
                           image_base64=image_base64)


def convertGraphToTree(graph):
  G = nx.DiGraph()
  for item in graph:
    if "->" in item:
      source, target = item.split("->")
      G.add_edge(source.strip(), target.strip())
  return G


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
