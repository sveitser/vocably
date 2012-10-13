<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/css/style.css" />
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js">
        </script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js">
        </script>
        <script src="/js/main.js">
        </script>
    </head>
    <body>
        <!-- Home -->
        <div data-role="page" id="page1">
            <div data-role="content">
                <div style="width: 40px; height: 35px; text-align: center; position: relative;">
                    <img src="/img/monkey_sm.png" alt="image" />
                </div>
                <h2>Words of the day</h2>
                    <div data-role="collapsible-set">
                    %for key in word_defs:
                        <div data-role="collapsible" class="collapsible">
                            <h3>{{key}}</h3>
                            <p>{{word_defs[key]}}</p>
                        </div>
                    %end
                    </div>
                <h2>{{user_score}} words known</h2>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>
