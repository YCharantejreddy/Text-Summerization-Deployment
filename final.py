
# # # from flask import Flask, render_template, request
# # # import spacy
# # # from spacy.lang.en.stop_words import STOP_WORDS as ENGLISH_STOP_WORDS
# # # from spacy.lang.hi.stop_words import STOP_WORDS as HINDI_STOP_WORDS
# # # from spacy.lang.kn.stop_words import STOP_WORDS as KANNADA_STOP_WORDS
# # # from spacy.lang.ml.stop_words import STOP_WORDS as MALAYALAM_STOP_WORDS
# # # from spacy.lang.fr.stop_words import STOP_WORDS as FRENCH_STOP_WORDS
# # # from spacy.lang.de.stop_words import STOP_WORDS as GERMAN_STOP_WORDS
# # # from spacy.lang.zh.stop_words import STOP_WORDS as CHINESE_STOP_WORDS
# # # from spacy.lang.ko.stop_words import STOP_WORDS as KOREAN_STOP_WORDS
# # # from string import punctuation
# # # from heapq import nlargest
# # # from rouge import Rouge

# # # app = Flask(__name__, template_folder='templates')

# # # def summarizer(rawdocs, language="english"):
# # #     if language == "english":
# # #         stopwords = ENGLISH_STOP_WORDS
# # #         nlp = spacy.load("en_core_web_sm")
# # #     elif language == "hindi":
# # #         stopwords = HINDI_STOP_WORDS
# # #         nlp = spacy.load("xx_ent_wiki_sm")
# # #     elif language == "kannada":
# # #         stopwords = KANNADA_STOP_WORDS
# # #         nlp = spacy.load("xx_ent_wiki_sm")
# # #     elif language == "malayalam":
# # #         stopwords = MALAYALAM_STOP_WORDS
# # #         nlp = spacy.load("xx_ent_wiki_sm")
# # #     elif language == "french":
# # #         stopwords = FRENCH_STOP_WORDS
# # #         nlp = spacy.load("fr_core_news_sm")
# # #     elif language == "german":
# # #         stopwords = GERMAN_STOP_WORDS
# # #         nlp = spacy.load("de_core_news_sm")
# # #     elif language == "chinese":
# # #         stopwords = CHINESE_STOP_WORDS
# # #         nlp = spacy.load("zh_core_web_sm")
# # #     elif language == "korean":
# # #         stopwords = KOREAN_STOP_WORDS
# # #         nlp = spacy.load("ko_core_news_sm")
# # #     else:
# # #         raise ValueError("Unsupported language.")
    
# # #     nlp.add_pipe('sentencizer')
# # #     doc = nlp(rawdocs)
# # #     tokens = [token.text for token in doc]
# # #     word_freq={}
# # #     for word in doc:
# # #         if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
# # #             if word.text not in word_freq.keys():
# # #                 word_freq[word.text] = 1
# # #             else:
# # #                 word_freq[word.text] += 1
# # #     max_freq=max(word_freq.values())
# # #     for word in word_freq.keys():
# # #         word_freq[word]=word_freq[word]/max_freq
# # #     sent_tokens=[sent for sent in doc.sents]
# # #     sent_scores={}
# # #     for sent in sent_tokens:
# # #         for word in sent:
# # #             if word.text in word_freq.keys():
# # #                 if sent not in sent_scores.keys():
# # #                     sent_scores[sent]=word_freq[word.text]
# # #                 else:
# # #                     sent_scores[sent]+=word_freq[word.text]
# # #     select_len=int(len(sent_tokens)*0.3)
# # #     summary=nlargest(select_len,sent_scores,key=sent_scores.get)
# # #     final_summary=[word.text for word in summary]
# # #     summary=' '.join(final_summary)
# # #     return summary, doc, len(rawdocs.split(' ')),len(summary.split(' '))

# # # def calculate_rouge(summary, rawdocs):
# # #     rouge = Rouge()
# # #     scores = rouge.get_scores(summary, rawdocs)
# # #     return scores[0]['rouge-1']['f']

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # @app.route('/about')
# # # def about():
# # #     return render_template('about.html')

# # # @app.route('/testcases')
# # # def testcases():
# # #     return render_template('testcases.html')

# # # @app.route('/analyze', methods=['GET', 'POST'])
# # # def analyze():
# # #     if request.method == "POST":
# # #         rawtext = request.form['rawtext']
# # #         language = request.form['language']
        
# # #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# # #         if language in supported_languages:
# # #             try:
# # #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# # #                 rouge_score = calculate_rouge(summary, rawtext)
# # #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# # #             except ValueError as e:
# # #                 return render_template('error.html', message=str(e))
# # #         else:
# # #             return render_template('error.html', message="Unsupported language.")

# # # if __name__ == "__main__":
# # #     app.run(debug=True)
# # # from flask import Flask, render_template, request
# # # from transformers import pipeline
# # # from rouge import Rouge

# # # app = Flask(__name__, template_folder='templates')

# # # # Load the summarization pipeline
# # # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # def summarizer(rawdocs, language="english"):
# # #     # Perform summarization using the pipeline
# # #     summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
# # #     summary = summary_result[0]['summary_text']
    
# # #     # Calculate the number of words in original and summary
# # #     len_orig_txt = len(rawdocs.split(' '))
# # #     len_summary = len(summary.split(' '))
    
# # #     return summary, rawdocs, len_orig_txt, len_summary

# # # def calculate_rouge(summary, rawdocs):
# # #     rouge = Rouge()
# # #     scores = rouge.get_scores(summary, rawdocs)
# # #     return scores[0]['rouge-1']['f']

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # @app.route('/about')
# # # def about():
# # #     return render_template('about.html')

# # # @app.route('/testcases')
# # # def testcases():
# # #     return render_template('testcases.html')

# # # @app.route('/analyze', methods=['GET', 'POST'])
# # # def analyze():
# # #     if request.method == "POST":
# # #         rawtext = request.form['rawtext']
# # #         language = request.form['language']
        
# # #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# # #         if language in supported_languages:
# # #             try:
# # #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# # #                 rouge_score = calculate_rouge(summary, rawtext)
# # #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# # #             except ValueError as e:
# # #                 return render_template('error.html', message=str(e))
# # #         else:
# # #             return render_template('error.html', message="Unsupported language.")

# # # if __name__ == "__main__":
# # #     app.run(debug=True)












# # # from flask import Flask, render_template, request, redirect, url_for, flash
# # # from transformers import pipeline
# # # from rouge import Rouge
# # # import os
# # # from werkzeug.utils import secure_filename
# # # from flask_sqlalchemy import SQLAlchemy

# # # app = Flask(__name__, template_folder='templates')
# # # app.secret_key = 'your_secret_key'
# # # app.config['UPLOAD_FOLDER'] = 'uploads'
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///summaries.db'
# # # db = SQLAlchemy(app)

# # # # Database model for storing summaries
# # # class Summary(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     original_text = db.Column(db.Text, nullable=False)
# # #     summary = db.Column(db.Text, nullable=False)
# # #     rouge_score = db.Column(db.Float, nullable=False)

# # # # Initialize database
# # # with app.app_context():
# # #     db.create_all()

# # # # Load the summarization pipeline
# # # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # def summarizer(rawdocs):
# # #     summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
# # #     summary = summary_result[0]['summary_text']
# # #     len_orig_txt = len(rawdocs.split(' '))
# # #     len_summary = len(summary.split(' '))
# # #     return summary, rawdocs, len_orig_txt, len_summary

# # # def calculate_rouge(summary, rawdocs):
# # #     rouge = Rouge()
# # #     scores = rouge.get_scores(summary, rawdocs)
# # #     return scores[0]['rouge-1']['f']

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # @app.route('/about')
# # # def about():
# # #     return render_template('about.html')

# # # @app.route('/testcases')
# # # def testcases():
# # #     return render_template('testcases.html')

# # # @app.route('/upload', methods=['GET', 'POST'])
# # # def upload_file():
# # #     if request.method == 'POST':
# # #         if 'file' not in request.files:
# # #             flash('No file part')
# # #             return redirect(request.url)
# # #         file = request.files['file']
# # #         if file.filename == '':
# # #             flash('No selected file')
# # #             return redirect(request.url)
# # #         if file:
# # #             filename = secure_filename(file.filename)
# # #             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# # #             file.save(filepath)
# # #             with open(filepath, 'r', encoding='utf-8') as f:
# # #                 rawtext = f.read()
# # #             return redirect(url_for('analyze', rawtext=rawtext))
# # #     return render_template('upload.html')

# # # @app.route('/analyze', methods=['GET', 'POST'])
# # # def analyze():
# # #     if request.method == "POST":
# # #         rawtext = request.form['rawtext']
# # #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
# # #         rouge_score = calculate_rouge(summary, rawtext)
        
# # #         # Save to database
# # #         new_summary = Summary(original_text=original_txt, summary=summary, rouge_score=rouge_score)
# # #         db.session.add(new_summary)
# # #         db.session.commit()
        
# # #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# # #     elif request.method == "GET" and 'rawtext' in request.args:
# # #         rawtext = request.args.get('rawtext')
# # #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
# # #         rouge_score = calculate_rouge(summary, rawtext)
        
# # #         # Save to database
# # #         new_summary = Summary(original_text=original_txt, summary=summary, rouge_score=rouge_score)
# # #         db.session.add(new_summary)
# # #         db.session.commit()
        
# # #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# # #     return render_template('index.html')

# # # @app.route('/history')
# # # def history():
# # #     summaries = Summary.query.all()
# # #     return render_template('history.html', summaries=summaries)

# # # @app.route('/download/<int:id>')
# # # def download(id):
# # #     summary = Summary.query.get_or_404(id)
# # #     return render_template('download.html', summary=summary)

# # # if __name__ == "__main__":
# # #     if not os.path.exists(app.config['UPLOAD_FOLDER']):
# # #         os.makedirs(app.config['UPLOAD_FOLDER'])
# # #     app.run(debug=True)








# # import os
# # from flask import Flask, render_template, request, redirect, url_for, send_file
# # from transformers import pipeline
# # from rouge import Rouge
# # from werkzeug.utils import secure_filename
# # import logging

# # app = Flask(__name__, template_folder='templates')

# # # Set up logging
# # logging.basicConfig(level=logging.INFO)  # Adjust level as needed

# # # Load the summarization pipeline
# # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # Configure upload folder
# # UPLOAD_FOLDER = 'uploads'
# # if not os.path.exists(UPLOAD_FOLDER):
# #     os.makedirs(UPLOAD_FOLDER)
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # def summarizer(rawdocs, language="english"):
# #     try:
# #         # Perform summarization using the pipeline
# #         summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
# #         summary = summary_result[0]['summary_text']
        
# #         # Calculate the number of words in original and summary
# #         len_orig_txt = len(rawdocs.split(' '))
# #         len_summary = len(summary.split(' '))
        
# #         return summary, rawdocs, len_orig_txt, len_summary
# #     except ValueError as ve:
# #         logging.error(f"ValueError in summarizer: {str(ve)}")
# #         raise ve
# #     except Exception as e:
# #         logging.error(f"Error in summarizer: {str(e)}")
# #         raise ValueError("Error in summarizer")

# # def calculate_rouge(summary, rawdocs):
# #     rouge = Rouge()
# #     scores = rouge.get_scores(summary, rawdocs)
# #     return scores[0]['rouge-1']['f']

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# # @app.route('/testcases')
# # def testcases():
# #     return render_template('testcases.html')

# # @app.route('/analyze', methods=['POST'])
# # def analyze():
# #     if request.method == "POST":
# #         rawtext = request.form['rawtext']
# #         language = request.form['language']
        
# #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# #         if language in supported_languages:
# #             try:
# #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #                 rouge_score = calculate_rouge(summary, rawtext)
# #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #             except ValueError as e:
# #                 return render_template('error.html', message=str(e))
# #         else:
# #             return render_template('error.html', message="Unsupported language.")

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return redirect(request.url)
# #     file = request.files['file']
# #     if file.filename == '':
# #         return redirect(request.url)
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)
# #         return redirect(url_for('analyze_uploaded', filename=filename))

# # # @app.route('/analyze_uploaded/<filename>')
# # # def analyze_uploaded(filename):
# # #     try:
# # #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# # #         with open(filepath, 'r', encoding='utf-8') as f:
# # #             rawtext = f.read()
# # #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
# # #         rouge_score = calculate_rouge(summary, rawtext)
# # #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# # #     except ValueError as e:
# # #         return render_template('error.html', message=str(e))
# # #     except Exception as e:
# # #         logging.error(f"Error analyzing uploaded file: {str(e)}")
# # #         return render_template('error.html', message="Error analyzing uploaded file.")


# # @app.route('/analyze_uploaded/<filename>')
# # def analyze_uploaded(filename):
# #     try:
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         with open(filepath, 'r', encoding='utf-8') as f:
# #             rawtext = f.read()
# #         language = request.form['language']  # Get the language from the form
# #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #         rouge_score = calculate_rouge(summary, rawtext)
# #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #     except ValueError as e:
# #         return render_template('error.html', message=str(e))
# #     except Exception as e:
# #         logging.error(f"Error analyzing uploaded file: {str(e)}")
# #         return render_template('error.html', message="Error analyzing uploaded file.")
# # # @app.route('/download')
# # # def download():
# # #     history_path = 'summarization_history.txt'
# # #     return send_file(history_path, as_attachment=True)@app.route('/download')
# # def download():
# #     history_path = os.path.join(app.config['UPLOAD_FOLDER'], 'summarization_history.txt')
# #     if not os.path.exists(history_path):
# #         with open(history_path, 'w') as f:
# #             f.write("")  # Create an empty file
# #     return send_file(history_path, as_attachment=True)

# # if __name__ == "__main__":
# #     app.run(debug=True)
# # from flask import Flask, render_template, request, redirect, url_for, send_file
# # from transformers import pipeline
# # from rouge import Rouge
# # from werkzeug.utils import secure_filename
# # import logging
# # import os

# # app = Flask(__name__, template_folder='templates')

# # # Set up logging
# # logging.basicConfig(level=logging.INFO)  # Adjust level as needed

# # # Load the summarization pipeline
# # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # Configure upload folder
# # UPLOAD_FOLDER = 'uploads'
# # if not os.path.exists(UPLOAD_FOLDER):
# #     os.makedirs(UPLOAD_FOLDER)
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # def summarizer(rawdocs, language="english"):
# #     try:
# #         # Perform summarization using the pipeline
# #         summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
# #         summary = summary_result[0]['summary_text']
        
# #         # Calculate the number of words in original and summary
# #         len_orig_txt = len(rawdocs.split(' '))
# #         len_summary = len(summary.split(' '))
        
# #         return summary, rawdocs, len_orig_txt, len_summary
# #     except ValueError as ve:
# #         logging.error(f"ValueError in summarizer: {str(ve)}")
# #         raise ve
# #     except Exception as e:
# #         logging.error(f"Error in summarizer: {str(e)}")
# #         raise ValueError("Error in summarizer")

# # def calculate_rouge(summary, rawdocs):
# #     rouge = Rouge()
# #     scores = rouge.get_scores(summary, rawdocs)
# #     return scores[0]['rouge-1']['f']

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# # @app.route('/testcases')
# # def testcases():
# #     return render_template('testcases.html')

# # @app.route('/analyze', methods=['POST'])
# # def analyze():
# #     if request.method == "POST":
# #         rawtext = request.form['rawtext']
# #         language = request.form['language']
        
# #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# #         if language in supported_languages:
# #             try:
# #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #                 rouge_score = calculate_rouge(summary, rawtext)
# #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #             except ValueError as e:
# #                 return render_template('error.html', message=str(e))
# #         else:
# #             return render_template('error.html', message="Unsupported language.")

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return redirect(request.url)
# #     file = request.files['file']
# #     if file.filename == '':
# #         return redirect(request.url)
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)
# #         return redirect(url_for('analyze_uploaded', filename=filename))

# # @app.route('/analyze_uploaded/<filename>', methods=['GET', 'POST'])
# # def analyze_uploaded(filename):
# #     if request.method == 'POST':
# #         language = request.form['language']
# #     else:
# #         language = "english"  # Default language
# #     try:
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         with open(filepath, 'r', encoding='utf-8') as f:
# #             rawtext = f.read()
# #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #         rouge_score = calculate_rouge(summary, rawtext)
# #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #     except ValueError as e:
# #         return render_template('error.html', message=str(e))
# #     except Exception as e:
# #         logging.error(f"Error analyzing uploaded file: {str(e)}")
# #         return render_template('error.html', message="Error analyzing uploaded file.")

# # # @app.route('/download')
# # # def download():
# # #     history_path = os.path.join(app.config['UPLOAD_FOLDER'], 'ummarization_history.txt')
# # #     if not os.path.exists(history_path):
# # #         with open(history_path, 'w') as f:
# # #             f.write("")  # Create an empty file
# # #     return send_file(history_path, as_attachment=True)
# # @app.route('/download')
# # def download():
# #     history_path = os.path.join(app.root_path, 'summarization_history.txt')
# #     if os.path.exists(history_path):
# #         return send_file(history_path, as_attachment=True)
# #     else:
# #         return render_template('error.html', message="File not found.")

# # if __name__ == "__main__":
# #     app.run(debug=True)







# #Sumaary working 



# # from flask import Flask, render_template, request, redirect, url_for, send_file
# # from transformers import pipeline
# # from rouge import Rouge
# # from werkzeug.utils import secure_filename
# # import logging
# # import os

# # app = Flask(__name__, template_folder='templates')

# # # Set up logging
# # logging.basicConfig(level=logging.INFO)  # Adjust level as needed

# # # Load the summarization pipeline
# # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # Configure upload folder
# # UPLOAD_FOLDER = 'uploads'
# # if not os.path.exists(UPLOAD_FOLDER):
# #     os.makedirs(UPLOAD_FOLDER)
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # def summarizer(rawdocs, language="english"):
# #     try:
# #         # Perform summarization using the pipeline
# #         summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
        
# #         if not summary_result or len(summary_result) == 0 or 'summary_text' not in summary_result[0]:
# #             raise ValueError("Unable to generate summary")
        
# #         summary = summary_result[0]['summary_text']
        
# #         # Calculate the number of words in original and summary
# #         len_orig_txt = len(rawdocs.split(' '))
# #         len_summary = len(summary.split(' '))
        
# #         return summary, rawdocs, len_orig_txt, len_summary
# #     except ValueError as ve:
# #         logging.error(f"ValueError in summarizer: {str(ve)}")
# #         raise ve
# #     except Exception as e:
# #         logging.error(f"Error in summarizer: {str(e)}")
# #         raise ValueError("Error in summarizer")

# # def calculate_rouge(summary, rawdocs):
# #     rouge = Rouge()
# #     scores = rouge.get_scores(summary, rawdocs)
# #     return scores[0]['rouge-1']['f']

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# # @app.route('/testcases')
# # def testcases():
# #     return render_template('testcases.html')

# # @app.route('/analyze', methods=['POST'])
# # def analyze():
# #     if request.method == "POST":
# #         rawtext = request.form['rawtext']
# #         language = request.form['language']
        
# #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# #         if language in supported_languages:
# #             try:
# #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #                 rouge_score = calculate_rouge(summary, rawtext)
# #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #             except ValueError as e:
# #                 return render_template('error.html', message=str(e))
# #         else:
# #             return render_template('error.html', message="Unsupported language.")

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return redirect(request.url)
# #     file = request.files['file']
# #     if file.filename == '':
# #         return redirect(request.url)
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)
# #         return redirect(url_for('analyze_uploaded', filename=filename))

# # @app.route('/analyze_uploaded/<filename>', methods=['GET', 'POST'])
# # def analyze_uploaded(filename):
# #     if request.method == 'POST':
# #         language = request.form['language']
# #     else:
# #         language = "english"  # Default language
# #     try:
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         with open(filepath, 'r', encoding='utf-8') as f:
# #             rawtext = f.read()
# #         return render_template('analyze.html', rawtext=rawtext, filename=filename, language=language)
# #     except Exception as e:
# #         logging.error(f"Error analyzing uploaded file: {str(e)}")
# #         return render_template('error.html', message="Error analyzing uploaded file.")

# # @app.route('/summarize', methods=['POST'])
# # def summarize():
# #     rawtext = request.form['rawtext']
# #     language = request.form['language']
# #     filename = request.form['filename']
# #     try:
# #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #         rouge_score = calculate_rouge(summary, rawtext)
# #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #     except ValueError as e:
# #         return render_template('error.html', message=str(e))
# #     except Exception as e:
# #         logging.error(f"Error summarizing: {str(e)}")
# #         return render_template('error.html', message="Error summarizing.")

# # @app.route('/download')
# # def download():
# #     history_path = os.path.join(app.root_path, 'summarization_history.txt')
# #     if os.path.exists(history_path):
# #         return send_file(history_path, as_attachment=True)
# #     else:
# #         return render_template('error.html', message="File not found.")

# # if __name__ == "__main__":
# #     app.run(debug=True)





# # from flask import Flask, render_template, request, redirect, url_for, send_file
# # from transformers import pipeline
# # from rouge import Rouge
# # from werkzeug.utils import secure_filename
# # import logging
# # import os

# # app = Flask(__name__, template_folder='templates')

# # # Set up logging
# # logging.basicConfig(level=logging.INFO)  # Adjust level as needed

# # # Load the summarization pipeline
# # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # # Configure upload folder
# # UPLOAD_FOLDER = 'uploads'
# # if not os.path.exists(UPLOAD_FOLDER):
# #     os.makedirs(UPLOAD_FOLDER)
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # def summarizer(rawdocs, language="english"):
# #     try:
# #         # Perform summarization using the pipeline
# #         summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
        
# #         if not summary_result or len(summary_result) == 0 or 'summary_text' not in summary_result[0]:
# #             raise ValueError("Unable to generate summary")
        
# #         summary = summary_result[0]['summary_text']
        
# #         # Calculate the number of words in original and summary
# #         len_orig_txt = len(rawdocs.split(' '))
# #         len_summary = len(summary.split(' '))
        
# #         return summary, rawdocs, len_orig_txt, len_summary
# #     except ValueError as ve:
# #         logging.error(f"ValueError in summarizer: {str(ve)}")
# #         raise ve
# #     except Exception as e:
# #         logging.error(f"Error in summarizer: {str(e)}")
# #         raise ValueError("Error in summarizer")

# # def calculate_rouge(summary, rawdocs):
# #     rouge = Rouge()
# #     scores = rouge.get_scores(summary, rawdocs)
# #     return scores[0]['rouge-1']['f']

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# # @app.route('/testcases')
# # def testcases():
# #     return render_template('testcases.html')

# # @app.route('/analyze', methods=['POST'])
# # def analyze():
# #     if request.method == "POST":
# #         rawtext = request.form['rawtext']
# #         language = request.form['language']
        
# #         supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
# #         if language in supported_languages:
# #             try:
# #                 summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #                 rouge_score = calculate_rouge(summary, rawtext)
# #                 return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #             except ValueError as e:
# #                 return render_template('error.html', message=str(e))
# #         else:
# #             return render_template('error.html', message="Unsupported language.")

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return redirect(request.url)
# #     file = request.files['file']
# #     if file.filename == '':
# #         return redirect(request.url)
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)
# #         return redirect(url_for('analyze_uploaded', filename=filename))

# # @app.route('/analyze_uploaded/<filename>', methods=['GET', 'POST'])
# # def analyze_uploaded(filename):
# #     if request.method == 'POST':
# #         language = request.form['language']
# #     else:
# #         language = "english"  # Default language
# #     try:
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         with open(filepath, 'r', encoding='utf-8') as f:
# #             rawtext = f.read()
# #         return render_template('analyze.html', rawtext=rawtext, filename=filename, language=language)
# #     except Exception as e:
# #         logging.error(f"Error analyzing uploaded file: {str(e)}")
# #         return render_template('error.html', message="Error analyzing uploaded file.")

# # @app.route('/summarize', methods=['POST'])
# # def summarize():
# #     rawtext = request.form['rawtext']
# #     language = request.form['language']
# #     filename = request.form['filename']
# #     try:
# #         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
# #         rouge_score = calculate_rouge(summary, rawtext)
# #         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
# #     except ValueError as e:
# #         return render_template('error.html', message=str(e))
# #     except Exception as e:
# #         logging.error(f"Error summarizing: {str(e)}")
# #         return render_template('error.html', message="Error summarizing.")

# # @app.route('/download')
# # def download():
# #     history_path = os.path.join(app.root_path, 'ummarization_history.txt')
# #     if os.path.exists(history_path):
# #         return send_file(history_path, as_attachment=True)
# #     else:
# #         return render_template('error.html', message="File not found.")

# # if __name__ == "__main__":
# #     app.run(debug=True)




# from flask import Flask, request, redirect, url_for, render_template
# import logging
# import transformers

# app = Flask(__name__)
# app.config["DEBUG"] = True  # Enable debug mode

# # Load the summarization model
# model = transformers.T5ForConditionalGeneration.from_pretrained('t5-small')
# tokenizer = transformers.T5Tokenizer.from_pretrained('t5-small')

# def summarizer(rawdocs, language="english"):
#     try:
#         # Preprocess the input text
#         inputs = tokenizer.encode_plus(
#             rawdocs,
#             add_special_tokens=True,
#             max_length=512,
#             return_attention_mask=True,
#             return_tensors='pt'
#         )

#         # Generate the summary
#         summary_ids = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=150, min_length=30, do_sample=False)
#         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#         # Calculate the number of words in original and summary
#         len_orig_txt = len(rawdocs.split(' '))
#         len_summary = len(summary.split(' '))

#         return summary, rawdocs, len_orig_txt, len_summary
#     except ValueError as ve:
#         logging.error(f"ValueError in summarizer: {str(ve)}")
#         raise ve
#     except Exception as e:
#         logging.error(f"Error in summarizer: {str(e)}")
#         raise ValueError("Error in summarizer")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         rawtext = request.form['rawtext']
#         language = request.form['language']
#         summary, rawdocs, len_orig_txt, len_summary = summarizer(rawtext, language)
#         return redirect(url_for('analyze', summary=summary, rawdocs=rawdocs, len_orig_txt=len_orig_txt, len_summary=len_summary))
#     return render_template('index.html')

# @app.route('/analyze', methods=['GET'])
# def analyze():
#     summary = request.args.get('summary')
#     rawdocs = request.args.get('rawdocs')
#     len_orig_txt = request.args.get('len_orig_txt')
#     len_summary = request.args.get('len_summary')
#     return render_template('analyze.html', summary=summary, rawdocs=rawdocs, len_orig_txt=len_orig_txt, len_summary=len_summary)

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, send_file
from transformers import pipeline
from rouge import Rouge
from werkzeug.utils import secure_filename
import os
import logging

app = Flask(__name__, template_folder='templates')

# Set up logging
logging.basicConfig(level=logging.INFO)  # Adjust level as needed

# Load the summarization pipeline
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def summarizer(rawdocs, language="english"):
    try:
        # Perform summarization using the pipeline
        summary_result = summarizer_pipeline(rawdocs, max_length=150, min_length=30, do_sample=False)
        summary = summary_result[0]['summary_text']
        
        # Calculate the number of words in original and summary
        len_orig_txt = len(rawdocs.split())
        len_summary = len(summary.split())
        
        return summary, rawdocs, len_orig_txt, len_summary
    except ValueError as ve:
        logging.error(f"ValueError in summarizer: {str(ve)}")
        raise ve
    except Exception as e:
        logging.error(f"Error in summarizer: {str(e)}")
        raise ValueError("Error in summarizer")

def calculate_rouge(summary, rawdocs):
    rouge = Rouge()
    scores = rouge.get_scores(summary, rawdocs)
    return scores[0]['rouge-1']['f']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testcases')
def testcases():
    return render_template('testcases.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == "POST":
        rawtext = request.form.get('rawtext', '')
        language = request.form.get('language', '')

        if not rawtext:
            return render_template('error.html', message="Please provide text to analyze.")

        supported_languages = ["english", "hindi", "kannada", "malayalam", "french", "german", "chinese", "korean"]
        
        if language in supported_languages:
            try:
                summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
                rouge_score = calculate_rouge(summary, rawtext)
                return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
            except ValueError as e:
                return render_template('error.html', message=str(e))
        else:
            return render_template('error.html', message="Unsupported language.")
    else:
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('analyze_uploaded', filename=filename))

@app.route('/analyze_uploaded/<filename>', methods=['GET', 'POST'])
def analyze_uploaded(filename):
    if request.method == 'POST':
        language = request.form['language']  # Get the language from the form
    else:
        language = "english"  # Default language
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            rawtext = f.read()
        return render_template('analyze.html', rawtext=rawtext, filename=filename, language=language)
    except Exception as e:
        logging.error(f"Error analyzing uploaded file: {str(e)}")
        return render_template('error.html', message="Error analyzing uploaded file.")
@app.route('/summarize', methods=['POST'])
def summarize():
    rawtext = request.form.get('rawtext', '')
    language = request.form.get('language', 'english')  # Default language
    filename = request.form.get('filename', '')
    try:
        summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext, language)
        rouge_score = calculate_rouge(summary, rawtext)
        return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary, rouge_score=rouge_score)
    except ValueError as e:
        return render_template('error.html', message=str(e))
    except Exception as e:
        logging.error(f"Error summarizing: {str(e)}")
        return render_template('error.html', message="Error summarizing.")

@app.route('/download')
def download():
    history_path = os.path.join(app.root_path, 'summarization_history.txt')
    if os.path.exists(history_path):
        return send_file(history_path, as_attachment=True)
    else:
        return render_template('error.html', message="File not found.")

if __name__ == "__main__":
    app.run(debug=True)
