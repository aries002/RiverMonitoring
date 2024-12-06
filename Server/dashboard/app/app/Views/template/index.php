<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Website">
    <meta name="author" content="Website">

    <title><?php echo $title; ?></title>
    <link rel="shortcut icon" type="image/png" href="<?php echo base_url('dist/images/icon-round.png'); ?>" />
    <link rel="stylesheet" type="text/css" href="<?php echo base_url('dist/bootstrap/css/bootstrap.min.css'); ?>">
    <link href="<?php echo base_url('dist/main/css/nunito.css'); ?>" rel="stylesheet" />
    <link href="<?php echo base_url('dist/select2/select2.min.css'); ?>" rel="stylesheet" />
    <link href="<?php echo base_url('dist/fontawesome/css/all.min.css'); ?>" rel="stylesheet" type="text/css">
    <link href="<?php echo base_url('dist/datetimepicker/bootstrap-material-datetimepicker.css'); ?>" rel="stylesheet"
        type="text/css">

    <link href="<?php echo base_url('dist/main/css/template.css'); ?>" rel="stylesheet" />
    <style>
        #debug-icon {
            display: none;
        }
    </style>

    <script src="<?php echo base_url('dist/main/js/jquery.1.12.4.min.js'); ?>"></script>
</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">
        <?php echo $_sidebar_menu; ?>

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">
                <?php echo $_header; ?>

                <!-- Begin Page Content -->
                <div class="container-fluid" id="containerfluid">
                    <div class="row">
                        <div class="col-lg-1" id="sideleft"></div>
                        <div class="col-lg-10" id="contentmain">
                            <div class="content-wrap">
                                <?php
                                echo $_content;
                                ?>
                            </div>
                        </div>
                        <div class="col-lg-1" id="sideright"></div>
                    </div>
                </div>
                <!-- /.container-fluid -->
            </div>
            <!-- End of Main Content -->

            <?php echo $_footer; ?>
        </div>
        <!-- End of Content Wrapper -->
    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class=" scroll-to-top" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>


    <!-- Modal -->
    <div class="modal fade" id="confirm-modal" tabindex="-1" aria-labelledby="confirmLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="box-shadow: 0px 0px 25px 3px #333;">
                <div class="modal-header" id="confirm-head">
                    <h5 class="modal-title" id="confirm-title"></h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"
                        aria-label="Close"></button>
                </div>
                <div class="modal-body" id="confirm-body">

                </div>
                <div class="modal-footer">
                    <!-- <button type="button" class="btn btn-secondary" id="confirm-cancel" data-bs-dismiss="modal">Close</button> -->
                    <button type="button" class="btn btn-warning hide" id="confirm-warning"></button>
                    <button type="button" class="btn btn-danger hide" id="confirm-danger"></button>
                    <button type="button" class="btn btn-info hide" id="confirm-info"></button>
                    <button type="button" class="btn btn-primary hide" id="confirm-primary"></button>
                    <button type="button" class="btn btn-success hide" id="confirm-success"></button>
                </div>
            </div>
        </div>
    </div>


    <div class="position-fixed top-0 end-0 p-3" style="z-index: 10331">
        <div id="liveToast" class="toast align-items-center text-white border-0 bg-secondary" role="alert"
            aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body" id="toastmsg">
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"
                    aria-label="Close"></button>
            </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="<?php echo base_url('dist/bootstrap/js/bootstrap.bundle.min.js'); ?>"></script>

    <!-- Custom scripts for all pages-->
    <script src="<?php echo base_url('dist/main/js/script.js'); ?>"></script>
    <script src="<?php echo base_url('dist/datetimepicker/moment-with-locales.min.js'); ?>"></script>
    <script src="<?php echo base_url('dist/datetimepicker/bootstrap-material-datetimepicker.js'); ?>"></script>

    <script src="<?php echo base_url('dist/select2/select2.min.js'); ?>"></script>
    <script src="<?php echo base_url('dist/main/js/moment.min.js'); ?>"></script>
</body>

</html>