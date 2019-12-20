<template>
  <!-- eslint-disable max-len -->
  <div class="full-page">
    <div :class="{'animated fadeIn': lazyLoad}">
      <section v-scroll-reveal.reset class="container-box">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div class="container columns text-left mx-auto pt-5">
          <div class="content column content-box">
            <h1 class="title is-size-1 is-size-2-mobile">Creating abstractive text
              summarization using deep learning</h1>
            <hr />
            <div class="columns is-mobile is-vcentered">
              <div class="column">
                <p
                  class="is-size-4 is-size-5-mobile
                  has-text-weight-semibold is-family-monospace avatar-text"
                >Thomas, Samuel och Per</p>
                <p
                  class="is-size-6 is-size-7-mobile
                  has-text-weight-semibold is-family-monospace avatar-text"
                >9 December, 2019</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section
        v-scroll-reveal.reset
        :style="{ backgroundImage:
        'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.2)), url(' + contentImageUrl + ')' }"
        class="hero is-info is-fullheight bg-image"
      />

      <section class="container-box container columns text-left mx-auto pt-5">
        <hr />
        <div class="container columns is-fluid">
          <div class="content column is-three-fifths is-offset-one-fifth content-box content-text">
            <h1>Introduction</h1>
            <p>Often when reading a report, you have to give a summary of the results which is common in and after college. However, this is a very time consuming task as you often have to read the whole article to understand the results. Until now, we can rely on the power of Natural Language Processing methods to summarize text for us.</p>
<p>There are two types of approaches which can be used for text summarization.</p>
<p>The first type is called Extractive Summarization. This approach identifies the most important sentences or phrases from the original text and extract only those from text&nbsp;as shown on the figure below. [1]</p>
<p><img title="" src="/assets/images/image26.png" alt="" /></p>
<p>However, our approach will be the second type, called Abstractive Summarization. Unlike Extractive summarization, we generate new sentences from the original text. [1]</p>
<p><img title="" src="assets/images/image14.png" alt="" /></p>
<p>The following is a walkthrough of how to use deep learning to create abstractive text summarization powered through python and vue. Pre-study was done using these tutorials:</p>
<ul>
<li><a href="https://www.google.com/url?q=https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/&amp;sa=D&amp;ust=1576877610190000">Comprehensive Guide to Text Summarization using Deep Learning in Python</a></li>
<li><a href="https://www.google.com/url?q=https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/&amp;sa=D&amp;ust=1576877610191000">Developing a Single Page App with Flask and Vue.js</a></li>
</ul>
<p>We will mainly focus on the deep learning part and briefly explain how the client was built. Lastly we will try to answer our question in research:</p>
<p>How can we generate abstract summaries of reviews of different genres e.g. food and books using deep learning?</p>
<p><img title="" src="assets/images/image3.png" alt="" /></p>
<h2>What is Flask?</h2>
<p>As mentioned in <a href="https://www.google.com/url?q=https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/&amp;sa=D&amp;ust=1576877610192000">Developing a Single Page App with Flask and Vue.js</a>, Flask is a simple microweb framework for Python, meaning that it does not require particular tools or libraries. It&rsquo;s perfect for building RESTful APIs which can easily be used as a backend server for our frontend client.</p>
<h2>What is Vue?</h2>
<p>Vue is an open source JavaScript framework used for building UI (User Interface) and SPA (Single-page applications). Compared to React and Angular, it&rsquo;s much easier for beginners to create modern frontend applications.</p>
<p>Vue supports multiple libraries. For this project a well known open source frontend library, called Bootstrap will be used.</p>
<h2>Sequence-to-Sequence (Seq2Seq) Modeling</h2>
<p>...</p>
<h2>Training phase</h2>
<p>...</p>
<p>Encoder</p>
<p>&hellip;</p>
<p>Decoder</p>
<p>&hellip;</p>
<h2>Attention Machine</h2>
<p>...</p>
<p>Implementation</p>
<p>All credits for the implementation of the presented theory goes to the original article found here: <a href="https://www.google.com/url?q=https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/&amp;sa=D&amp;ust=1576877610194000">https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/</a></p>
<h2>Setting up a Client/Server and a simple RESTful API</h2>
<p>Using the earlier mentioned tools we can start by creating a simple website that takes in a form input that the user pastes in. This string is then sent to the server-side for pre-processing and summarization.</p>
<p>The first thing we need to do is create a Vue project. You can follow the steps specified on the Vue CLI documentation website:</p>
<p><a href="https://www.google.com/url?q=https://cli.vuejs.org/guide/creating-a-project.html&amp;sa=D&amp;ust=1576877610195000">https://cli.vuejs.org/guide/creating-a-project.html</a></p>
<p>This gives us a very basic website with some starting code. We can clean out most of this and instead customize it to our needs.</p>
<p><img title="" src="assets/images/image17.png" alt="" /></p>
<p>Create several folders under /src to structurize our project, such as:</p>
<p>--/src/assets</p>
<p>--/src/components</p>
<p>--/src/views</p>
<p>--/src/router</p>
<p>Create a new .vue file named &ldquo;Home.vue&rdquo;. This will be our main view component.</p>
<p>&lt;template&gt;</p>
<p>&lt;divclass="container"&gt;</p>
<p>&lt;divclass="column bg-primary half-box"&gt;</p>
<p>&lt;b-imgsrc="https://www.shareicon.net/data/512x512/2016/10/22/846922_book_512x512.png"</p>
<p>class="logo m-3"roundedfluidalt="Responsive image"&gt;&lt;/b-img&gt;</p>
<p>&lt;b-jumbotron</p>
<p>class="p-0 text-white"</p>
<p>header="GastroLiter"</p>
<p>lead="A mini project for the course TNM108 at LiU"</p>
<p>bg-variant=transparent&gt;</p>
<p>&lt;/b-jumbotron&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;/template&gt;</p>
<p>&lt;script&gt;</p>
<p>importInputfrom'../components/Input.vue';</p>
<p>importOutputfrom'../components/Output.vue';</p>
<p>exportdefault&nbsp;{</p>
<p>name: 'Home',</p>
<p>components: {</p>
<p>Input,</p>
<p>Output,</p>
<p>},</p>
<p>data() {</p>
<p>return&nbsp;{</p>
<p>inputStatus: false,</p>
<p>data_type: '',</p>
<p>};</p>
<p>},</p>
<p>methods: {</p>
<p>inputData(status) {</p>
<p>this.inputStatus&nbsp;= status;</p>
<p>},</p>
<p>dataUpdate(type) {</p>
<p>this.data_type&nbsp;= type;</p>
<p>},</p>
<p>},</p>
<p>};</p>
<p>&lt;/script&gt;</p>
<p>&lt;style&gt;</p>
<p>.container&nbsp;{</p>
<p>height: 100vh;</p>
<p>margin: 0;</p>
<p>position: relative;</p>
<p>}</p>
<p>textarea&nbsp;{</p>
<p>resize:none;</p>
<p>}</p>
<p>.half-box{</p>
<p>height: 50%;</p>
<p>width: 100vw;</p>
<p>padding: 0;</p>
<p>}</p>
<p>.half-box-header{</p>
<p>height: 50%;</p>
<p>max-width: 20rem;</p>
<p>padding: 10;</p>
<p>}</p>
<p>.card&nbsp;{</p>
<p>position: absolute;</p>
<p>left: calc(50vw&nbsp;- 360px);</p>
<p>top: calc(50vh&nbsp;- 80px);</p>
<p>z-index: 1;</p>
<p>}</p>
<p>.logo&nbsp;{</p>
<p>height: 100px;</p>
<p>}</p>
<p>&lt;/style&gt;</p>
<p>What we have got here is a very basic component which displays a basic header on the top.</p>
<p><img title="" src="assets/images/image13.png" alt="" /></p>
<p>This will be our starting point. Now let&rsquo;s create another component and put it in --/src/components/Input.vue</p>
<p>This will handle all the text that the user inputs and send it to the server. It will consist of a</p>
<p>a textarea, two radio buttons and a submit button.</p>
<p><img title="" src="assets/images/image9.png" alt="" /></p>
<p>Here is the code:</p>
<p>&lt;template&gt;</p>
<p>&lt;divclass="form-group shadow-textarea"&gt;</p>
<p>&lt;formclass="input md-form mb-2 pink-textarea active-pink-textarea"</p>
<p>method="post"&nbsp;@submit.prevent="submit" &gt;</p>
<p>&lt;labelfor="exampleFormControlTextarea6"</p>
<p>class="text-danger animated shake delay-2s"&gt;{{ error&nbsp;}}&lt;/label&gt;</p>
<p>&lt;textareaclass="form-control z-depth-1"id="exampleFormControlTextarea6"</p>
<p>rows="3"placeholder="Paste your review here..."</p>
<p>name="name"value="value"v-model="data"&gt;&lt;/textarea&gt;</p>
<p>&lt;divclass="mt-3"&gt;</p>
<p>&lt;divclass="form-check form-check-inline"&gt;</p>
<p>&lt;inputclass="form-check-input"type="radio"</p>
<p>name="exampleRadios"id="book"v-model="data_type"</p>
<p>v-bind:value="'book'" v-on:change="data_type_set" checked&gt;</p>
<p>&lt;labelclass="form-check-label"for="book"&gt;</p>
<p>Book</p>
<p>&lt;/label&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;divclass="form-check form-check-inline"&gt;</p>
<p>&lt;inputclass="form-check-input"type="radio"</p>
<p>name="exampleRadios"id="food"v-model="data_type"</p>
<p>v-bind:value="'food'" v-on:change="data_type_set"&gt;</p>
<p>&lt;labelclass="form-check-label"for="food"&gt;</p>
<p>Food</p>
<p>&lt;/label&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;buttontype="submit"class="mt-3 btn btn-primary btn-md"</p>
<p>name="button"&gt;Summarize it!&lt;/button&gt;</p>
<p>&lt;/form&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;/template&gt;</p>
<p>&lt;script&gt;</p>
<p>importaxiosfrom'axios';</p>
<p>exportdefault&nbsp;{</p>
<p>name: 'Input',</p>
<p>data() {</p>
<p>return&nbsp;{</p>
<p>data: '',</p>
<p>error: '',</p>
<p>data_type: 'book',</p>
<p>};</p>
<p>},</p>
<p>mounted() {</p>
<p>this.data_type_set();</p>
<p>},</p>
<p>methods: {</p>
<p>data_type_set() {</p>
<p>this.$emit('radio', this.data_type);</p>
<p>},</p>
<p>asyncsubmit() {</p>
<p>this.error&nbsp;= '';</p>
<p>// Check if text is long enough</p>
<p>if&nbsp;(this.data.length&nbsp;&lt; 10) {</p>
<p>this.error&nbsp;= 'Enter a longer review.';</p>
<p>return;</p>
<p>}</p>
<p>constpath&nbsp;= 'http://localhost:5000/ping';</p>
<p>letstatus&nbsp;= false;</p>
<p>await&nbsp;axios.post(path, { data: this.data, data_type: this.data_type&nbsp;})</p>
<p>// eslint-disable-next-line no-unused-vars</p>
<p>.then((res) =&gt;&nbsp;{</p>
<p>status&nbsp;= true;</p>
<p>})</p>
<p>.catch((error) =&gt;&nbsp;{</p>
<p>// eslint-disable-next-line</p>
<p>console.log(error);</p>
<p>});</p>
<p>awaitthis.$emit('submit', status);</p>
<p>},</p>
<p>},</p>
<p>};</p>
<p>&lt;/script&gt;</p>
<p>&lt;style&gt;</p>
<p>.card&nbsp;{</p>
<p>background: #fff;</p>
<p>border-radius: 10px;</p>
<p>box-shadow: 014px28pxrgba(0, 0, 0, .25), 010px10pxrgba(0, 0, 0, .22);</p>
<p>position: relative;</p>
<p>overflow: hidden;</p>
<p>width: 720px;</p>
<p>max-width: 100%;</p>
<p>padding-left: 3vw;</p>
<p>padding-right: 3vw;</p>
<p>}</p>
<p>.shadow-textareatextarea.form-control::placeholder&nbsp;{</p>
<p>font-weight: 300;</p>
<p>}</p>
<p>.shadow-textareatextarea.form-control&nbsp;{</p>
<p>padding-left: 0.8rem;</p>
<p>}</p>
<p>&lt;/style&gt;</p>
<p>Most of it is built using BootstrapVue which has a lot of useful components. Read more about them here:</p>
<p><a href="https://www.google.com/url?q=https://bootstrap-vue.js.org/docs/components/&amp;sa=D&amp;ust=1576877610228000">https://bootstrap-vue.js.org/docs/components/</a></p>
<p>We then need to add the input component to Home.vue</p>
<p>&lt;divclass="row half-box"&gt;&lt;/div&gt;</p>
<p>&lt;b-card</p>
<p>v-bind:title="!inputStatus&nbsp;? 'Paste your'&nbsp;+ data_type&nbsp;+' review below!': 'Summarized!'"</p>
<p>class="card animated bounceInUp"&gt;</p>
<p>&lt;Inputv-if="!inputStatus" @submit="inputData" @radio="dataUpdate"/&gt;</p>
<p>&lt;/b-card&gt;</p>
<p>&lt;/div&gt;</p>
<p>The component has radio buttons which emit the data_type on change. This will change the b-card&rsquo;s title depending on if the user wants to summarize a book or food review. The user&rsquo;s pasted text, along with the currently selected button will be sent using an Axios POST request.</p>
<p>Let&rsquo;s now move on the server side.</p>
<p>Create a Python file called f.e App.py and start by importing Flask, Jsonify etc. We will need these later.</p>
<p>from&nbsp;flask import&nbsp;Flask, jsonify, request</p>
<p>from&nbsp;flask_cors import&nbsp;CORS</p>
<p>from&nbsp;summarizer import&nbsp;TextSummarizer</p>
<p>import&nbsp;json</p>
<p>Instantiate the Flask app and enable CORS</p>
<p># instantiate the app</p>
<p>app = Flask(__name__)</p>
<p>app.config.from_object(__name__)</p>
<p># enable CORS</p>
<p>CORS(app, resources={r'/*': {'origins': '*'}})</p>
<p>Now we&rsquo;re going to create a simple Axios POST config which will receive an array of strings for every pasted input form word. The Jsonify() returns a Flask.response() object that has the appropriate content-type header 'application/json' for use with json responses. The predicted_data variable will be used to do the summarization later on.</p>
<p>@app.route('/', methods=['POST'])</p>
<p>defreceiveMessage():</p>
<p>if&nbsp;request.method == 'POST':</p>
<p>post_data = request.get_json()</p>
<p>inputData = post_data['data']</p>
<p>typeOfSummarization = post_data['data_type']</p>
<p>print('type of Summarization '&nbsp;+ typeOfSummarization)</p>
<p>global&nbsp;predicted_data</p>
<p>predicted_data = ML(inputData, typeOfSummarization)</p>
<p>else:</p>
<p>print('error')</p>
<p>return&nbsp;jsonify(response_object)</p>
<p>We can also add the GET config</p>
<p># Send back summarization</p>
<p>@app.route('/', methods=['GET'])</p>
<p>defreturnSummarization():</p>
<p>global&nbsp;predicted_data</p>
<p>return&nbsp;jsonify(predicted_data)</p>
<p>Predicted data will contain the prediction received from the trained models. This process is explained in detail later.</p>
<p>defML(data, typeOfSummarization):</p>
<p>text_input = []</p>
<p>text_input.append(data)</p>
<p>print('Using:'&nbsp;+ typeOfSummarization)</p>
<p>if&nbsp;typeOfSummarization == 'book':</p>
<p>predicted_data = book_summarizer.predict(text_input)</p>
<p>elif&nbsp;typeOfSummarization == 'food':</p>
<p>predicted_data = food_summarizer.predict(text_input)</p>
<p>return&nbsp;predicted_data</p>
<p>Now let&rsquo;s initialize the models and load them into TextSummarizer</p>
<p>definit_summarizer&nbsp;(data_file_name):</p>
<p># Set paths to pretrained models</p>
<p>encoder_model_path = "./models/encoder_model_"&nbsp;+ data_file_name + ".h5"</p>
<p>decoder_model_path = "./models/decoder_model_"&nbsp;+ data_file_name + ".h5"</p>
<p># Set paths to corresponding tokenizers</p>
<p>x_tokenizer_path = "./models/x_tokenizer_"&nbsp;+ data_file_name + ".pickle"</p>
<p>y_tokenizer_path = "./models/y_tokenizer_"&nbsp;+ data_file_name + ".pickle"</p>
<p>return&nbsp;TextSummarizer(encoder_model_path, decoder_model_path, x_tokenizer_path, y_tokenizer_path)</p>
<p>And lastly let&rsquo;s call them and run the code.</p>
<p>if__name__&nbsp;== '__main__':</p>
<p># Name of the processed data</p>
<p>book = "Kindle_Reviews_Processed_100k"</p>
<p>food = "Food_Reviews_Processed_200k"</p>
<p># Initialize the summarizer with preloaded models and corresponding tokenizers</p>
<p>book_summarizer = init_summarizer(book)</p>
<p>food_summarizer = init_summarizer(food)</p>
<p>&nbsp;</p>
<p>app.run()</p>
<p>We are now done on the server side and can start implementing the response of the summarization on the client side.</p>
<p>To make things easy, let&rsquo;s create another Vue component named &ldquo;Output&rdquo; in</p>
<p>-/src/components/Output.vue</p>
<p>&lt;template&gt;</p>
<p>&lt;divclass="animated fadeIn"&gt;</p>
<p>&lt;divclass="overflow-auto box"&gt;</p>
<p>&lt;b-card-text&gt;</p>
<p>{{ msg&nbsp;}}</p>
<p>&lt;/b-card-text&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;buttontype="button"&nbsp;@click="emitBack" class="mt-4 btn btn-primary btn-md"&gt;Retry?&lt;/button&gt;</p>
<p>&lt;/div&gt;</p>
<p>&lt;/template&gt;</p>
<p>&lt;script&gt;</p>
<p>importaxiosfrom'axios';</p>
<p>exportdefault&nbsp;{</p>
<p>name: 'Output',</p>
<p>data() {</p>
<p>return&nbsp;{</p>
<p>msg: '',</p>
<p>};</p>
<p>},</p>
<p>methods: {</p>
<p>emitBack() {</p>
<p>this.msg&nbsp;= '';</p>
<p>this.$emit('retry', false);</p>
<p>},</p>
<p>getMessage() {</p>
<p>constpath&nbsp;= 'http://localhost:5000/ping';</p>
<p>axios.get(path)</p>
<p>.then((res) =&gt;&nbsp;{</p>
<p>this.msg&nbsp;=&nbsp;res.data;</p>
<p>})</p>
<p>.catch((error) =&gt;&nbsp;{</p>
<p>console.error(error);</p>
<p>});</p>
<p>},</p>
<p>},</p>
<p>created() {</p>
<p>this.getMessage();</p>
<p>},</p>
<p>};</p>
<p>&lt;/script&gt;</p>
<p>&lt;stylescoped&gt;</p>
<p>.card&nbsp;{</p>
<p>background: #fff;</p>
<p>border-radius: 10px;</p>
<p>box-shadow: 014px28pxrgba(0, 0, 0, .25), 010px10pxrgba(0, 0, 0, .22);</p>
<p>position: relative;</p>
<p>overflow: hidden;</p>
<p>width: 720px;</p>
<p>max-width: 100%;</p>
<p>padding: 5vw;</p>
<p>height: 360px;</p>
<p>}</p>
<p>.box{</p>
<p>height: 150px;</p>
<p>}</p>
<p>&lt;/style&gt;</p>
<p>The component simply makes a GET-request using Axios, receives the json output and displays it. It also features a retry button which renders the Input component when clicked.</p>
<p>We add the new component to App.vue and using conditional rendering, a simple boolean inputStatus decides to render it whenever the client has received the Flask request.</p>
<p>&lt;divclass="row half-box"&gt;&lt;/div&gt;</p>
<p>&lt;b-card</p>
<p>v-bind:title="!inputStatus&nbsp;? 'Paste your'&nbsp;+ data_type&nbsp;+' review below!': 'Summarized!'"</p>
<p>class="card animated bounceInUp"&gt;</p>
<p>&lt;Inputv-if="!inputStatus" @submit="inputData" @radio="dataUpdate"/&gt;</p>
<p>&lt;Outputv-else&nbsp;@retry="inputData"/&gt;</p>
<p>&lt;/b-card&gt;</p>
<p>&lt;/div&gt;</p>
<p>With both client and server up and running we can now move on to actually summarizing the text. This will be detailed in the following chapters.</p>
<h2>The Datasets</h2>
<p>The two datasets used for the implementation are called Amazon Fine Food Reviews&nbsp;and Amazon Reviews: Kindle Store Category&nbsp;and are available for download on Kaggle:</p>
<ul>
<li><a href="https://www.google.com/url?q=https://www.kaggle.com/snap/amazon-fine-food-reviews&amp;sa=D&amp;ust=1576877610252000">https://www.kaggle.com/snap/amazon-fine-food-reviews</a></li>
<li><a href="https://www.google.com/url?q=https://www.kaggle.com/bharadwaj6/kindle-reviews&amp;sa=D&amp;ust=1576877610253000">https://www.kaggle.com/bharadwaj6/kindle-reviews</a></li>
</ul>
<p>The datasets includes several categories, however, for the purpose of text summarization we only use the reviews and the corresponding summaries. Note that the summaries are very brief and more similar to a descriptive title rather than an actual summary. Short summaries are suitable as a starting point for researching the subject since the task of putting together longer and multiple sentences can be more complex.</p>
<p>Both datasets are given in csv-files (comma-separated values) and contains more than 500 000 reviews each. Naturally more data yields better results, however in this implementation we will only use 200 000 to reduce the model training time. Note that if your computer lacks cpu or gpu power, consider using even less data to speed up the model training.</p>
<p>Start by reading one of the datasets (the Kindle reviews in this demonstration). The goal is to train one model per dataset which means that the process described below should be repeated separately for both datasets.</p>
<p># Import libraries</p>
<p>import csv</p>
<p>import pandas as pd</p>
<p>pd.set_option("display.max_colwidth", 200)</p>
<p># Set path for input data (unprocessed)</p>
<p>data_input_path = "./data/kindle_reviews.csv"</p>
<p># Set path for output data (processed)</p>
<p>data_output_path = "./processed_data/Kindle_Reviews_Processed_200k.csv"</p>
<p># Column header titles (open the data file to get these names)</p>
<p>TEXT = "reviewText"</p>
<p>SUMMARY = "summary"</p>
<p># Load subset</p>
<p>num_reviews = 200000;</p>
<p>data = pd.read_csv(data_input_path, nrows=num_reviews)</p>
<p>Make sure to remove duplicates and missing values (Null/NaN)</p>
<p># Remove duplicates and NA from the dataset</p>
<p>data.drop_duplicates(subset=[TEXT],inplace=True)</p>
<p>data.dropna(axis=0,inplace=True)</p>
<h2>Preprocessing the Data</h2>
<p>Before data can be used for training and testing, it is always important to clean it up by preprocessing it. When working with text data, it is recommended to first print out a couple of samples to learn the format. The goal is to get rid of unwanted symbols, characters and words.</p>
<p># Understand the format of the text</p>
<p># Print 10 first reviews</p>
<p>print(data[TEXT][:10])</p>
<p><img title="" src="assets/images/image19.png" alt="" /></p>
<p># Print 10 first summaries</p>
<p>print(data[SUMMARY][:10])</p>
<p><img title="" src="assets/images/image7.png" alt="" /></p>
<p>We can see from these outputs that the texts contains contractions, punctuations and terms called stopwords. Typical stopwords are: a, an, and, any, are, as, it, its, just, these, they, this, to, we, was, were, etc. These words are shared between most documents and are not contributing to help distinguish between one document from another. The stopwords are imported from nltk.corpus. To import them you will first need to download them by typing the following code in a python terminal.</p>
<p>import nltk</p>
<p>nltk.download()</p>
<p>This will open up a GUI for managing downloads. In the GUI, simply click Corpora tab and download stopwords.</p>
<p>Below, we define a class with two static functions for cleaning up the summaries and the texts.</p>
<p># Import libraries</p>
<p>import re</p>
<p>from bs4 import BeautifulSoup</p>
<p>from nltk.corpus import stopwords</p>
<p># Use english stopwords</p>
<p>stop_words = set(stopwords.words('english'))</p>
<p>To replace contractions to their base form, we define a list of contractions. The list is derived from:</p>
<p><a href="https://www.google.com/url?q=https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python&amp;sa=D&amp;ust=1576877610257000">https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python</a></p>
<p># A list for mapping contractions with their base forms</p>
<p>contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is", "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will", "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are", "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have", "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}</p>
<p>The full class with comments is defined as follows:</p>
<p>class DataCleaner(object):</p>
<p>"""Class for cleaning text data"""</p>
<p>@staticmethod</p>
<p>def clean_text(text):</p>
<p># Convert all words to lowercase</p>
<p>new_string = text.lower()</p>
<p># Remove HTML tags</p>
<p>new_string = BeautifulSoup(new_string, "lxml").text</p>
<p># Remove text inside parentheses</p>
<p>new_string = re.sub(r'\([^)]*\)', '', new_string)</p>
<p># Remove citations</p>
<p>new_string = re.sub('"','', new_string)</p>
<p># Perform contraction mapping (replace contraction with full words)</p>
<p>new_string = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in new_string.split(" ")])</p>
<p># Remove &lsquo;s</p>
<p>new_string = re.sub(r"'s\b", "", new_string)</p>
<p># Remove punctuations and special characters (non-letters)</p>
<p>new_string = re.sub("[^a-zA-Z]", " ", new_string)</p>
<p># Remove stopwords</p>
<p>tokens = [w for w in new_string.split() if not w in stop_words]</p>
<p># Remove short words</p>
<p>long_words = []</p>
<p>for i in tokens:</p>
<p>if len(i)&gt;=3:</p>
<p>long_words.append(i)</p>
<p>return (" ".join(long_words)).strip()</p>
<p>@staticmethod</p>
<p>def clean_summary(text):</p>
<p># Convert all words to lowercase</p>
<p>new_string = text.lower()</p>
<p># Remove citations</p>
<p>new_string = re.sub('"','', new_string)</p>
<p># Perform contraction mapping (replace contraction with full words)</p>
<p>new_string = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in new_string.split(" ")])</p>
<p># Remove &lsquo;s</p>
<p>new_string = re.sub(r"'s\b", "", new_string)</p>
<p># Remove punctuations and special characters (non-letters)</p>
<p>new_string = re.sub("[^a-zA-Z]", " ", new_string)</p>
<p>tokens = new_string.split()</p>
<p>new_string = ''</p>
<p># Remove short words</p>
<p>for i in tokens:</p>
<p>if len(i)&gt;1:</p>
<p>new_string = new_string+i+' '</p>
<p>return new_string</p>
<p>Save the class in a separate file, import it and use it to clean up the text data.</p>
<p># Import local class file for cleaning the text data</p>
<p>from cleaner import DataCleaner</p>
<p># Clean the reviews</p>
<p>cleaned_text = []</p>
<p>for t in data[TEXT]:</p>
<p>cleaned_text.append(DataCleaner.clean_text(t))</p>
<p># Clean summarizes</p>
<p>cleaned_summary = []</p>
<p>for t in data[SUMMARY]:</p>
<p>cleaned_summary.append(DataCleaner.clean_summary(t))</p>
<p>When the data has been cleaned, to avoid having to redo the whole process again, it is recommended to save it to a new file for future uses.</p>
<p># Save the processed data to a new csv-file</p>
<p>with open(data_output_path, "w", newline='') as csv_file:</p>
<p>fieldnames = ['Summary', 'Text']</p>
<p>writer = csv.DictWriter(csv_file, fieldnames=fieldnames)</p>
<p>writer.writeheader()</p>
<p>for i in range(len(cleaned_summary)):</p>
<p>writer.writerow({'Summary': cleaned_summary[i], 'Text': cleaned_text[i]})</p>
<p>The final step before we start analyzing the data is to add the special tokens START and END in the beginning and end of each summary. For good measure, we import the saved file and use that as our new data source.</p>
<p># Set file path to the saved file</p>
<p>data_file_path = data_output_path</p>
<p># Read processed data</p>
<p>data = pd.read_csv(data_file_path)</p>
<p>data['Summary'].replace('', np.nan, inplace=True)</p>
<p>data.dropna(axis=0, inplace=True)</p>
<p># Add special tokens START in the beginning and END at the end of all summaries</p>
<p>data['Summary'] = data['Summary'].apply(lambda x : '_START_ '+ x + '_END_')</p>
<p>Print out some of the processed data and to inspect the result.</p>
<p># Print out the top 5 processed reviews and summaries</p>
<p>for i in range(5):</p>
<p>print("Review: ", data['Text'][i])</p>
<p>print("Summary: ", data['Summary'][i])</p>
<p>print("\n")</p>
<p><img title="" src="assets/images/image20.png" alt="" /></p>
<h2>Analyzing the Data</h2>
<p>In this phase, we will try to understand the approximate distribution of words for the reviews and summaries. This is important to know when we set the maximum length of the sequences. First we count the words in the texts, then we plot out the lengths of the texts in a histogram.</p>
<p>import matplotlib.pyplot as plt</p>
<p>text_word_count = []</p>
<p>summary_word_count = []</p>
<p># Count words in the reviews</p>
<p>for i in data['Text']:</p>
<p>text_word_count.append(len(i.split()))</p>
<p># Count words in the summaries</p>
<p>for i in data['Summary']:</p>
<p>summary_word_count.append(len(i.split()))</p>
<p># Analyze the distribution of sequences by looking at the length of the texts</p>
<p>length_df = pd.DataFrame({'text':text_word_count, 'summary':summary_word_count})</p>
<p># Plot a histogram</p>
<p>length_df.hist(bins = 30)</p>
<p>plt.show()</p>
<p><img title="" src="assets/images/image11.png" alt="" /></p>
<p>From the histograms it is seen that the majority of summaries contains less than ten words; the reviews less than 80 words. Set these values as the maximum sequence lengths.</p>
<p># From the histogram we learned that most reviews has the length 80 and summaries has length 10</p>
<p>max_len_text = 80</p>
<p>max_len_summary = 10</p>
<h2>Split the Data</h2>
<p>Now it is time to split the data into training sets and validation sets. For this we will use train_test_split from sklearn. The data is split into 90% for training the model and 10% for validating the performance.</p>
<p># Split the dataset into a training and validation set (90% train, 10% val)</p>
<p>from sklearn.model_selection import train_test_split</p>
<p>x_train, x_validation, y_train, y_validation = train_test_split(data['Text'], data['Summary'], test_size=0.1, random_state=0, shuffle=True)</p>
<p>To convert the text sequences into integer sequences, tokenizers are used. The tokenizers also builds the entire vocabulary for the model. Next step is to use the training data to create tokenizers for both the reviews (x_train) and the summaries (y_train).</p>
<p># Include libraries</p>
<p>from keras.preprocessing.text import Tokenizer</p>
<p>from keras.preprocessing.sequence import pad_sequences</p>
<p>from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional</p>
<p>from tensorflow.keras.models import Model</p>
<p>from tensorflow.keras.callbacks import EarlyStopping</p>
<p># Review Tokenizer :</p>
<p># Prepare a tokenizer for reviews (x) on training data</p>
<p>x_tokenizer = Tokenizer()</p>
<p>x_tokenizer.fit_on_texts(list(x_train))</p>
<p># Convert string sequences into integer sequences</p>
<p>x_train = x_tokenizer.texts_to_sequences(x_train)</p>
<p>x_validation = x_tokenizer.texts_to_sequences(x_validation)</p>
<p># Padding zero to maximum length</p>
<p>x_train = pad_sequences(x_train, maxlen=max_len_text, padding='post')</p>
<p>x_validation = pad_sequences(x_validation, maxlen=max_len_text, padding='post')</p>
<p>x_vocabulary_size = len(x_tokenizer.word_index) + 1</p>
<p># Summary Tokenizer :</p>
<p># Prepare a tokenizer for summary (y) on training data</p>
<p>y_tokenizer = Tokenizer()</p>
<p>y_tokenizer.fit_on_texts(list(y_train))</p>
<p># Convert string sequences into integer sequences</p>
<p>y_train = y_tokenizer.texts_to_sequences(y_train)</p>
<p>y_validation = y_tokenizer.texts_to_sequences(y_validation)</p>
<p># Padding zero to maximum length</p>
<p>y_train = pad_sequences(y_train, maxlen=max_len_summary, padding='post')</p>
<p>y_validation = pad_sequences(y_validation, maxlen=max_len_summary, padding='post')</p>
<p>y_vocabulary_size = len(y_tokenizer.word_index) + 1</p>
<p>Finally the tokenizers should also be saved into&nbsp;pickle-files so that we can reuse them in the future with the trained model.</p>
<p>import pickle</p>
<p># Save x_tokenizer to file</p>
<p>with open('x_tokenizer.pickle', 'wb') as handle:</p>
<p>pickle.dump(x_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)</p>
<p># Save tokenizer to file</p>
<p>with open('y_tokenizer.pickle', 'wb') as handle:</p>
<p>pickle.dump(y_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)</p>
<h2>Building the Model</h2>
<p>By now all preparations are completed and it is time to build the model. We will be using a three stacked LSTM (Long Short-Term Memory network) for the encoder with the following settings:</p>
<ul>
<li>return_sequence = True (return the hidden state and cell state output for the full sequence)</li>
<li>return_state = True (return the last hidden state and cell state in addition to the output sequences)</li>
</ul>
<p>from keras import backend as K</p>
<p>K.clear_session()</p>
<p>latent_dim = 500</p>
<p># Encoder (embedding layer turns positive integers into dense vectors of fixed size)</p>
<p>encoder_inputs = Input(shape=(max_len_text,))</p>
<p>encoder_embedding_layer = Embedding(x_vocabulary_size, latent_dim, trainable=True)</p>
<p>encoder_embedding = encoder_embedding_layer(encoder_inputs)</p>
<p>#LSTM 1</p>
<p>encoder_lstm1 = LSTM(latent_dim, return_sequences=True, return_state=True)</p>
<p>encoder_output1, state_h1, state_c1 = encoder_lstm1(encoder_embedding)</p>
<p>#LSTM 2</p>
<p>encoder_lstm2 = LSTM(latent_dim, return_sequences=True, return_state=True)</p>
<p>encoder_output2, state_h2, state_c2 = encoder_lstm2(encoder_output1)</p>
<p>#LSTM 3</p>
<p>encoder_lstm3 = LSTM(latent_dim, return_state=True, return_sequences=True)</p>
<p>encoder_outputs, state_h, state_c = encoder_lstm3(encoder_output2)</p>
<p># Decoder</p>
<p>decoder_inputs = Input(shape=(None,))</p>
<p>decoder_embedding_layer = Embedding(y_vocabulary_size, latent_dim, trainable=True)</p>
<p>decoder_embedding = decoder_embedding_layer(decoder_inputs)</p>
<p>#LSTM using encoder_states as initial state</p>
<p>decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)</p>
<p>decoder_outputs, decoder_fwd_state, decoder_back_state = decoder_lstm(decoder_embedding, initial_state=[state_h, state_c])</p>
<p>Unfortunately Keras does not have an official attention layer support so we use a custom implementation found here: <a href="https://www.google.com/url?q=https://github.com/thushv89/attention_keras/blob/master/layers/attention.py&amp;sa=D&amp;ust=1576877610275000">https://github.com/thushv89/attention_keras/blob/master/layers/attention.py</a></p>
<p># Import custom third-party attention layer</p>
<p>from attention import AttentionLayer</p>
<p># Create attention layer</p>
<p>attention_layer = AttentionLayer(name='attention_layer')</p>
<p>attention_out, attention_states = attention_layer([encoder_outputs, decoder_outputs])</p>
<p># Concatenate attention output and decoder LSTM output</p>
<p>decoder_concat_input = Concatenate(axis=-1, name='concat_layer')([decoder_outputs, attention_out])</p>
<p># Dense layer</p>
<p>decoder_dense = TimeDistributed(Dense(y_vocabulary_size, activation='softmax'))</p>
<p>decoder_outputs = decoder_dense(decoder_concat_input)</p>
<p># Define the model</p>
<p>model = Model([encoder_inputs, decoder_inputs], decoder_outputs)</p>
<p>The next and final step in this phase is to compile and train the model. We use sparse categorical cross-entropy&nbsp;as the loss function. With this option an integer sequence is converted to a one-hot vector automatically which helps us to overcome memory issues. This also allow us to keep integer sequences as targets (predictions). A one-hot vector is used to distinguish each word in a vocabulary from every other word in the vocabulary.</p>
<p># Compile the model with Sparse Categorial Cross-entropy as the loss function</p>
<p>model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')</p>
<p>Utilize early stoppage to stop training the neural network as soon as the validation loss starts increasing.</p>
<p># Stop training the neural network at the right time by monitoring a user-specified metric.</p>
<p># Here the model will stop training once the validation loss (val_loss) increase.</p>
<p>early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1)</p>
<p># Train the model</p>
<p>history=model.fit(</p>
<p>[x_train, y_train[:,:-1]],</p>
<p>y_train.reshape(y_train.shape[0], y_train.shape[1], 1)[:,1:],</p>
<p>epochs=10,</p>
<p>callbacks=[early_stop],</p>
<p>batch_size=512,</p>
<p>validation_data=([x_validation, y_validation[:,:-1]], y_validation.reshape(y_validation.shape[0], y_validation.shape[1], 1)[:,1:]))</p>
<p>When the training is complete, it is always a good idea to save the model since the training can take several hours depending on the size of the data.</p>
<p>model.save("model.h5")</p>
<p>Even though we use early stoppage, it can be interesting to look at the loss and validation loss in a plot to understand the behaviour of the model.</p>
<p># Plot a few diagnostic plots to understand the behavior of the model over time</p>
<p>from matplotlib import pyplot</p>
<p>pyplot.plot(history.history['loss'], label='train')</p>
<p>pyplot.plot(history.history['val_loss'], label='test')</p>
<p>pyplot.legend()</p>
<p>pyplot.show()</p>
<p><img title="" src="assets/images/image8.jpg" alt="" /></p>
<p>In this case the validation loss started to increase at epoch 10.</p>
<h2>Inference Phase</h2>
<p>Now it is time to set up the encoder and decoder to finally test our trained model.</p>
<p># Encoder inference</p>
<p>encoder_model = Model(inputs=encoder_inputs, outputs=[encoder_outputs, state_h, state_c])</p>
<p># Decoder inference</p>
<p># Below tensors will hold the states of the previous time step</p>
<p>decoder_state_input_h = Input(shape=(latent_dim,))</p>
<p>decoder_state_input_c = Input(shape=(latent_dim,))</p>
<p>decoder_hidden_state_input = Input(shape=(max_len_text, latent_dim))</p>
<p># Get the embeddings of the decoder sequence</p>
<p>decoder_embedding2 = decoder_embedding_layer(decoder_inputs)</p>
<p># To predict the next word in the sequence, set the initial states to the states from the previous time step</p>
<p>decoder_outputs2, state_h2, state_c2 = decoder_lstm(decoder_embedding2, initial_state=[decoder_state_input_h, decoder_state_input_c])</p>
<p># Attention inference</p>
<p>attention_out_inference, attention_states_inference = attention_layer([decoder_hidden_state_input, decoder_outputs2])</p>
<p>decoder_inference_concat = Concatenate(axis=-1, name='concat')([decoder_outputs2, attention_out_inference])</p>
<p># A dense softmax layer to generate prob dist. over the target vocabulary</p>
<p>decoder_outputs2 = decoder_dense(decoder_inference_concat)</p>
<p># Final decoder model</p>
<p>decoder_model = Model(</p>
<p>[decoder_inputs] + [decoder_hidden_state_input, decoder_state_input_h, decoder_state_input_c],</p>
<p>[decoder_outputs2] + [state_h2, state_c2])</p>
<p>Same as before, the models should be saved so they can be loaded in the future.</p>
<p># Save model and architecture to files</p>
<p>encoder_model.save("encoder_model.h5")</p>
<p>decoder_model.save("decoder_model.h5")</p>
<p>In the inference process of actually predicting the summary of a review we use the encoder and decoder models created above. We define the following function.</p>
<p>def decode_sequence(input_seq):</p>
<p># Make sure the input sequence is not longer than max text length</p>
<p>input_seq = input_seq.reshape(1, max_len_text)</p>
<p># Encode the input as state vectors.</p>
<p>e_out, e_h, e_c = encoder_model.predict(input_seq)</p>
<p># Generate empty target sequence of length 1.</p>
<p>target_seq = np.zeros((1,1))</p>
<p># Chose the 'start' word as the first word of the target sequence</p>
<p>target_seq[0, 0] = target_word_index['start']</p>
<p>stop_condition = False</p>
<p>decoded_sentence = ''</p>
<p>while not stop_condition:</p>
<p>output_tokens, h, c = decoder_model.predict([target_seq] + [e_out, e_h, e_c])</p>
<p># Sample a token</p>
<p>sampled_token_index = np.argmax(output_tokens[0, -1, :])</p>
<p>if (sampled_token_index == 0):</p>
<p>stop_condition = True</p>
<p>else:</p>
<p>sampled_token = reverse_target_word_index[sampled_token_index]</p>
<p>if(sampled_token != 'end'):</p>
<p>decoded_sentence += ' ' + sampled_token</p>
<p># Exit condition: either hit max length or find stop word.</p>
<p>if (len(decoded_sentence.split()) &gt;= (max_len_summary-1)):</p>
<p>stop_condition = True</p>
<p>&nbsp;</p>
<p># Update the target sequence (of length 1).</p>
<p>target_seq = np.zeros((1,1))</p>
<p>target_seq[0, 0] = sampled_token_index</p>
<p># Update internal states</p>
<p>e_h, e_c = h, c</p>
<p>return decoded_sentence</p>
<p>Before we can start testing, we need two functions to convert integer sequences to word sequences: one for the review and one for the summary.</p>
<p># Functions to convert an integer sequence to a word sequence</p>
<p>def seq2summary(input_seq):</p>
<p>newString = ''</p>
<p>for i in input_seq:</p>
<p>if((i!=0 and i!=target_word_index['start']) and i!=target_word_index['end']):</p>
<p>newString = newString + reverse_target_word_index[i] + ' '</p>
<p>return newString</p>
<p>def seq2text(input_seq):</p>
<p>newString = ''</p>
<p>for i in input_seq:</p>
<p>if(i!=0):</p>
<p>newString = newString + reverse_source_word_index[i] + ' '</p>
<p>return newString</p>
<p>Finally we test the model by generating summaries for a few reviews from the validation batch.</p>
<p># Print sample results</p>
<p>num_predictions = 20</p>
<p>for i in range(num_predictions):</p>
<p>print("Review:", seq2text(x_validation[i]))</p>
<p>print("Original summary:", seq2summary(y_validation[i]))</p>
<p>print("Predicted summary:", decode_sequence(x_validation[i]))</p>
<p>print("\n")</p>
<h2>Results and Discussion</h2>
<p>We trained two separate models with the two data sets: food reviews and Kindle reviews with the presented python implementation. Below are a few example outputs from both data sets using the validation data.</p>
<p>Kindle</p>
<p><img title="" src="assets/images/image21.png" alt="" /></p>
<p><img title="" src="assets/images/image23.png" alt="" /></p>
<p><img title="" src="assets/images/image16.png" alt="" /></p>
<p><img title="" src="assets/images/image12.png" alt="" /></p>
<p><img title="" src="assets/images/image27.png" alt="" /></p>
<p><img title="" src="assets/images/image2.png" alt="" /></p>
<p><img title="" src="assets/images/image22.png" alt="" /></p>
<p><img title="" src="assets/images/image4.png" alt="" /></p>
<p>Food</p>
<p><img title="" src="assets/images/image25.png" alt="" /></p>
<p><img title="" src="assets/images/image24.png" alt="" /></p>
<p><img title="" src="assets/images/image5.png" alt="" /></p>
<p><img title="" src="assets/images/image10.png" alt="" /></p>
<p><img title="" src="assets/images/image1.png" alt="" /></p>
<p><img title="" src="assets/images/image6.png" alt="" /></p>
<p><img title="" src="assets/images/image15.png" alt="" /></p>
<p><img title="" src="assets/images/image18.png" alt="" /></p>
<p>Even though the predicted summary and original are not identical in most cases, they often have the same meaning. One problem is that the generated predictions can be quite repetitive but this is expected since a lot of human generated summaries are the same, and the vocabulary of the model is based on those summaries. Another observation is that, for the kindle data set, the predictions are biased in the way that they are very rarely negative. This is probably because of the lack of negative reviews in the data set.</p>
<h2>References</h2>
<p>[1] <a href="https://www.google.com/url?q=https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/&amp;sa=D&amp;ust=1576877610287000">https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/</a></p>
<p>[2]</p>
<p><a href="https://www.google.com/url?q=https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/&amp;sa=D&amp;ust=1576877610288000">https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/</a></p>
<p>The <a href="https://rubiks-cube-solver.com/">Rubik's Cube solver</a> can fix 2x2 cubes and Pyraminx puzzles too. Set the scrambled configuration and let the program find the solution in seconds.</p>
            <vue-embed-gist
              gist-id="f801f1236fa6511a1730b542ab86c03b"
              file="fwafwa"/>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<script src="https://gist.github.com/samuelllsvensson/464d2960b3a1a6c74186115d8c0e6612.js"></script>
<script>
import VueEmbedGist from 'vue-embed-gist';

export default {
  components: {
    VueEmbedGist,
  },
  data() {
    return {
      lazyLoad: false,
      shortName: 'flashcms',
      id: 'unique',
      contentImageUrl: 'https://images.idgesg.net/images/article/2018/01/emerging-tech_ai_machine-learning-100748222-large.jpg',
    };
  },
};
</script>

<style lang="scss" scoped>
$border-radius-size: 14px;

*,
*:before,
*:after {
  box-sizing: border-box;
}

.hidden {
  visibility: hidden;
}

.avatar {
  width: 70px;
  height: 70px;
  border-radius: 50%;

  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

.avatar-text {
  margin-bottom: 0 !important;
}

.content-text {
  font-size: 20px;
  line-height: 40px;
}

.container-box {
  height: 300px;
}

.bg-image {
  background-position: center;
  background-size: cover;
  height: 500px;
}

img {
  height: 300px;
}
</style>
