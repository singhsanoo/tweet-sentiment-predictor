<!DOCTYPE html>
<html>

<head>
  <!-- These three elements must come first! -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- CSS files will be here -->
    <link rel="stylesheet" href="static/bootstap.min.css" media="screen">
  <link rel="stylesheet" href="static/style.css">
  <link rel="stylesheet" href="static/reset.css">

  <!-- Import Bootstsrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

  <!-- Give it a title -->
  <title>Tweet Sentiment Predictor</title>

</head>

<header>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <!-- <a class="navbar-brand" href="index.html" style="color: #3ca5fb; padding-left: 10px; font-size: 25px;" >Navbar</a> -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href="#" >Tweet Sentiment Predictor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href={{ url_for("word") }}>Word Collage</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href={{ url_for("team") }}>Team</a>
        </li>

      </ul>
    </div>

  </nav>
  <div class="two-toned-header-color"></div>
</header>
<body style="width: 100vw" style="margin:auto">

  <style>
    body {
      background-image: url(static/images/twitter_logos_top_r_corner.png);
      background-repeat: no-repeat;
      background-size: cover;
    }
    </style>
  <div class="top-space border">

  </div>
  <!-- <div class="container"> -->

  <!-- <style>
    body {
      background-image: url('../Resources/twitter_logos_top_r_corner.webp');
      background-repeat: no-repeat;
      background-size: cover;
      width: fit-content;
      height: fit-content;
    }
  </style> -->
  <div class="border" id="page-content" style="width: 100%">

    <div class="row">
      <div class="col-md-12 text-center">
        <h1 style="font-size: 10vh;">Twitter Sentiment Type</h1>
        <div class="spacer-1" style="padding-block: 25px;">

        </div>
        <h3>Enter your tweet into the box to see predicted Sentiment!</h3>
        <br>
      </div>
    </div>

    <!-- Input section using a form and the Hypertext Transfer Protocol (HTTP) POST method -->
    <!-- Pass the form input to 'url_for'.  Make sure that the url_for argument matches the route method name  in app.py -->
    <form action="{{url_for('predict')}}" method="post">

      <!-- Use a Jinja if-statement to fill the previous values from the Flask server if data has been entered -->
      <div class="my-4" style="display:flex; justify-content: center;">
        <!-- <div class="spacer-2" style="padding-block:25px;">

        </div> -->
        <div>
          <H5 class="text-end" style="font-size: 56px">Tweet Input</H5>
          <br>
        </div>

        <div class="mx-3">
          <input type="text" name="tweet-input" id="tweet-input" style="height:90px; width: 400px; font-size: 25px; border-radius: 15px;" placeholder="tweet-input"  required="required" {% if features %} value="" {% endif %} />
        </div>
        <div>
          <button type="submit" class="btn btn-primary" style="height:90px; width: 90px; font-size: 40px; background-color: white; border: 3px solid black;border-radius: 15px; padding-bottom: 13px; margin-left: 0px;"><img src="static/images/verification-mark.png" alt="" height="50px" width="50px"> </button>
        </div>
      </div>

        {% if pred_txt_lrc_p %}
        <div class="col-md-12 predict-results-box d-flex justify-content-center">

          <div class="bg-light p-5" style="width:fit-content; border-radius: 8px;">
            <h3>Tweet Input </h3>
            <h5 style="font-style:italic;">{{ features }}</h5>
            <hr>
            <div class="d-flex justify-content-center gap-5">
              <div>
                <h3> Logistic Regression Classifier </h3>
                <h4>Positive : {{ pred_txt_lrc_p }}%</h4>
                <progress value="{{ pred_txt_lrc_p }}" max="100"></progress>
                <h4>Negative : {{ pred_txt_lrc_n }}%</h4>
                <progress value="{{ pred_txt_lrc_n }}" max="100"></progress>
              </div>

              <div>
                <h3> Stochastic Gradient Descent </h3>
                <h4>Positive : {{ pred_txt_clf_p }}%</h4>
                <progress value="{{ pred_txt_clf_p }}" max="100"></progress>
                <h4>Negative : {{ pred_txt_clf_n }}%</h4>
                <progress value="{{ pred_txt_clf_n }}" max="100"></progress>
              </div>

              <div>
                <h3> Multinomial Naive Bayes </h3>
                <h4>Positive : {{ pred_txt_mnb_p }}%</h4>
                <progress value="{{ pred_txt_clf_p }}" max="100"></progress>
                <h4>Negative : {{ pred_txt_mnb_n }}%</h4>
                <progress value="{{ pred_txt_clf_n }}" max="100"></progress>
              </div>

              <div>
                <h3> Light Gradient-Boosting </h3>
                <h4>Positive : {{ pred_txt_lgb_p }}%</h4>
                <progress value="{{ pred_txt_lgb_p }}" max="100"></progress>
                <h4>Negative : {{ pred_txt_lgb_n }}%</h4>
                <progress value="{{ pred_txt_lgb_n }}" max="100"></progress>
                <!-- <div class="progress">
                <div class="progress-bar bg-warning w-{{ pred_txt_lgb_n }}" role="progressbar" aria-valuenow="{{ pred_txt_lgb_n }}" aria-valuemin="0" aria-valuemax="100"></div>
                </div> -->
              </div>

            </div>
          </div>
        </div>

        {% elif cannot_predict %}
        <div class="col-md-12 predict-results-box d-flex justify-content-center">
          <div class="bg-light p-5" style="width:fit-content; border-radius: 8px;">
            <h3>Tweet Input </h3>
            <h5 style="font-style:italic;">{{ features }}</h5>
            <hr>
            <h4>{{ cannot_predict }}</h4>
          </div>
        </div>

        {% endif %}

      <!-- </div> -->

    </form>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    </div>

</body>

<!-- jQuery CDN -->
<script type="text/javascript" hef="#" src="https://code.jquery.com/jquery-2.1.4.min.js"></script>

<!-- Start footer -->
<footer class="footer-bottom navbar-fixed-bottom" id="footer-index">
  <div class="two-toned-footer-color">
    
  </div>
  <p class="text-muted text-muted-footer text-center"> 
        Machine Learning Tweet Sentiment Predictor
  </p>
</footer>

</html>

 <style>
    body {
      background-image: url(static/images/twitter_logos_top_r_corner.png);
      background-repeat: no-repeat;
      background-size: cover;
    }
    </style>

          <!-- team starts -->
          <section class="team section-padding" id="team">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                    <div style="padding: 5%;">
                        <div class="section-header text-center pb-5">
                            <h1>Positive Vs Negative</h1>
                        </div>
                        <div class="section-header text-center pb-5">
                          <h1>Word Collage</h1>
                      </div>
                    </div>
                    </div>
                </div>
                <div class="row" style="margin-right: -20%">
                    <div class="col-12 col-md-6 col-lg-5">
                        <div class="card text-center">
                            <div class="card-body">
                                <img alt="" class="img-fluid rounded-circle" src="#">
                                <img src="static/images/thumbs_up.png">
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-md-6 col-lg-5">
                        <div class="card text-center">
                            <div class="card-body">
                                <img alt="" class="img-fluid rounded-circle" src="3">
                                <img src="static/images/thumbs_down.png">

                            </div>
                        </div>
                    </div>
                    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>




  <!-- jQuery CDN -->
  <script type="text/javascript" hef="#" src="https://code.jquery.com/jquery-2.1.4.min.js"></script>

  <!-- Bootstrap CDN -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

  <!DOCTYPE html>
<html>

<head>
  <!-- These three elements must come first! -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- CSS files will be here -->
  <link rel="stylesheet" href="static/style.css">
  <link rel="stylesheet" href="static/reset.css">
  <link rel="stylesheet" href="static/bootstap.min.css" media="screen">
  <!-- Import Bootstsrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

  <!-- Give it a title -->
  <title>Tweet Sentiment Predictor</title>

</head>

<header>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <!-- <a class="navbar-brand" href="index.html" style="color: #3ca5fb; padding-left: 10px; font-size: 25px;" >Navbar</a> -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href={{ url_for("home") }}>Tweet Sentiment Predictor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href={{ url_for("word") }}>Word Collage</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: #3ca5fb; font-size: 20px;" href="#">Team</a>
        </li>

      </ul>
    </div>

  </nav>
  <div class="two-toned-header-color"></div>
</header>

<body>

  <style>
    body {
      background-image: url(static/images/twitter_logos_top_r_corner.png);
      background-repeat: no-repeat;
      background-size: cover;
    }
    </style>

    <div class="container">

      <div class="row">
        <div class="col-md-12 text-center">
          <!-- team starts -->
        <section class="team section-padding" id="team">
          <div class="container">
              <div class="row">
                  <div class="col-md-12">
                  <div style="padding: 5%;">
                      <div class="section-header text-center pb-5">
                          <h1>Our Team</h1>
                      </div>
                  </div>
                  </div>
              </div>
              <div class="row">
                  <div class="col-12 col-md-6 col-lg-4" id="card-size">
                      <div class="card text-center">
                          <div class="card-body">
                              <img alt="" class="img-fluid rounded-circle" src="static/images/brandon.jpeg" id= scuff>
                              <h3 class="card-title py-2 name-set">Brandon Groenewold</h3>
                          <br>
                              <h5 class="name">Comapay agents house</h5><h7 class="desc">is a long established fact that eader&nbsp; will be distracted by the readable content.</h7>
                          </br>

                          </div>
                      </div>
                  </div>
                  <div class="col-12 col-md-6 col-lg-4">
                      <div class="card text-center">
                          <div class="card-body">
                              <img alt="" class="img-fluid rounded-circle" src="static/images/jon.png" id= scuff>
                              <h3 class="card-title py-2 name-set">Jon Kwiatkowski</h3>
                              <br>
                              <h5 class="name">Comapay agents house</h5><h7 class="desc">is a long established fact that eader&nbsp; will be distracted by the readable content.</h7>
                          </br>
                          </div>
                      </div>
                  </div>
                  <div class="col-12 col-md-6 col-lg-4">
                      <div class="card text-center">
                          <div class="card-body">
                              <img alt="" class="img-fluid rounded-circle" src="static/images/sanoo.jpeg" id= scuff>
                              <h3 class="card-title py-2 name-set">Sanoo Singh</h3>
                              <br>
                              <h5 class="name">Comapay agents house</h5><h7 class="desc">is a long established fact that eader&nbsp; will be distracted by the readable content.</h7>
                          </br>
                          </div>
                      </div>
                  </div>

                  <div class="col-12 col-md-6 col-lg-4">
                      <div class="card text-center">
                          <div class="card-body">
                              <img alt="" class="img-fluid rounded-circle" src="static/images/nhan.jpeg" id= scuff>
                              <h3 class="card-title py-2 name-set">Nhan Tran</h3>
                              <br>
                              <h5 class="name">Comapay agents house</h5><h7 class="desc">is a long established fact that eader&nbsp; will be distracted by the readable content.</h7>
                          </br>
                          </div>
                      </div>
                  </div>
                  <div class="col-12 col-md-6 col-lg-4">
                    <div class="card text-center">
                        <div class="card-body">
                            <img alt="" class="img-fluid rounded-circle" src="static/images/adrian_profile.jpg" id= scuff>
                            <h3 class="card-title py-2 name-set">Adrian Wood</h3>
                            <br>
                            <h5 class="name">Comapay agents house</h5><h7 class="desc">is a long established fact that eader&nbsp; will be distracted by the readable content.</h7>
                        </br>
                        </div>
                  </div>

                  </div>
                </div>
              </div>
          </div>
      </section><!-- team ends -->

      </form>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>




  <!-- jQuery CDN -->
  <script type="text/javascript" hef="#" src="https://code.jquery.com/jquery-2.1.4.min.js"></script>

  </body>
<!-- Start footer -->
<footer class="footer-bottom navbar-fixed-bottom" id="footer-index">
  <div class="two-toned-footer-color"></div>
      <p class="text-muted text-muted-footer text-center"> 
           Machine Learning Tweet Sentiment Predictor
      </p>
</footer>
  
  </html>