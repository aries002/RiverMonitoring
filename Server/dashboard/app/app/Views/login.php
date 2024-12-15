<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="<?php echo base_url("dist/bootstrap/css/bootstrap.min.css"); ?>">

    <style>
        #debug-icon {
            display: none;
        }

        html,
        body {
            height: 100%;
        }

        body {
            display: flex;
            align-items: center;
            padding-top: 40px;
            padding-bottom: 40px;
            background-color: #ffdb6d;
        }

        .form-signin {
            width: 100%;
            max-width: 400px;
            padding: 30px;
            margin: auto;
            background: #ffffff;
            border-radius: 10px;
        }

        .form-signin .checkbox {
            font-weight: 400;
        }

        .form-signin .form-floating:focus-within {
            z-index: 2;
        }
    </style>
</head>

<body>

    <main class="form-signin">
        <form method="post" action="">
            <div class="mb-3" style="text-align:center;">
                <h2 style="font-weight:bold;-webkit-text-stroke: 5px #000000;paint-order:stroke fill;">
                    <span style="color:red;">Sungai</span> <span style="color:yellow;">Monitoring</span>
                </h2>
            </div>
            <h1 class="h3 mb-3 fw-normal">Login</h1>

            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="username" name="username" placeholder="Username" autofocus>
                <label for="username">Username</label>
            </div>
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="password" name="password" placeholder="Password">
                <input type="hidden" name="lgnid" value="<?php echo $_SESSION['tokens']; ?>" />
                <label for="password">Password</label>
            </div>

            <button class="w-100 btn btn-lg btn-warning" type="submit">Login</button>
        </form>
    </main>

</body>

</html>