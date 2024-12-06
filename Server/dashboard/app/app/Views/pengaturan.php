<style>
    #dtadd0 {
        display: none;
    }
</style>
<div class="container">
    <div class="row">
        <div class="col-md-2"></div>
        <div class="col-md-8">

            <h2>Ubah Password</h2>
            <hr>
            <div style="width:100%;text-align:center;"><?php echo $info; ?></div>
            <form method="post" action="">
                <div class="mb-3">
                    <label>Password Saat Ini</label>
                    <input type="password" class="form-control" name="passnow" />
                </div>
                <div class="mb-3">
                    <label>Password Baru</label>
                    <input type="password" class="form-control" name="passnew1" />
                </div>
                <div class="mb-3">
                    <label>Ulangi Password Baru</label>
                    <input type="password" class="form-control" name="passnew2" />
                </div>
                <button type="submit" class="btn btn-primary" name="simpan">Simpan</button>
            </form>

        </div>
        <div class="col-md-2"></div>
    </div>
</div>