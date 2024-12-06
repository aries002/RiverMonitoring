<div class="offcanvas offcanvas-start" style="z-index:11112;" tabindex="-1" id="offcanvasWithBackdrop"
    aria-labelledby="offcanvasWithBackdropLabel">
    <div class="offcanvas-header">
        <h6 class="offcanvas-title d-none d-sm-block" id="offcanvas"></h6>
        <button type="button" class="btn-close text-reset sideclosebtn mt-3" data-bs-dismiss="offcanvas"
            aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
        <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-start" id="menu">
            <?php
            if ($_SESSION["level"] == 1) {
                ?>
                <li>
                    <a href="<?php echo base_url('dashboard'); ?>" class="nav-link text-truncate">
                        <i class="fa-solid fa-gauge"></i> <span>Dashboard</span>
                    </a>
                </li>
                <!-- <li>
                <a href="<?php echo base_url('pengaturan'); ?>" class="nav-link text-truncate">
                    <i class="fa-solid fa-gear"></i> <span>Pengaturan</span>
                </a>
                </li> -->
                <!-- <li>
                    <a href="<?php echo base_url('bantuan'); ?>" class="nav-link text-truncate">
                        <i class="fa-solid fa-circle-question"></i> <span>Bantuan</span>
                    </a>
                </li> -->
                <?php
            } else {
                ?>
                <!-- <li>
                    <a href="<?php echo base_url('pengaturan'); ?>" class="nav-link text-truncate">
                        <i class="fa-solid fa-gear"></i> <span>Pengaturan</span>
                    </a>
                </li> -->
                <?php
            }
            ?>
        </ul>
    </div>
    <a href="<?php echo base_url("home/logout"); ?>" class="nav-link text-truncate" id="btnlogout">
        <i class="fa-solid fa-right-from-bracket"></i> <span>Logout</span></a>
</div>