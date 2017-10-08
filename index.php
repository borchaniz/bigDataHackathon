<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <style>
            @font-face {
                font-family: 'digital';
                src: url('digital.ttf');
            }
            body{
              background-image: url("bg.jpg");
                background-repeat: no-repeat;
                background-size: cover;
            }
            .navbar-default{
                background-color: rgba(214,214,214,0.6);
                border: none;
                -webkit-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                -moz-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
            }
            form{
                background-color: rgba(214,214,214,0.6);
                align: center;
                width:40%;
                padding: 20px;
                margin-top: 120px;
                -webkit-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                -moz-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
            }
            img{
                background-color: rgba(214,214,214,0.6);
                align: center;
                padding: 20px;
                margin-top: 40px;
                -webkit-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                -moz-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);

            }
            h2{
                margin-top:80px;
            }
            h1{

                font-family: digital;
                font-size: 1200%;
            }
            #a{
                background-color: rgba(214,214,214,0.6);
                -webkit-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                -moz-box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
                box-shadow: 1px 2px 10px -2px rgba(0,0,0,0.75);
            }
        </style>
    </head>
    <body >
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Can I Travel?</a>
            </div>
            <ul class="nav navbar-nav navbar-right">
                <li><a>by Greens Beans Potatoes Tomatoes</a></li>
            </ul>
        </div>
    </nav>
    <?php
    if ((isset($_POST['dep']))&&(isset($_POST['arr']))&&(isset($_POST['fin']))&&(isset($_POST['debut']))&&(isset($_POST['sel']))){
    exec('python ./script.py'.' '.$_POST['dep'].' '.$_POST['arr'].' '.$_POST['debut'].' '.$_POST['fin'].' '.$_POST['sel'], $output, $ret_code);
    $f=fopen("b.txt","r");
    $res=fgets($f);
    ?>
        <div class="container-fluid">
        <div class="row">
            <div class="col-xs-12 col-md-6">
                <?php echo "<div id='a'><center><h2 style='padding-top: 30px; font-size: 300%'>Best Departure Time</h2><br><h1 style='margin-top: -3%'>".$res.":00</h1></center></div>"?>


            </div>
            <div class="col-xs-12 col-md-6">
                <img src="foo.png" width="100%">
            </div>
        </div>
        </div>

    <?php }
    else {
?>
    <center><form action="" method="POST">
        <h4>Trajet</h4>
        <div class="row">
            <div class="col-xs-6">
                <div class="form-group">
                    <select id="dep" name="dep" class="form-control">
                        <option value="tn">Tunis</option>
                        <option value="sf">Sfax</option>
                        <option value="nb">Nabeul/Cap Bon</option>
                        <option value="mn">Monastir/Sousse</option>
                    </select>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="form-group">
                    <select id="arr" name="arr" class="form-control">
                        <option value="tn">Tunis</option>
                        <option value="sf">Sfax</option>
                        <option value="nb">Nabeul/Cap Bon</option>
                        <option value="mn">Monastir/Sousse</option>
                    </select>
                </div>
            </div>
        </div>
        <h4>Période</h4>
        <div class="row">
            <div class="col-xs-6">
                <div class="form-group">
                    <input name="debut" type="datetime-local" class="form-control" class="col-xs-6">
                </div>
            </div>
            <div class="col-xs-6">
                <div class="form-group">
                    <input name="fin" type="datetime-local" class="form-control" class="col-xs-6">
                </div>
            </div>
        </div>
        <div class="form-group">
            <select name="sel" type="time" class="form-control" class="col-xs-6">
                <option value="prop">Je Propose</option>
                <option value="cher">Je Cherche</option>
            </select>
        </div>
        <button type="submit" class="btn btn-default fbutton">Submit</button>
    </form>
    </center><?php } ?>
    </body>
</html>