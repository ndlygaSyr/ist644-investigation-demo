from flask import Flask
from flask import render_template, request, jsonify
from text_summarizer import FrequencySummarizer
from url_summarizer import URLSummarizer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')


@app.route("/summarize", methods=['POST'])
def summarize_url():
    url = request.form['summary_url']
    sent_count = int(request.form["sent_count"])
    usum = URLSummarizer()
    summary = usum.summarizeURL(url, sent_count)
    keywords = usum.get_keywords()
    return jsonify(
        message="Success",
        summary=summary,
        keywords=keywords,
        pageTitle=usum.get_page_title()
    )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000,debug=True)