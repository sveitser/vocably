<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name=cd "viewport" content="width=device-width, initial-scale=1" />
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
                <div style="width: 100%; height: 173px; position: relative; text-align: center;">
                    <img src="/img/monkey.png" alt="image" />
                </div>
                <h1>
                    Vocably
                </h1>
                <div style="float:center">
                    <a type="button" href="/login">Submit</a>
                </div>

                <form action="/login">
                    <div id="checkboxes3" data-role="fieldcontain">
                        <p>Vocably will access your Google Mail account. We do not save any of your information.</p>
                           <fieldset data-role="controlgroup" data-type="vertical">
                            <input id="checkbox4" name="" type="checkbox" />
                            <label for="checkbox4">
                                I agree to the terms.
                            </label>
                        </fieldset>
                    </div>
                    <input value="Submit" type="submit" />
                </form>
            </div>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>
